from django import template
from django.contrib.admin.models import LogEntry
from django.template import RequestContext, Context, Variable, Template, TemplateSyntaxError
from django.utils.safestring import mark_safe
from django.shortcuts import render_to_response, render, get_object_or_404, redirect

from replica.pulse.models import Entry, Draft, Topic, Media, Channel, CodeBlock
from replica import settings as ReplicaSettings

register = template.Library()

class RenderAsTemplateNode(template.Node):
    def __init__(self, item_to_be_rendered):
        self.item_to_be_rendered = Variable(item_to_be_rendered)

    def render(self, context):
        try:
            actual_item = self.item_to_be_rendered.resolve(context)
            return Template(actual_item).render(context)
        except template.VariableDoesNotExist:
            return ''

@register.inclusion_tag('replica/cms/components/_header.html', takes_context=True)
def componentHeader(context, user=None):
	request = context['request']
	u = request.user
	return {'user_obj':u, 'request':request }

@register.inclusion_tag('replica/cms/templatetags/month_links_snippet.html')
def render_entry_months(username):
	dates = Entry.objects.filter(user=username).dates('pub_date', 'month')
	return { 'dates': dates, }

@register.inclusion_tag('replica/cms/templatetags/nav_list_topics.html')
def render_nav_topic_list(num=9999):
    topics = Topic.objects.all().order_by('title')[:num]
    return { 'object_list': topics, }

@register.simple_tag
def render_counts(obj_type):
	if obj_type == 'topic':
		obj_count = Topic.objects.count()
	elif obj_type == 'published':
		obj_count = Entry.objects.published().count()
	elif obj_type == 'upcoming':
		obj_count = Entry.objects.upcoming().count()
	elif obj_type == 'idea':
		obj_count = Entry.objects.ideas().count()
	elif obj_type == 'channel':
		obj_count = Channel.objects.all().count()
	elif obj_type == 'media':
		obj_count = Media.objects.all().count()
	elif obj_type == 'page':
		obj_count = Entry.objects.pages().count()
	elif obj_type == 'entry':
		obj_count = Entry.objects.all().count()
	else:
		obj_count = '0'
	return obj_count

@register.simple_tag
def render_codeblock(slug=None):
    code = get_object_or_404(CodeBlock, type=1, slug=slug)
    context = Context({"title": code.title })
    template = Template(code.template_html)
    return template.render(context)

@register.tag(name='render_as_template')
def render_as_template(parser, token):
    bits = token.split_contents()
    if len(bits) !=2:
        raise TemplateSyntaxError("'%s' takes only one argument (a variable representing a template to render)" % bits[0])
    return RenderAsTemplateNode(bits[1])

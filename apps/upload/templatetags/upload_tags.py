from django import template

register = template.Library()

#take current context of template
#@register.simple_tag(takes_context=True)
@register.simple_tag(takes_context=True)

#return most recent video in separate dictionary
def display_grid(context):
	data={}
	size = len(context['media'])
	d=0
	c=0
	grid = 4

	while size != 0:
		if size <= grid:
			data[d] = context['media'][c:]
			size = size - len(context['media'][c:])
		else:
			data[d] = context['media'][c:c+grid]
			size = size - len(context['media'][c:c+grid])
		d+=1
		c+=grid

	context['data'] = data
	return ''
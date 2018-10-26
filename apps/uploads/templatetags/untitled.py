from django import template

register = template.Library()

#take current context of template
#@register.simple_tag(takes_context=True)
@register.simple_tag(takes_context=True)

#take context list object and create 4 col grid, cut out most recent upload
def display_grid(context):
	data={}
	listSize = len(context['upload_obj'])
	d=0
	c=0
	grid = 4

	while listSize != 0:
		if listSize <= grid:
			data[d] = context['upload_obj'][c:]
			listSize = listSize - len(context['upload_obj'][c:])
		else:
			data[d] = context['upload_obj'][c:c+grid]
			listSize = listSize - len(context['upload_obj'][c:c+grid])
		d+=1
		c+=grid

	context['data'] = data
	return ''
	
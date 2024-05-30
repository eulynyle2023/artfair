from django import template

register = template.Library()

@register.simple_tag  # This decorator registers the tag as a simple tag
def is_active(request, url):
  return url == request.path
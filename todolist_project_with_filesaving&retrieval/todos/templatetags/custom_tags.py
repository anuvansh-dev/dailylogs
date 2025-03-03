from django import template
from todos.models import BackgroundImage

register = template.Library()

@register.simple_tag
def get_background_image():
    background = BackgroundImage.objects.first()
    if background and background.image:
        return background.image.url
    return "/static/todos/images/default_bg.jpg"

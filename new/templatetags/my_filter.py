from django import template
from datetime import datetime
register = template.Library()


@register.filter('my_greet'):
    
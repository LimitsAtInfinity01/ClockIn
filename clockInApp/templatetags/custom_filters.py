from django import template

register = template.Library()

@register.filter
def format_timedelta(value):
    if value:
        total_seconds = int(value.total_seconds())
        hours, remainder = divmod(total_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        if hours < 1:
            return f"{minutes} minutes and {seconds:02} seconds"
        return f"{hours:02} hours with {minutes:02} and {seconds:02}"
    return ""

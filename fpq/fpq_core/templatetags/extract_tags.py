from django.template import Library


register = Library()


def tags(tags) -> list:
    return [str(name) for name in tags.all()]


register.filter('tags', tags)

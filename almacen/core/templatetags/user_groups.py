from django import template

register = template.Library()

@register.filter(name='has_group')
def has_group(user, group_name):
    # verificar si el usuario pertenece a un grupo
    return user.groups.filter(name=group_name).exists() # devulve un valor booleano
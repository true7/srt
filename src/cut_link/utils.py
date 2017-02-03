import string
import random
from django.conf import settings

SHORTLINK_MIN = getattr(settings, "SHORTLINK_MIN", 6)


def code_generator(size=SHORTLINK_MIN):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(size))


def create_shortlink(instance):
    new_link = code_generator()
    class_ = instance.__class__
    query_set = class_.objects.filter(shortlink=new_link)
    if query_set.exists():
        return create_shortlink()
    return new_link

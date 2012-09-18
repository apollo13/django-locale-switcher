from collections import namedtuple

from django.core.urlresolvers import reverse
from django.conf import settings
from django.utils import translation

locale_info = namedtuple('locale_info', ['language_code', 'language_name', 'url', 'active'])
def locale_switcher(request):
    data = {'locale_switcher': []}
    info = request.resolver_info
    # Translate the lanuages first:
    lang_names = [translation.ugettext(i[1]) for i in settings.LANGUAGES]
    for (lang_code, _), lang_name in zip(settings.LANGUAGES, lang_names):
        with translation.override(lang_code):
            url = reverse(info[0], args=info[1], kwargs=info[2])
            data['locale_switcher'].append(locale_info(lang_code, lang_name, url, False))
    return data

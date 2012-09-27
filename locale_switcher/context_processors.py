from collections import namedtuple

from django.core.urlresolvers import reverse
from django.conf import settings
from django.utils import translation

locale_info = namedtuple('locale_info', ['language_code', 'language_name', 'url', 'active'])
def locale_switcher(request):
    data = {'locale_switcher': []}
    rm = request.resolver_match
    # Translate the lanuages first:
    lang_names = [translation.ugettext(i[1]) for i in settings.LANGUAGES]
    for (lang_code, _), lang_name in zip(settings.LANGUAGES, lang_names):
        with translation.override(lang_code):
            url = reverse(rm.url_name, args=rm.args,
                          kwargs=rm.kwargs, current_app=rm.app_name)
            data['locale_switcher'].append(locale_info(lang_code, lang_name, url,
                                           lang_code == request.LANGUAGE_CODE))
    return data

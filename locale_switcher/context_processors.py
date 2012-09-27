from collections import namedtuple

from django.core.urlresolvers import reverse
from django.conf import settings
from django.utils import translation
from django.utils.functional import lazy


locale_info = namedtuple('locale_info', ['language_code', 'language_name', 'url', 'active'])


def locale_switcher(request):
    def _get_locale_switcher():
        data = []
        rm = request.resolver_match
        # Translate the lanuages first:
        lang_names = [translation.ugettext(i[1]) for i in settings.LANGUAGES]
        for (lang_code, _), lang_name in zip(settings.LANGUAGES, lang_names):
            with translation.override(lang_code):
                url = reverse(rm.url_name, args=rm.args,
                              kwargs=rm.kwargs, current_app=rm.app_name)
                data.append(locale_info(lang_code, lang_name, url,
                                        lang_code == request.LANGUAGE_CODE))
        return data
    return {'locale_switcher': lazy(_get_locale_switcher, list)}

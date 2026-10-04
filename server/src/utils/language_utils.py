import gettext
import re
import unicodedata
from functools import lru_cache

import pycountry

from models.language import Language

DEFAULT_UI_LANGUAGE = "en"

# The most spoken languages, shown on top in this order. The rest follow alphabetically.
_COMMON_LANGUAGES = [
    "en", "zh", "hi", "es", "fr", "ar", "bn", "pt", "ru", "ur",
    "id", "de", "ja", "tr", "ko", "vi", "it", "th", "fa", "pl",
]

# pycountry names its translation catalogs by locale, not always by language code.
_CATALOGS = {"zh": "zh_CN", "nb": "nb_NO"}


@lru_cache(maxsize=None)
def _translation(language_code: str) -> gettext.NullTranslations | None:
    """pycountry's language-name translations into language_code, if it has them."""
    try:
        return gettext.translation(
            "iso639-3", pycountry.LOCALES_DIR, languages=[_CATALOGS.get(language_code, language_code)]
        )
    except FileNotFoundError:
        return None


def _name(language, translation: gettext.NullTranslations | None) -> str:
    name = translation.gettext(language.name) if translation else language.name
    # Keep the first of alternative names ("中文; 汉语") and drop ISO qualifiers
    # such as "Modern Greek (1453-)".
    return re.sub(r"\s*\(.*\)$", "", name.split(";")[0]).strip()


def _sort_key(name: str) -> str:
    """Orders accented letters with their base letter ("Árabe" under A)."""
    return "".join(c for c in unicodedata.normalize("NFKD", name) if not unicodedata.combining(c)).casefold()


@lru_cache(maxsize=None)
def get_languages(ui_language: str = DEFAULT_UI_LANGUAGE) -> list[Language]:
    """All ISO 639-1 languages named in ui_language (English when there is no
    translation for it), the most common first."""
    ui_language = ui_language.lower()
    translation = None if ui_language == DEFAULT_UI_LANGUAGE else _translation(ui_language)
    if translation is None:
        ui_language = DEFAULT_UI_LANGUAGE
    languages = [
        (language.alpha_2, _name(language, translation), _name(language, _translation(language.alpha_2)))
        for language in pycountry.languages
        if hasattr(language, "alpha_2")
    ]
    common = {code: position for position, code in enumerate(_COMMON_LANGUAGES)}
    languages.sort(key=lambda l: (common.get(l[0], len(common)), _sort_key(l[1])))
    return [
        Language(code=code, name_language_code=ui_language, name=name, native_name=native_name, weight=weight)
        for weight, (code, name, native_name) in enumerate(languages)
    ]

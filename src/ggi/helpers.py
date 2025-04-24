from typing import List, Optional
import requests

from ggi.supported_langs import SUPPORTED_LANGS

GH_GITIGNORE_TEMPLATES_URL = "https://api.github.com/gitignore/templates"


def get_gitignore(lang: str) -> str:
    url = f"{GH_GITIGNORE_TEMPLATES_URL}/{lang}"
    req = requests.get(url)
    data = req.json()
    return data["source"]


def write_gitignore(dir: str, overwrite: bool, gitignore: str) -> None:
    file = f"{dir}/.gitignore"
    mode = "w" if overwrite else "a"
    with open(file, mode) as f:
        f.write(gitignore)


def get_available_langs() -> str:
    req = requests.get(GH_GITIGNORE_TEMPLATES_URL)
    return req.json()


def check_lang_support(lang: str, remote: bool = False) -> str:
    lang = lang.lower()
    langs = get_available_langs() if remote else SUPPORTED_LANGS
    ok = next((lg for lg in langs if lang == lg.lower()), None)
    return ok if ok else None


def convert_list_to_str(ls: List[str]) -> str:
    return "\n".join(ls)


def sanity_check_lang(lang: str) -> Optional[str]:
    ok = check_lang_support(lang)
    if ok is None:
        ok = check_lang_support(lang, True)
    return ok

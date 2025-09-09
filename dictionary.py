import json
import re
from unidecode import unidecode

with open(r"C:\Users\dotra\Downloads\Flet\dictionary.json", "r", encoding="utf-8") as f:
    dictionary = json.load(f)
with open(r"C:\Users\dotra\Downloads\Flet\dictionary_viet_anh.json", "r", encoding="utf-8") as f:
    dictionary_viet_anh = json.load(f)

def extract_en_word(s):
    match = re.match(r"^([^\s{]+)", s)
    return match.group(1) if match else s

def search_anh_viet(word):
    for key, mean in dictionary.items():
        if key.strip().lower().startswith(word):
            clean = mean.replace("# English:: Vietnamese dictionary extracted from http://en.wiktionary.org/", "").strip()
            return key, clean
    return None, None

def search_viet_anh(word):
    word_no_diacritics = unidecode(word)
    for mean, eng in dictionary_viet_anh.items():
        mean_compare = unidecode(mean.strip().lower())
        if mean_compare.startswith(word_no_diacritics):
            clean = eng.replace("# Vietnamese:: English dictionary extracted from http://vi.wiktionary.org/", "").strip()
            return mean, clean
    return None, None
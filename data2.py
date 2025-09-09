import json

# Đọc file Anh-Việt
with open("dictionary.json", "r", encoding="utf-8") as f:
    dict_en_vi = json.load(f)
dict_vi_en = {}

for en_word, vi_mean in dict_en_vi.items():
    vi_mean_clean = vi_mean.lstrip(":").strip()
    meanings = [m.strip() for m in vi_mean_clean.split(",")]
    for m in meanings:
        if m:
            dict_vi_en[m] = en_word
with open("dictionary_viet_anh.json", "w", encoding="utf-8") as f:
    json.dump(dict_vi_en, f, ensure_ascii=False, indent=4)

print("Đảo ngược từ điển xong!")
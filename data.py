import requests
import json
#Link tới file dict.txt trên Github
url = "https://raw.githubusercontent.com/open-dsl-dict/wiktionary-dict/refs/heads/master/src/en-vi-enwiktionary.txt"
#Tải dữ liệu
print("Đang tải dữ liệu từ Github")
respone = requests.get(url)

if respone.status_code == 200:
    dictionary = {}
    lines = respone.text.splitlines()
    for line in lines:
        if ":" in line:
            word, meaning = line.strip().split(":", 1)
            dictionary[word.strip()] = meaning.strip()
    #Lưu thành dictionary json
    with open("dictionary.json","w", encoding="utf-8") as f:
        json.dump(dictionary, f, ensure_ascii=False, indent=4)
        print("Đã tạo file dictionary.json thành công")
        print(f"Số lượng từ vựng: {len(dictionary)}")
else:
    print("Lỗi khi tải dữu liệu từ Github")
    

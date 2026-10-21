import json
import re

DATA_PATH = r"C:\Users\ddonn\Downloads\Bible_Reader\reference_lookup\Bible-json-main\Bible-json-main\versions\en\KING JAMES BIBLE.json"
VERSIONS = r"C:\Users\ddonn\Downloads\Bible_Reader\reference_lookup\Bible-json-main\Bible-json-main\versions\en"
LANG = r""


def load_bible(path = DATA_PATH):
    with open(path,"r",encoding="utf-8")as f:
        data = json.load(f)
    
    book_names = list(data.keys())
    return data, book_names

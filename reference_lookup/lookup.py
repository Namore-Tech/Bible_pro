def get_verse(data, book, chapter, verse):
    try:
        return data[book][str(chapter)][str(verse)]
    except KeyError:
        return f"sorry couldn't find {book} chapter{chapter} verse{verse}."
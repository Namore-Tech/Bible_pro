from loader import load_bible
from parser import parse_reference
from lookup import get_verse
from STT import listen_and_transcribe

transcript = listen_and_transcribe()
bible_data, book_names = load_bible()

result = parse_reference(transcript, book_names)
if result:
    book, chapter, verse = result
    verse_text = get_verse(bible_data, book, chapter, verse)
    print(verse_text)
else:
    print("Sorry i didn't catch a valid scripture reference")
import re
from rapidfuzz import fuzz, process 
from word2number import w2n

PATTERN = re.compile(
    r"([a-zA-Z0-9]+?)\s+chapter\s+([a-zA-Z0-9\-]+)\s+verse\s+([a-zA-Z0-9\-]+)", re.IGNORECASE
)

def parse_reference(transcript,book_names, threshold = 70):
    match =PATTERN.search(transcript)

    if not match:
        return None

    raw_book, raw_chapter, raw_verse = match.groups()
    print(f"DEBUG raw groups: book={raw_book!r},chapter={raw_chapter!r},verse={raw_verse!r}")
    try:
        chapter = w2n.word_to_num(raw_chapter.strip())
        verse = w2n.word_to_num(raw_verse.strip())
    except ValueError:
        return None

    result = process.extractOne(
        raw_book.strip(),
        book_names,
        scorer= fuzz.token_sort_ratio
    )

    if result is None:
        return None

    matched_book, score,_ = result
    if score < threshold:
        return None
    return (matched_book, chapter, verse)
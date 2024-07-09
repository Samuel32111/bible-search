import json
from docx import Document

def docx_to_json(file_path):
    document = Document(file_path)
    bible_data = []

    for paragraph in document.paragraphs:
        # Assuming each paragraph is a verse with format "Book Chapter:Verse Text"
        if paragraph.text.strip():
            parts = paragraph.text.split(" ", 1)
            if len(parts) > 1:
                book_chapter = parts[0]
                text = parts[1]
                book, chapter_verse = book_chapter.split(" ", 1)
                chapter, verse = chapter_verse.split(":", 1)
                bible_data.append({
                    "book": book,
                    "chapter": int(chapter),
                    "verse": int(verse),
                    "text": text
                })

    return bible_data

# Update the path to your Bible Word document
file_path = 'C:\\Users\Zamfir12\Desktop\\bible_conversion\\-bible.docx'
-convert_to_json.py
bible_data = docx_to_json(file_path)

with open('bible.json', 'w') as json_file:
    json.dump(bible_data, json_file, indent=4)

import ebooklib
from ebooklib import epub

import nltk
from epub_conversion.utils import open_book, convert_epub_to_lines
from bs4 import BeautifulSoup
import html2text


def readEpub(filename):
    # book = epub.read_epub(filename)
    book = open_book(filename)
    lines = convert_epub_to_lines(book)
    return html2text.html2text(''.join(lines))
    # soup = BeautifulSoup(lines)
    # print(soup.get_text('\n'))

    # german_corpus = []

    # for doc in book.get_items():
    #     doc_content = str(doc.content)
    #     for w in nltk.word_tokenize(doc_content):
    #         german_corpus.append(w.lower())
    #     print(german_corpus)
    # for item in book.get_items():
    #     if item.get_type() == ebooklib.ITEM_DOCUMENT:
    #         print('==================================')
    #         print('NAME : ', item.get_name())
    #         print('----------------------------------')
    #         print(item.get_content())
    #         print('==================================')
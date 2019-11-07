import os
from django.conf import settings
from striprtf.striprtf import rtf_to_text
from .txt import get_txt_word


def get_rtf_text(filename):
    raw_text = get_txt_word(filename)
    text = rtf_to_text(raw_text)
    

    return text
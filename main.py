import os
import numpy as  np
import re
import spacy
import urllib.request

def poem_generator(file, word, n_sents=4):
    nlp = spacy.load("es")
    init_str = nlp(word)


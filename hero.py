#!/usr/bin/env python

import json
import os
import pycorpora
import random
import requests
import shutil
import string
import tempfile

full_path = os.path.dirname(os.path.realpath(__file__)) + "/"
data_files_path = full_path + "data_files/"

def make_hero():
    rand = random.randint(0,10)
    dbrand = random.randint(0,20)
    pre = ""
    post = ""
    special = ""
    if rand > 7:
        pre = random.choice(open(data_files_path + 'pre').readlines())
    if rand < 8:
        post = random.choice(open(data_files_path + 'post').readlines())
    adjective = random.choice(pycorpora.words.adjs['adjs']) + " "
    noun = random.choice(pycorpora.words.nouns['nouns']) + " "
    if dbrand > 18:
        special = random.choice(open(data_files_path + 'special').readlines())
    hero = special + pre + adjective + noun + post
    print string.capwords(hero.replace("\n", " "))
    return string.capwords(hero.replace("\n", " "))

def get_image_url(query):
    giphyurl = "https://api.giphy.com/v1/gifs/search"
    api_key = "%GIPHY_API_KEY%"
    i = requests.get(
        giphyurl + "?q=" + query + "&api_key=" + api_key + "&limit=1&rating=R")
    image_url = str(i.json()['data'][0]['images']['original']['url'])
    return image_url

def get_image(url):
    i = requests.get(url, stream=True, timeout=15)
    with tempfile.NamedTemporaryFile(delete=False, suffix=".gif") as f:
        i.raw.decode_content = True
        shutil.copyfileobj(i.raw, f)
        f.close()
        return f.name

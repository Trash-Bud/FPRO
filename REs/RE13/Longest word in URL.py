# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 11:38:24 2020

@author: Joana
"""
import re
import string
ponct = ["!",".",",","?",":",";"]
def longest_word(url):
    import urllib.request
    response = urllib.request.urlopen(url)
    html = response.read().decode()
    ref = urllib.request.urlopen('https://raw.githubusercontent.com/fpro-feup/public/master/assigns/13/words')
    wl = ref.read().decode()  
    wl = wl.split("\n")
    wl = sorted(wl, key = lambda x: (- len(x), x))
    html = re.sub('['+string.punctuation+']', '', html).split() 
    for word in wl:
        if word in html:
            return word
        
#!/usr/bin/env python
# coding: utf-8

# In[1]:
from konlpy.tag import Okt
from tqdm import tqdm

def getnouns(x, q):
    twit = Okt()
    result = []
    for i in tqdm(x):
        result.append(twit.nouns(i))
    q.put(result)


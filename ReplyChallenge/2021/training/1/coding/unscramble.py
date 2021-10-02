#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import hashlib

# Check if w and d have exactly the same letters, but not in the same order. 
# Return 1 if yes, 0 if not 
def sameLetters(w, d):
    if len(w) != len(d):
        return 0
    letterOfD = list(d)
    for l in w:
        if l in letterOfD:
            p = letterOfD.index(l)    # find position of the letter l
            del(letterOfD[p])         # delete it (to avoid something likes find waves with saves wich have all letter in it but use 2 times the 's')
        elif not l in letterOfD:
            return 0
        if len(letterOfD)==0:
            break
    return 1


def getUnscrambledWords(dic, words_lists):
    tabUnscrambledWords = []
    for w in words_lists:
        isInDic = False
        for d in dic: 
            if w == d:
                isInDic = True
                break
            if sameLetters(w, d) > 0:
                tabUnscrambledWords+=d
                print(f'{w} : {d}')
                break
        if isInDic:
            tabUnscrambledWords+=w
    return tabUnscrambledWords

if __name__ == '__main__':
    with open('scrambled-words.txt','r') as file_scrambled:
        with open('dictionary.txt','r') as dic:
            dic = dic.read().split()
            wScrambled = file_scrambled.read().split()
            listResult = getUnscrambledWords(dic, wScrambled)
            result = ''.join(listResult)
            print("-"*70)
            print("Result ? "+str(not (result=='')))
            print("-"*70)
            print("{FLG:"+str(hashlib.sha256(result.encode()).hexdigest())+"}")
            print("-"*70)
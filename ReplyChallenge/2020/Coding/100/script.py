#!/usr/bin/env python3

import re
import time

# Get the time remaining with calculating the past average 5
def timeRemaining(initLast5, endLast5, currentPercentage):
    return int((100-currentPercentage) * ((endLast5-initLast5)/5)) 

# Check if the word is possibly the same and check if only one character is different and return it
def checkNGetDiff(word, wordInDic):
    word=word.lower()
    if len(word) != len(wordInDic): #or len(word)<5:
        return ''
    cptErr = 0
    letterErr = ''
    for i, letter in enumerate(word):
        if letter != wordInDic[i]:
            cptErr+=1
            letterErr = letter
        if cptErr>1:
            return ''
    #print(f'{word} | {wordInDic} : {letterErr}')
    return letterErr

# return sentence composed with word wich are not in dictionnary
def findDiff(book):
    result = ""
    try:
        with open('words.txt', 'r') as dictionnary:
            words = book.split(' ')
            dictionnary = dictionnary.read().split('\n')
            dictionnary = [i.lower() for i in dictionnary] # Avoid miscapture from caps
            cpt = 0
            lastPercentage = 0
            initTimeLast5 = time.time()
            for word in words:
                word = word.lower()

                # INFORMATION PRINTING
                currentPercentage = int((cpt/len(words))*100)
                if currentPercentage != lastPercentage:
                    lastPercentage = currentPercentage
                    info = f'[+] {currentPercentage}%'
                    if (currentPercentage % 5 == 0 and currentPercentage != 0):
                        info += f' | {timeRemaining(initTimeLast5, time.time(), currentPercentage)}s remaining'
                        initTimeLast5 = time.time()
                    print(info) 

                # LOGIC
                if not word in dictionnary:
                    for dicWord in dictionnary:
                        if word.lower == dicWord:
                            break
                        else:
                            if '{' in word:
                                result+="{"
                                result+="\n"
                                word = word.replace('{','')
                            if '}' in word:
                                word = word.replace('}','')
                                result+="}"
                                result+="\n"
                            checkResult = checkNGetDiff(word, dicWord)
                            result+= checkResult
                            if checkResult != '':
                                result+=' '
                            
                cpt+=1

    except KeyboardInterrupt:
        with open('output.txt', 'wb') as r:
            r.write(result.encode())
            
    return result

with open('The Time Machine by H. G. Wells.txt', 'r') as f:
    book = f.read().replace('\n',' ')\
        .replace('\"',' ')\
        .replace("--",' ')\
        .replace("-",' ')\
        .replace('_',' ')\
        .replace('.',' ')\
        .replace('?',' ')\
        .replace('!',' ')\
        .replace(',',' ')\
        .replace(';',' ')\
        .replace('(',' ')\
        .replace(')',' ')\
        .replace('\'',' ')\
        .replace(':',' ')\
        .replace('#',' ')\
        .replace(',',' ')\
        .replace('  ',' ')
    with open('output.txt', 'wb') as r:
        r.write(findDiff(book).encode())
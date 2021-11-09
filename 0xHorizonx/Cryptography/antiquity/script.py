#!/usr/bin/env python3

alphabet = "abcdefghijklmnopqrstuvwxyz"

FLAG_ENCRYPTED = "wymul aluncum uai ncvc kocu ch ijncgog yayn yluhn wog jluymylncg ihym xihyw aluncum uai ncvc kocu hih mwcly koug ux pyrcffog gusvy u jluywcjci pivcm: bilct0hr{liguh_yhwlsjncih_cm_yums_ni_lypylmy}"
recovered_flag = ""

def ceasar(s : str, offset : int):
    result = ""
    for letter in s:
        if letter in alphabet:
            # Get the index of letter in alphabet and add the offset (the modulus is for the case where adding the offset makes the index greater than the length of alphabet, allowing to switch z with a for example)
            result += alphabet[(alphabet.index(letter)+offset) % len(alphabet)] 
        else:
            result += letter
    return result

if __name__ == '__main__':
    for i in range(len(alphabet)):
        recovered_flag = ceasar(FLAG_ENCRYPTED, i)
        if "horiz0nx" in recovered_flag: 
            print(recovered_flag)

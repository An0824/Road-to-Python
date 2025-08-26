# 모음 찾기 함수

def count_vowels(text):
    new_text = text.lower()
    new = []
    for i in new_text:
        if i in "aeiou": 
            new.append(i)
        else: continue
    return len(new)
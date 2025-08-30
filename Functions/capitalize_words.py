# 대문자 함수

def capitalize_words(sentence):
    k = []
    for i in sentence.split():
        i = i.capitalize()
        k.append(i)
    return " ".join(k)

# --- 실행 코드 ---
text1 = "heLLo wORLd"
text2 = "python is FUN"

print(f"'{text1}' -> '{capitalize_words(text1)}'")
print(f"'{text2}' -> '{capitalize_words(text2)}'")


        



    
    

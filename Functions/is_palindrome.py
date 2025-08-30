# 회문 확인 함수

def is_palindrome(text):
    new_text = ""
    for i in text:
        if i.isalnum():
            new_text += i
    new_text = new_text.lower()
    if new_text == new_text[::-1]:
        return True
    else:
        return False


# --- 실행 코드 ---
print(f"'level' 은 회문인가? {is_palindrome('level')}")
print(f"'hello' 는 회문인가? {is_palindrome('hello')}")
print(f"'A man, a plan, a canal: Panama' 는 회문인가? {is_palindrome('A man, a plan, a canal: Panama')}")
print(f"'기러기' 는 회문인가? {is_palindrome('기러기')}")

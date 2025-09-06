# 딕셔너리 뒤집기 함수
def invert_dictionary(d):
    k = {}
    for new_value, new_key in d.items():
        k[new_key] = new_value
    return k
       

# --- 실행 코드 ---
original_dict1 = {'a': 1, 'b': 2, 'c': 3}
inverted_dict1 = invert_dictionary(original_dict1)
print(f"{original_dict1} -> {inverted_dict1}")

original_dict2 = {'a': 1, 'b': 2, 'c': 1} # value '1'이 중복됨
inverted_dict2 = invert_dictionary(original_dict2)
print(f"{original_dict2} -> {inverted_dict2}")

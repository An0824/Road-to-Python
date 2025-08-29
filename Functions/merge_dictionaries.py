# 딕셔너리 병합 함수

def merge_dictionaries(dict1, dict2):
    new_dictionary = {}
    for k, v in dict1.items():
        new_dictionary[k] = v
    for k, v in dict2.items():
        new_dictionary[k] = v

    return new_dictionary
        
    

# --- 실행 코드 ---
dict_a = {'a': 1, 'b': 2, 'c': 3}
dict_b = {'b': 20, 'd': 40}

merged = merge_dictionaries(dict_a, dict_b)
print("병합된 딕셔너리:", merged)
print("원본 딕셔너리 A:", dict_a)
print("원본 딕셔너리 B:", dict_b)


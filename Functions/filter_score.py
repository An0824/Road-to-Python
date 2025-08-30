def filter_students_by_score(students, min_score):
    new_list = []
    for i in students:
        if i["score"] >= min_score:
            new_list.append(i)
    return new_list


# --- 실행 코드 ---
student_data = [
    {'name': '김철수', 'score': 85},
    {'name': '이영희', 'score': 92},
    {'name': '박민준', 'score': 78},
    {'name': '최유리', 'score': 95}
]

high_scorers = filter_students_by_score(student_data, 90)
print(high_scorers)
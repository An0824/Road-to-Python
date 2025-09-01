# 공통 과목 찾기 함수

def find_common_courses(student1_courses, student2_courses):
    a = set(student1_courses)
    b = set(student2_courses)
    new_list = list(a & b)
    new_list.sort(key=str.lower)
    return new_list


# --- 실행 코드 ---
courses_a = ["Math", "English", "Science", "History"]
courses_b = ["Science", "Art", "English", "Music"]

common = find_common_courses(courses_a, courses_b)
print("공통 수강 과목:", common)
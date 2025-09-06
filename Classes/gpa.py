# 학점 관리 클래스

class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.courses = {}

    def add_course(self, course_name, grade):
        self.courses[course_name] = grade
        print(f"{course_name}이(가) 목록에 추가되었습니다.")

    def get_gpa(self):
        sum_gpa = 0
        if self.courses == {}:
            print("아직 수강한 과목이 없습니다.")
        else:
            for i in self.courses.values():
                sum_gpa += i
            mean_gpa = sum_gpa / len(self.courses.values())
            print("{0:.2f}".format(mean_gpa))
      

    def get_transcript(self):
        print(f"이름: {self.name}, 학번:{self.student_id}")
        for i, v in self.courses.items():
            print(f"과목: {i}, 학점: {v}")


# --- 실행 코드 ---
student = Student("드라간", "20250824")

# 과목 추가
student.add_course("객체지향프로그래밍", 4.0)
student.add_course("자료구조", 4.0)
student.add_course("한문기초", 3.5)
print("-" * 20)

# 성적표 및 GPA 확인
student.get_transcript()
print("-" * 20)
student.get_gpa()
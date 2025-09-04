# 블로그 포스트 클래스

class Post:
    def __init__(self, author, content):
        self.author = author
        self.content = content
        self.likes = 0
    
    def like(self):
        self.likes += 1

    def edit(self, new_content):
        self.content = new_content
        print("포스트의 내용이 수정되었습니다.")
    
    def display(self):
        print(f"작성자: {self.author}님")
        print(f"내용: {self.content}")
        print(f"좋아요: {self.likes}")


# --- 실행 코드 ---
my_post = Post("드라간", "오늘의 파이썬 공부 기록!")

# 초기 상태 출력
my_post.display()
print("-" * 20)

# 좋아요 누르기
my_post.like()
my_post.like()
my_post.like()

# 내용 수정
my_post.edit("오늘의 파이썬 클래스 문제 풀이 완료!")

# 최종 상태 출력
my_post.display()
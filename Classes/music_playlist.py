# 플레이리스트 클래스

class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
    
    def __str__(self):
        return f"{self.title} by {self.artist}"
    
class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []
    
    def add_song(self, song):
        self.songs.append(song)
        print(f"플레이리스트에 {song.title}이 추가되었습니다.")

    def remove_song(self, title):
        new_list = []
        for i in self.songs:
            new_list.append(i.title)
        if title in new_list:
            for k in self.songs:
                if k.title == title:
                    self.songs.remove(k)
                    print(f"플레이리스트에서 {k.title}이 삭제되었습니다.")
        else:
            print(f"플레이리스트에서 {title}을 찾을 수 없습니다.")
    
    def play_all(self):
        print(f"--- 재생 목록: {self.name} ---")
        for i in self.songs:
            print(i)


# --- 실행 코드 ---
# 1. 노래 객체 생성
song1 = Song("Bohemian Rhapsody", "Queen")
song2 = Song("Imagine", "John Lennon")
song3 = Song("Stairway to Heaven", "Led Zeppelin")

# 2. 플레이리스트 생성 및 노래 추가
my_playlist = Playlist("나의 최애 팝송")
my_playlist.add_song(song1)
my_playlist.add_song(song2)
my_playlist.add_song(song3)
print("-" * 20)

# 3. 전체 재생
my_playlist.play_all()
print("-" * 20)

# 4. 노래 삭제
my_playlist.remove_song("Imagine")
my_playlist.remove_song("Hotel California") # 없는 노래
print("-" * 20)

# 5. 최종 재생
my_playlist.play_all()



            
            
       
            
         
            


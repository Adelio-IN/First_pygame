import tkinter as tk
import random
from tkinter import messagebox

class ShootingGame:
    def __init__(self):
        #게임을 표시할 윈도우 생성 / 제목 표시
        self.window = tk.Tk()
        self.window.title("Shooting Game")
        # 게임이 실행되는 영역(배경화면) 생성
        self.width = 400
        self.height = 600
        self.canvas = tk.Canvas(
            master=self.window,  # 부모 객체 이름
            width=self.width,    # 캔버스 가로 크기(픽셀)
            height=self.height,  # 캔버스 세로 크기(픽셀)
            bg="black"           # 배경색
        )
        self.canvas.pack()

        # 플레이어 생성
        self.player = self.canvas.create_rectangle(180, 580, 220, 660, fill = "blue")
        self.bullets = [] # 총알을 담아 놓을 리스트
        self.enemies = [] # 적을 담아 놓을 리스트
        self.score = 1 # 적을 맞췄을 때 점수
        self.failures = 0 # 적을 놓친 횟수
        self.collisions = 0 #적과 충돌한 횟수
        self.running = False # 상태 관리 변수

        # 키보드에서 화살표 키를 눌렀을 때 작동할 함수 등록
        self.window.bind("<Left>", self.move_left)
        self.window.bind("<Right>", self.move_right)
        self.window.bind("<space>", self.shoot)

        self.start_button = tk.Button(
            self.window,
            text="Start",
            command=self.start_game
        )
        self.start_button.pack(side=tk.LEFT)

        self.pause_button = tk.Button(
            self.window,
            text="Pause",
            command=self.pause_game
        )
        self.pause_button.pack(side=tk.LEFT)

        self.resume_button = tk.Button(
            self.window,
            text="Resume",
            command=self.resume_game)
        self.resume_button.pack(side=tk.LEFT)

        self.exit_button = tk.Button(
            self.window,
            text="Exit",
            command=self.exit_game
        )
        self.exit_button.pack(side=tk.LEFT) # 왼쪽 공간에 이어 붙이기

        # 게임이 window.mainloop() 실행되면 업데이트 함수 실행
        #  -> start_game() 실행되면 시작해야 되므로
        #   프로그램 동작과 동시에 게임 시작하는 기존 내용 삭제
        # self.update_game()

        def exit_game(self):
            self.running = False
            self.window.destroy()

        def start_game(self):
            if not self.running:
                self.running = True
                self.update_game()

        def pause_game(self):
            self.running = False

        def resume_game(self):
            if not self.running:
                self.running = True
                self.update_game()
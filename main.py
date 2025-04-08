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
        
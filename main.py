# アニメーションの基本
# 画像の連続表示と、pygame.time.wait()を使って、アニメーションを実装しよう

import pygame
from pygame.locals import *
import re  # 正規表現
import glob  # ファイル操作

pygame.init()

# 音楽ファイルのロード
pygame.mixer.init()
syoryuken_se = pygame.mixer.Sound("sound/syoryuken_se.wav")
hadouken_se = pygame.mixer.Sound("sound/hadouken_se.wav")

# 画像ファイルのロード：フォルダにあるファイルを一気にリストに入れる
syoryuken = glob.glob("syoryuken_img/*")
hadouken = glob.glob("hadouken-jpeg/*")
# 番号順に並べ替える（ソート）
syoryuken.sort(key=lambda s: int(re.search(r'\d+', s).group()))
hadouken.sort(key=lambda s: int(re.search(r'\d+', s).group()))
# 画像のロード（内包表記）
s_images = [pygame.image.load(i) for i in syoryuken]
h_images = [pygame.image.load(i) for i in hadouken]

screen = pygame.display.set_mode((300, 300))
screen.fill((255, 255, 255))
pygame.display.set_caption("昇龍拳")
counter = 0

# メインループ
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            screen.fill((255, 255, 255))
            if event.key == K_s:
                syoryuken_se.play()
                for i in s_images:
                    screen.fill((255, 255, 255))
                    screen.blit(s_images[counter], (0, screen.get_height() - s_images[counter].get_height()))
                    counter += 1
                    if counter == len(s_images):
                        counter = 0
                    pygame.display.update()
                    pygame.time.wait(50)
            elif event.key == K_h:
                hadouken_se.play()
                for i in h_images:
                    screen.blit(h_images[counter], (0, screen.get_height() - h_images[counter].get_height()))
                    counter += 1
                    if counter == len(h_images):
                        counter = 0
                    pygame.display.update()
                    pygame.time.wait(50)

    pygame.display.update()
pygame.quit()

# 問題①画像表示の部分で関数を使ってみよう

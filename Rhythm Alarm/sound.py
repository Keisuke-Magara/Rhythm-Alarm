from tkinter.constants import S
import pygame
def play_music(music_name):
    pygame.mixer.init()
    pygame.mixer.music.load(music_name)
    pygame.mixer.music.play(-1)
def stop_music():
    pygame.mixer.music.stop()
def play_se(se_name):
    pygame.mixer.init()
    se=pygame.mixer.Sound(se_name)
    se.play()
import os
from threading import Thread
import time
import pygame

total_time = 60 * 3 + 39
total_frames = 6574
duration = total_time / total_frames


def play_video():
    src_dir = './bad_apple_chars'
    frames = os.listdir(src_dir)
    frames.sort(key=lambda x: int(x.replace('.txt', '')))
    for frame in frames:
        with open(f'{src_dir}/{frame}', 'r') as f:
            content = f.read()
            print(content)
            time.sleep(duration)


def play_music():
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load('./bad_apple.mp3')
    pygame.mixer.music.play()
    time.sleep(240)
    pygame.mixer.music.fadeout(10000)


if __name__ == '__main__':
    t1 = Thread(target=play_music)
    t2 = Thread(target=play_video)
    t1.start()
    t2.start()

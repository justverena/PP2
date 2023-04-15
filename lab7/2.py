import pygame, os
pygame.init()
size = (640, 480)
color = (255, 255, 255)
screen = pygame.display.set_mode(size)
pygame.mixer.init()
playlist = ["chlorine.mp3", "shy_away.mp3"]
i = 0
pygame.mixer.music.load(playlist[i])
kplay_pause = pygame.K_SPACE
kquit = pygame.K_q
kstop = pygame.K_s
kprevious = pygame.K_LEFT
knext = pygame.K_RIGHT
pygame.mixer.music.play()
ok = True
while ok:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ok = False
        elif event.type == pygame.KEYDOWN:
            if event.key == kplay_pause:
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
            elif event.key == kstop:
                pygame.mixer.music.stop()
            elif event.key == knext:
                 i = (i + 1) % len(playlist)
                 pygame.mixer.music.load(playlist[i])
                 pygame.mixer.music.play()
            elif event.key == kprevious:
                 i = (i - 1) % len(playlist)
                 pygame.mixer.music.load(playlist[i])
                 pygame.mixer.music.play()
            elif event.key == kquit:
                pygame.quit()

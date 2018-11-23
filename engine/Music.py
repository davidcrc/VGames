import pygame

class Music:
    def __init__(self):
        self.playMe = pygame.mixer.music

    def PlayMusic(self, archivo):
        self.playMe.load(archivo)
        self.playMe.play(0)

if __name__ == '__main__':
    musica = Music()
    musica.PlayMusic('recursos/new_level.wav')
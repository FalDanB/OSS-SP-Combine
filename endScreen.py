#End Screen for Combine Game

import pygame

class EndScreen:
    def __init__(self):
        self.headlineText = "GAME OVER"
        self.restartText = "- Press SPACE to restart -"
        self.quitText = "- Press Q to quit -"

    def graphics(self, screen):
        pygame.font.init()
        fonts = pygame.font.get_fonts()

        #render Headline
        headlineFont = pygame.font.SysFont(fonts[2], 57, True, False)
        headlineShadow = headlineFont.render(self.headlineText, True,(0,0,0))
        headline = headlineFont.render(self.headlineText, True,(255,255,255))
        screen.blit(headlineShadow, (24,52))
        screen.blit(headline, (22,50))

        #render text for restarting
        restartTextFont = pygame.font.SysFont(fonts[2], 25, True, True)
        restartTextShadow = restartTextFont.render(self.restartText, True,(0,0,0))
        restartText = restartTextFont.render(self.restartText, True,(255,255,255))
        screen.blit(restartTextShadow, (44,202))
        screen.blit(restartText, (42,200))

        #render text for quitting
        quitTextFont = pygame.font.SysFont(fonts[2], 25, True, True)
        quitTextShadow = quitTextFont.render(self.quitText, True,(0,0,0))
        quitText = quitTextFont.render(self.quitText, True,(255,255,255))
        screen.blit(quitTextShadow, (74,252))
        screen.blit(quitText, (72, 250))

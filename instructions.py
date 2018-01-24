import pygame

class Instructions:
    def __init__(self):
        self.headlineText = "Combine"
        self.textLines = ["...at least three balls of the same",
                          "colour to make them disappear",
                          "and produce a ball of the colour of",
                          "the next higher level and to earn",
                          "points. In the beginning only two",
                          "colours are unlocked for dropping.",
                          "When balls of one colour are",
                          "combined, that colour will become",
                          "unlocked. This will make the game",
                          "more difficult but also earn you",
                          "more points. The game ends when",
                          "when stack goes over the read line."]
        self.startText = "- PRESS SPACE TO START -"

    def graphics(self, screen):
        pygame.font.init()
        fonts = pygame.font.get_fonts()
        headlineFont = pygame.font.SysFont(fonts[2], 80, True, False)
        headlineShadow = headlineFont.render(self.headlineText, True,(0,0,0))
        headline = headlineFont.render(self.headlineText, True,(255,255,255))
        screen.blit(headlineShadow, (24,52))
        screen.blit(headline, (22,50))
        textFont = pygame.font.SysFont(fonts[2], 20, True, False)
        for i in range(0,len(self.textLines)):
            textLineShadow = textFont.render(self.textLines[i], True, (0,0,0))
            textLine = textFont.render(self.textLines[i], True, (255,255,255))
            screen.blit(textLineShadow, (24, 152+i*20))
            screen.blit(textLine, (22, 150+i*20))
        startTextFont = pygame.font.SysFont(fonts[2], 27, True, True)
        startTextShadow = startTextFont.render(self.startText, True,(0,0,0))
        startText = startTextFont.render(self.startText, True,(255,255,255))
        screen.blit(startTextShadow, (30, 412))
        screen.blit(startText, (28,410))

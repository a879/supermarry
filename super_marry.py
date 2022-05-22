import pygame
import sys
from settings import Settings, BgTheme

class SuperMarry:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Super Marry")

        self.settings = Settings()
        self.bgTheme = BgTheme()

        # 设置屏幕宽高， 背景色， 获取 屏幕rect
        self.screen_shape = pygame.display.set_mode((self.settings.screenWidth, self.settings.screenHeight))

        self.screen_rect = self.screen_shape.get_rect()

        self.img = pygame.image.load('./images/1-1.png')
        self.img_rect = self.img.get_rect()

        self.img_rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        self.screen_shape.blit(self.img, self.img_rect)

    # 执行循环
    def game_run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen_shape.fill(self.bgTheme.bgColor)
            self.blitme()
            pygame.display.flip()


if __name__  == '__main__':
    ai = SuperMarry()
    ai.game_run()
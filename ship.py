import pygame;


class Ship():
    def __init__(self, screen, ai_settings):
        """初始化飞船并设置初始位置"""
        self.screen = screen
        # 加载飞船图像病获取七外接矩形
        self.image = pygame.image.load('image/my.png').convert_alpha()
        # self.image = pygame.transform.smoothscale(self.image, (50, 50))  # 缩小图片
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # 将每艘飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.move_left = False
        self.move_right = False
        self.fire = False
        self.fire_gap = ai_settings.bullet_fire_gap
        self.fire_ticks = 0

    def update(self, time_passed):
        if self.move_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += time_passed * 1
        elif self.move_left and self.rect.left > 0:
            self.rect.centerx -= time_passed * 1

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)

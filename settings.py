class Settings():
    def __init__(self):
        """初始化游戏设置"""
        self.screen_width = 422
        self.screen_height = 750
        self.bg_color = (255, 255, 255)

        # self.bullet_width = 3
        # self.bullet_height = 7
        # self.bullet_color = (60, 60, 60)
        self.bullet_speed_factor = 0.5  # 子弹速度
        self.bullet_fire_gap = 100  # 子弹间隔

        # self.enemy_speed_factor = 0.5  # 敌机下落速度
        self.enemy_spacing = 100  # 敌机垂直间距
        self.enemy_speed_factor = 0.4  # 敌机下落速度
        self.enemy_bullet_speed = 1  # 敌机子弹速度
        self.top_bar = 10

    def initialize_game_setting(self):
        self.bullet_speed_factor = 1
        self.enemy_speed_factor = 0.5

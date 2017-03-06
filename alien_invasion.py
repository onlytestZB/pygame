import sys
import pygame
from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf
from pygame.sprite import Group


def run_game():
    # 初始化游戏
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    # 创建飞船
    ship = Ship(ai_settings, screen)
    # 存储子弹状态
    bullets = Group()
    # 创建一个外星人编组
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)
    # 主循环
    while True:
        # 监视
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
        gf.update_aliens(ai_settings, aliens)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)

run_game()

import sys
import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
#from alien import Alien   #不直接创建机器人，因此不需要导入Alien类
import game_function as gf
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


def run_game():
	#初始化游戏并创建一个屏幕对象
	pygame.init()#初始化背景设置
	ai_settings = Settings()

	screen = pygame.display.set_mode(
		(ai_settings.screen_width, ai_settings.screen_height)
	)#创建名为screen的显示窗口，指定游戏窗口的尺寸
	pygame.display.set_caption("Alien Invasion")

	#创建Play按钮
	play_button = Button(ai_settings, screen, "Play")

	#创建一个用于存储游戏统计信息的实例
	stats = GameStats(ai_settings)
	
	#创建一艘飞船，一个子弹编组和一个外星人编组	
	ship = Ship(ai_settings, screen)
	bullets = Group()
	aliens = Group()

	#创建外星人群
	gf.create_fleet(ai_settings, screen, ship, aliens)

	#创建存储游戏统计信息的实例，并创建记分牌
	sb = Scoreboard(ai_settings,screen, stats)

	#开始游戏的主循环，包含事件循环以及管理屏幕更新的代码
	while True:
		#监视键盘和鼠标事件
		gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
		
		if stats.game_active == True:
			ship.update()
			gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
			gf.update_aliens(ai_settings, stats, sb, screen, ship, aliens, bullets)
		
		gf.update_screen(ai_settings, stats, screen, sb, ship, aliens, bullets, play_button)
		
 
run_game()

 
# 匯入 pygame
import pygame

# 設定視窗大小
WIN_width = 800
WIN_height = 600
# 設定圖像大小
image_background_width = 800
image_background_height = 550
image_enemy_width = 50
image_enemy_height = 50
image_pause_width = 60
image_pause_height = 60
image_continue_width = 50
image_continue_height = 50
image_sound_width = 50
image_sound_height = 50
image_muse_width = 50
image_muse_height = 50
image_hp_width = 35
image_hp_height = 35
image_hpgray_width = 35
image_hpgray_height = 35
# 設定顏色
color_white = (255, 255, 255)
color_black = (0, 0, 0)
color_red = (255, 0, 0)

# 匯入圖像、改變圖像大小
image_background = pygame.image.load('C://Users//user//PycharmProjects//pythongame//images//Map.png')
image_background = pygame.transform.scale(image_background, (image_background_width, image_background_height))
image_enemy = pygame.image.load('C://Users//user//PycharmProjects//pythongame//images//enemy.png')
image_enemy = pygame.transform.scale(image_enemy, (image_enemy_width, image_enemy_height))
image_pause = pygame.image.load('C://Users//user//PycharmProjects//pythongame//images//pause.png')
image_pause = pygame.transform.scale(image_pause, (image_pause_width, image_pause_height))
image_continue = pygame.image.load('C://Users//user//PycharmProjects//pythongame//images//continue.png')
image_continue = pygame.transform.scale(image_continue, (image_continue_width, image_continue_height))
image_sound = pygame.image.load('C://Users//user//PycharmProjects//pythongame//images//sound.png')
image_sound = pygame.transform.scale(image_sound, (image_sound_width, image_sound_height))
image_muse = pygame.image.load('C://Users//user//PycharmProjects//pythongame//images//muse.png')
image_muse = pygame.transform.scale(image_muse, (image_muse_width, image_muse_height))
image_hp = pygame.image.load('C://Users//user//PycharmProjects//pythongame//images//hp.png')
image_hp = pygame.transform.scale(image_hp, (image_hp_width, image_hp_height))
image_hpgray = pygame.image.load('C://Users//user//PycharmProjects//pythongame//images//hp_gray.png')
image_hpgray = pygame.transform.scale(image_hpgray, (image_hpgray_width, image_hpgray_height))

# 初始化
pygame.init()
window = pygame.display.set_mode((WIN_width, WIN_height))   # 視窗初始化
pygame.display.set_caption("My first game")     # 將 「 My first game」顯示在視窗上
start_time = pygame.time.get_ticks()    # 令 start_time 為系統時間
font = pygame.font.SysFont("fangsong", 20)    # 設定 font 的字型和字體大小

run = True
#   當 run 為真時，遊戲運行
while run:
    end_time = pygame.time.get_ticks()  # 令 end_time 為系統時間
    # 計算時間
    time = (end_time - start_time) // 1000
    sec = time % 60
    min = time // 60
    # 繪製遊戲背景
    window.fill(color_black)
    window.blit(image_background, (0, 100))
    # 繪製遊戲功能鍵
    window.blit(image_pause, (740, 17))
    window.blit(image_continue, (690, 19))
    window.blit(image_sound, (630, 21))
    window.blit(image_muse, (570, 21))
    # 繪製玩家生命值
    i = 0
    hp_x = 300
    while i < 5:
        window.blit(image_hp, (hp_x + i * 40, 15))  # 從 (570, 14) 繪製 image_muse 圖像在視窗上
        window.blit(image_hp, (hp_x + i * 40, 45))  # 從 (570, 14) 繪製 image_muse 圖像在視窗上
        i += 1
    i = 0
    hpgray_x = 380
    while i < 3:
        window.blit(image_hpgray, (hpgray_x + i * 40, 45))  # 從 (570, 14) 繪製 image_muse 圖像在視窗上
        i += 1
    # 繪製敵人及血條
    pygame.draw.rect(window, color_black, [0, 560, 80, 40])
    window.blit(image_enemy, (20, 320))
    pygame.draw.rect(window, color_red, [20, 310, 50, 5])
    # 顯示時間
    text_surface = font.render(str(min), True, color_white)
    window.blit(text_surface, (20, 573))
    text_surface = font.render(":", True, color_white)
    window.blit(text_surface, (30, 570))
    text_surface = font.render(str(sec), True, color_white)
    window.blit(text_surface, (40, 573))
    # 當按下右上角的叉號鍵結束遊戲
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()  # 將更新的內容顯示到視窗上

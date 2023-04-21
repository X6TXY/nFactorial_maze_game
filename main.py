import pygame
from maze_generator import *

RES = WIDTH, HEIGHT = 700, 500
TILE = 50
cols, rows = WIDTH // TILE, HEIGHT // TILE


time =60

icon = pygame.image.load('images/icon.png')
pygame.display.set_icon(icon)
pygame.display.set_caption('Maze game')
#music

def get_record():

    try:
        with open('record') as f:
            return f.readline()
    except FileNotFoundError:
        with open('record', 'w') as f:
            f.write('0')
            return 0

record =get_record()
def function(TILE):
        game_play = pygame.mixer.music.load('music/intro.mp3')
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.1)
        score = 0
        time = 60
        class Food:
            def __init__(self):
                self.img = pygame.image.load('images/food.png').convert_alpha()
                self.img = pygame.transform.scale(self.img, (TILE - 10, TILE - 10))
                self.rect = self.img.get_rect()
                self.set_pos()

            def set_pos(self):
                self.rect.topleft = randrange(cols) * TILE + 5, randrange(rows) * TILE + 5

            def draw(self):
                game_surface.blit(self.img, self.rect)


        def is_collide(x, y):
            tmp_rect = player_rect.move(x, y)
            if tmp_rect.collidelist(walls_collide_list) == -1:
                return False
            return True


        def eat_food():
            for food in food_list:
                if player_rect.collidepoint(food.rect.center):
                    food.set_pos()
                    return True
            return False


        def is_game_over():
            global time, score, record, FPS
            if time < 0:
                pygame.time.wait(700)
                player_rect.center = TILE // 2, TILE // 2
                [food.set_pos() for food in food_list]
                set_record(record, score)
                record = get_record()
                time, score, FPS = 60, 0, 60


        def get_record():
            try:
                with open('record') as f:
                    return f.readline()
            except FileNotFoundError:
                with open('record', 'w') as f:
                    f.write('0')
                    return 0


        def set_record(record, score):
            rec = max(int(record), score)
            with open('record', 'w') as f:
                f.write(str(rec))


        FPS = 60
        pygame.init()
        game_surface = pygame.Surface(RES)
        surface = pygame.display.set_mode((WIDTH + 300, HEIGHT))
        clock = pygame.time.Clock()

        # images
        bg_game = pygame.image.load('images/bg_1.jpeg').convert()
        bg = pygame.image.load('images/bg_main.png').convert()

        # get maze
        maze = generate_maze()

        # player settings
        player_speed = 5
        player_img = pygame.image.load('images/player2.png').convert_alpha()
        player_img = pygame.transform.scale(player_img, (TILE - 2 * maze[0].thickness, TILE - 2 * maze[0].thickness))
        player_rect = player_img.get_rect()
        player_rect.center = TILE // 2, TILE // 2
        directions = {'a': (-player_speed, 0), 'd': (player_speed, 0), 'w': (0, -player_speed), 's': (0, player_speed)}
        keys = {'a': pygame.K_LEFT, 'd': pygame.K_RIGHT, 'w': pygame.K_UP, 's': pygame.K_DOWN}
        direction = (0, 0)

        # food settings
        food_list = [Food() for i in range(1)]

        # collision list
        walls_collide_list = sum([cell.get_rects() for cell in maze], [])

        # timer, score, record
        pygame.time.set_timer(pygame.USEREVENT, 1000)
        
        record = get_record()

        # fonts
        font = pygame.font.SysFont('Impact', 50)
        text_font = pygame.font.SysFont('Impact', 40)

        while True:
            surface.blit(bg, (WIDTH, 0))
            surface.blit(game_surface, (0, 0))
            game_surface.blit(bg_game, (0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.USEREVENT:
                    time -= 1
                if time ==0:
                    game_over()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        exit()
                    if event.key == pygame.K_m:
                        welcome()
                

            # controls and movement
            pressed_key = pygame.key.get_pressed()
            for key, key_value in keys.items():
                if pressed_key[key_value] and not is_collide(*directions[key]):
                    direction = directions[key]
                    break
            if not is_collide(*direction):
                player_rect.move_ip(direction)

            # draw maze
            [cell.draw(game_surface) for cell in maze]

            # gameplay
            if eat_food():
                FPS += 10
                score += 1
            is_game_over()

            # draw player
            game_surface.blit(player_img, player_rect)

            # draw food
            [food.draw() for food in food_list]

            # draw stats
            surface.blit(text_font.render('TIME:', True, pygame.Color('cyan'), True), (WIDTH + 70, 75))
            surface.blit(font.render(f'{time}', True, pygame.Color('cyan')), (WIDTH + 70, 120))
            surface.blit(text_font.render('score:', True, pygame.Color('forestgreen'), True), (WIDTH + 50, 200))
            surface.blit(font.render(f'{score}', True, pygame.Color('forestgreen')), (WIDTH + 70, 240))
            surface.blit(text_font.render('record:', True, pygame.Color('magenta'), True), (WIDTH + 30, 300))
            surface.blit(font.render(f'{record}', True, pygame.Color('magenta')), (WIDTH + 70, 340))

            # print(clock.get_fps())
            pygame.display.flip()
            clock.tick(FPS)
def function(TILE):
        game_play = pygame.mixer.music.load('music/intro.mp3')
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.1)
        score = 0
        time = 60
        class Food:
            def __init__(self):
                self.img = pygame.image.load('images/food.png').convert_alpha()
                self.img = pygame.transform.scale(self.img, (TILE - 10, TILE - 10))
                self.rect = self.img.get_rect()
                self.set_pos()

            def set_pos(self):
                self.rect.topleft = randrange(cols) * TILE + 5, randrange(rows) * TILE + 5

            def draw(self):
                game_surface.blit(self.img, self.rect)


        def is_collide(x, y):
            tmp_rect = player_rect.move(x, y)
            if tmp_rect.collidelist(walls_collide_list) == -1:
                return False
            return True


        def eat_food():
            for food in food_list:
                if player_rect.collidepoint(food.rect.center):
                    food.set_pos()
                    return True
            return False


        def is_game_over():
            global time, score, record, FPS
            if time < 0:
                pygame.time.wait(700)
                player_rect.center = TILE // 2, TILE // 2
                [food.set_pos() for food in food_list]
                set_record(record, score)
                record = get_record()
                time, score, FPS = 60, 0, 60


        def get_record():
            try:
                with open('record') as f:
                    return f.readline()
            except FileNotFoundError:
                with open('record', 'w') as f:
                    f.write('0')
                    return 0


        def set_record(record, score):
            rec = max(int(record), score)
            with open('record', 'w') as f:
                f.write(str(rec))


        FPS = 60
        pygame.init()
        game_surface = pygame.Surface(RES)
        surface = pygame.display.set_mode((WIDTH + 300, HEIGHT))
        clock = pygame.time.Clock()

        # images
        bg_game = pygame.image.load('images/bg_1.jpeg').convert()
        bg = pygame.image.load('images/bg_main.png').convert()

        # get maze
        maze = generate_maze()

        # player settings
        player_speed = 5
        player_img = pygame.image.load('images/player2.png').convert_alpha()
        player_img = pygame.transform.scale(player_img, (TILE - 2 * maze[0].thickness, TILE - 2 * maze[0].thickness))
        player_rect = player_img.get_rect()
        player_rect.center = TILE // 2, TILE // 2
        directions = {'a': (-player_speed, 0), 'd': (player_speed, 0), 'w': (0, -player_speed), 's': (0, player_speed)}
        keys = {'a': pygame.K_LEFT, 'd': pygame.K_RIGHT, 'w': pygame.K_UP, 's': pygame.K_DOWN}
        direction = (0, 0)

        # food settings
        food_list = [Food() for i in range(1)]

        # collision list
        walls_collide_list = sum([cell.get_rects() for cell in maze], [])

        # timer, score, record
        pygame.time.set_timer(pygame.USEREVENT, 1000)
        
        record = get_record()

        # fonts
        font = pygame.font.SysFont('Impact', 50)
        text_font = pygame.font.SysFont('Impact', 40)

        while True:
            surface.blit(bg, (WIDTH, 0))
            surface.blit(game_surface, (0, 0))
            game_surface.blit(bg_game, (0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.USEREVENT:
                    time -= 1
                if time ==0:
                    game_over()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        exit()
                    if event.key == pygame.K_m:
                        welcome()
                

            # controls and movement
            pressed_key = pygame.key.get_pressed()
            for key, key_value in keys.items():
                if pressed_key[key_value] and not is_collide(*directions[key]):
                    direction = directions[key]
                    break
            if not is_collide(*direction):
                player_rect.move_ip(direction)

            # draw maze
            [cell.draw(game_surface) for cell in maze]

            # gameplay
            if eat_food():
                FPS += 10
                score += 1
            is_game_over()

            # draw player
            game_surface.blit(player_img, player_rect)

            # draw food
            [food.draw() for food in food_list]

            # draw stats
            surface.blit(text_font.render('TIME:', True, pygame.Color('cyan'), True), (WIDTH + 70, 75))
            surface.blit(font.render(f'{time}', True, pygame.Color('cyan')), (WIDTH + 70, 120))
            surface.blit(text_font.render('score:', True, pygame.Color('forestgreen'), True), (WIDTH + 50, 200))
            surface.blit(font.render(f'{score}', True, pygame.Color('forestgreen')), (WIDTH + 70, 240))
            surface.blit(text_font.render('record:', True, pygame.Color('magenta'), True), (WIDTH + 30, 300))
            surface.blit(font.render(f'{record}', True, pygame.Color('magenta')), (WIDTH + 70, 340))

            # print(clock.get_fps())
            pygame.display.flip()
            clock.tick(FPS)

FPS = 60
pygame.init()
game_surface = pygame.Surface(RES)
surface = pygame.display.set_mode((WIDTH + 300, HEIGHT))
clock = pygame.time.Clock()

# images
bg_game = pygame.image.load('images/bg_1.jpeg').convert()
bg = pygame.image.load('images/bg_main.png').convert()
bg_intro = pygame.image.load('images/intro.jpeg')


# get maze
maze = generate_maze()

# player settings
player_speed = 5
player_img = pygame.image.load('images/player2.png').convert_alpha()
player_img = pygame.transform.scale(player_img, (TILE - 2 * maze[0].thickness, TILE - 2 * maze[0].thickness))
player_rect = player_img.get_rect()
player_rect.center = TILE // 2, TILE // 2
directions = {'a': (-player_speed, 0), 'd': (player_speed, 0), 'w': (0, -player_speed), 's': (0, player_speed)}
keys = {'a': pygame.K_LEFT, 'd': pygame.K_RIGHT, 'w': pygame.K_UP, 's': pygame.K_DOWN}
direction = (0, 0)

# food settings


# collision list
walls_collide_list = sum([cell.get_rects() for cell in maze], [])

# timer, score, record
pygame.time.set_timer(pygame.USEREVENT, 1000)

# fonts
font = pygame.font.SysFont('Impact', 50)
text_font = pygame.font.SysFont('Impact', 40)
text_font_help = pygame.font.SysFont('Impact', 10)




def welcome():
    exit_game = False
    music_welcome = pygame.mixer.music.load('music/cat.mp3')
    pygame.mixer.music.play(-1)
    while not exit_game:
        surface.blit(bg_intro,(0,0))
        surface.blit(text_font.render('Press "1"-hard ,"2"-medium or "3"-easy to play', False, pygame.Color('white'),True), (130,350))
        surface.blit(text_font.render('Record:', True, pygame.Color('magenta')), (400, 400))
        surface.blit(font.render(f'{record}', True, pygame.Color('magenta')), (540, 395))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_2:
                    function(40)
                if event.key == pygame.K_3:
                    function(50)
                if event.key == pygame.K_1:
                    function(30)

        pygame.display.update()
        clock.tick(FPS)

def game_over():
    exit_game = False
    while not exit_game:
        surface.fill(pygame.Color('white'))
        surface.blit(text_font.render('Press "M" for main menu ', False, pygame.Color('white'), False), (WIDTH//2, HEIGHT//2+60))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                    welcome()

        
        pygame.display.update()
        clock.tick(FPS)



welcome()
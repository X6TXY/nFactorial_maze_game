import pygame
from random import randrange,choice

RES = WIDTH, HEIGHT = 700, 500

FPS = 60
time = 60

game_surface = pygame.Surface(RES)
surface = pygame.display.set_mode((WIDTH + 300, HEIGHT))
clock = pygame.time.Clock()

# timer, score, record
pygame.time.set_timer(pygame.USEREVENT, 1000)

# images
bg_game = pygame.image.load('bg_1.jpeg').convert()
bg = pygame.image.load('bg_main.png').convert()
bg_intro = pygame.image.load('intro.jpeg')
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)
pygame.display.set_caption('Maze game')
pygame.init()

#getting record functions
def get_med_1():
    try:
        with open('record_2_1') as f:
            return f.readline()
    except FileNotFoundError:
        with open('record_2_1', 'w') as f:
            f.write('0')
            return 0
            rec = max(int(record), score)
            with open('record_2_1', 'w') as f:
                f.write(str(rec))
def get_med_2():
    try:
        with open('record_2_2') as f:
            return f.readline()
    except FileNotFoundError:
        with open('record_2_2', 'w') as f:
            f.write('0')
            return 0
            rec = max(int(record), score)
            with open('record_2_2', 'w') as f:
                f.write(str(rec))
def get_med_3():
    try:
        with open('record_2_3') as f:
            return f.readline()
    except FileNotFoundError:
        with open('record_2_3', 'w') as f:
            f.write('0')
            return 0
            rec = max(int(record), score)
            with open('record_2_3', 'w') as f:
                f.write(str(rec))
def get_easy_1():
    try:
        with open('record_3_1') as f:
            return f.readline()
    except FileNotFoundError:
        with open('record_3_1', 'w') as f:
            f.write('0')
            return 0
            rec = max(int(record), score)
            with open('record_3_1', 'w') as f:
                f.write(str(rec))
def get_easy_2():
    try:
        with open('record_3_2') as f:
            return f.readline()
    except FileNotFoundError:
        with open('record_3_2', 'w') as f:
            f.write('0')
            return 0
            rec = max(int(record), score)
            with open('record_3_2', 'w') as f:
                f.write(str(rec))
def get_easy_3():
    try:
        with open('record_3_3') as f:
            return f.readline()
    except FileNotFoundError:
        with open('record_3_3', 'w') as f:
            f.write('0')
            return 0
            rec = max(int(record), score)
            with open('record_3_3', 'w') as f:
                f.write(str(rec))
def get_hard_1():

    try:
        with open('record_1_1') as f:
            return f.readline()
    except FileNotFoundError:
        with open('record_1_1', 'w') as f:
            f.write('0')
            return 0
            rec = max(int(record), score)
            with open('record_1_1', 'w') as f:
                f.write(str(rec))
def get_hard_2():

    try:
        with open('record_1_2') as f:
            return f.readline()
    except FileNotFoundError:
        with open('record_1_2', 'w') as f:
            f.write('0')
            return 0
            rec = max(int(record), score)
            with open('record_1_2', 'w') as f:
                f.write(str(rec))
def get_hard_3():

    try:
        with open('record_1_3') as f:
            return f.readline()
    except FileNotFoundError:
        with open('record_1_3', 'w') as f:
            f.write('0')
            return 0
            rec = max(int(record), score)
            with open('record_1_3', 'w') as f:
                f.write(str(rec))

# fonts
font = pygame.font.SysFont('Impact', 50)
text_font = pygame.font.SysFont('Impact', 40)
text_font_1 = pygame.font.SysFont('Impact', 35)
text_gm = pygame.font.SysFont('Verdana',100)


#easy levels
def easy_1(TILE,time):
    pygame.display.set_caption('Easy level 1')
    RES = WIDTH, HEIGHT = 700, 500
    cols, rows = WIDTH // TILE, HEIGHT // TILE
    
    game_surface = pygame.Surface(RES)
    surface = pygame.display.set_mode((WIDTH + 300, HEIGHT))
    clock = pygame.time.Clock()
    # images
    bg_game = pygame.image.load('bg_1.jpeg').convert()
    bg = pygame.image.load('bg_main.png').convert()
    bg_intro = pygame.image.load('intro.jpeg')
    icon = pygame.image.load('icon.png')
    pygame.display.set_icon(icon)
    pygame.init()
    class Cell:
        def __init__(self, x, y):
            self.x, self.y = x, y
            self.walls = {'top': True, 'right': True, 'bottom': True, 'left': True}
            self.visited = False
            self.thickness = 4
        def draw(self, sc):
            x, y = self.x * TILE, self.y * TILE
            if self.walls['top']:
                pygame.draw.line(sc, pygame.Color('darkorange'), (x, y), (x + TILE, y), self.thickness)
            if self.walls['right']:
                pygame.draw.line(sc, pygame.Color('darkorange'), (x + TILE, y), (x + TILE, y + TILE), self.thickness)
            if self.walls['bottom']:
                pygame.draw.line(sc, pygame.Color('darkorange'), (x + TILE, y + TILE), (x , y + TILE), self.thickness)
            if self.walls['left']:
                pygame.draw.line(sc, pygame.Color('darkorange'), (x, y + TILE), (x, y), self.thickness)
        def get_rects(self):
            rects = []
            x, y = self.x * TILE, self.y * TILE
            if self.walls['top']:
                rects.append(pygame.Rect( (x, y), (TILE, self.thickness) ))
            if self.walls['right']:
                rects.append(pygame.Rect( (x + TILE, y), (self.thickness, TILE) ))
            if self.walls['bottom']:
                rects.append(pygame.Rect( (x, y + TILE), (TILE , self.thickness) ))
            if self.walls['left']:
                rects.append(pygame.Rect( (x, y), (self.thickness, TILE) ))
            return rects
        def check_cell(self, x, y):
            find_index = lambda x, y: x + y * cols
            if x < 0 or x > cols - 1 or y < 0 or y > rows - 1:
                return False
            return self.grid_cells[find_index(x, y)]
        def check_neighbors(self, grid_cells):
            self.grid_cells = grid_cells
            neighbors = []
            top = self.check_cell(self.x, self.y - 1)
            right = self.check_cell(self.x + 1, self.y)
            bottom = self.check_cell(self.x, self.y + 1)
            left = self.check_cell(self.x - 1, self.y)
            if top and not top.visited:
                neighbors.append(top)
            if right and not right.visited:
                neighbors.append(right)
            if bottom and not bottom.visited:
                neighbors.append(bottom)
            if left and not left.visited:
                neighbors.append(left)
            return choice(neighbors) if neighbors else False
    def remove_walls(current, next):
        dx = current.x - next.x
        if dx == 1:
            current.walls['left'] = False
            next.walls['right'] = False
        elif dx == -1:
            current.walls['right'] = False
            next.walls['left'] = False
        dy = current.y - next.y
        if dy == 1:
            current.walls['top'] = False
            next.walls['bottom'] = False
        elif dy == -1:
            current.walls['bottom'] = False
            next.walls['top'] = False
    def generate_maze():
        grid_cells = [Cell(col, row) for row in range(rows) for col in range(cols)]
        current_cell = grid_cells[0]
        array = []
        break_count = 1
        while break_count != len(grid_cells):
            current_cell.visited = True
            next_cell = current_cell.check_neighbors(grid_cells)
            if next_cell:
                next_cell.visited = True
                break_count += 1
                array.append(current_cell)
                remove_walls(current_cell, next_cell)
                current_cell = next_cell
            elif array:
                current_cell = array.pop()
        return grid_cells
    
    game_play = pygame.mixer.music.load('intro.mp3')
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.1)
    score = 0
    class Food:
        def __init__(self):
            self.img = pygame.image.load('food.png').convert_alpha()
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
            set_record(record, time)
            record = get_easy_1()
            
    def get_med_1():
        try:
            with open('record_3_1') as f:
                return f.readline()
        except FileNotFoundError:
            with open('record_3_1', 'w') as f:
                f.write('0')
                return 0
    def set_record(record, score):
        rec = max(int(record), score)
        with open('record_3_1', 'w') as f:
            f.write(str(rec))
    FPS = 60
    

    # get maze
    maze = generate_maze()
    # player settings
    player_speed = 5
    player_img = pygame.image.load('player2.png').convert_alpha()
    player_img = pygame.transform.scale(player_img, (TILE - 2 * maze[0].thickness, TILE - 2 * maze[0].thickness))
    player_rect = player_img.get_rect()
    player_rect.center = TILE // 2, TILE // 2
    directions = {'a': (-player_speed, 0), 'd': (player_speed, 0), 'w': (0, -player_speed), 's': (0, player_speed)}
    keys = {'a': pygame.K_LEFT, 'd': pygame.K_RIGHT, 'w': pygame.K_UP, 's': pygame.K_DOWN }
    direction = (0, 0)
    # food settings
    food_list = [Food() for i in range(1)]
    # collision list
    walls_collide_list = sum([cell.get_rects() for cell in maze], [])
    # timer, score, record
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    
    record = get_easy_1()
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
            if score == 1:
                set_record(record,time)
                if time >int(record):
                    print("New record")
                easy_2()
            if time == 0:
                set_record(record,time)
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
        surface.blit(text_font.render('record:', True, pygame.Color('magenta'), True), (WIDTH + 70, 300))
        surface.blit(font.render(f'{record}', True, pygame.Color('magenta')), (WIDTH + 70, 340))
        # print(clock.get_fps())
        pygame.display.flip()
        clock.tick(FPS)

def easy_2():
    TILE = 100
    time = 20
    pygame.display.set_caption('Easy level 2')
    RES = WIDTH, HEIGHT = 700, 500
    cols, rows = WIDTH // TILE, HEIGHT // TILE
    
    game_surface = pygame.Surface(RES)
    surface = pygame.display.set_mode((WIDTH + 300, HEIGHT))
    clock = pygame.time.Clock()
    # images
    bg_game = pygame.image.load('bg_1.jpeg').convert()
    bg = pygame.image.load('bg_main.png').convert()
    bg_intro = pygame.image.load('intro.jpeg')
    icon = pygame.image.load('icon.png')
    pygame.display.set_icon(icon)
    pygame.init()
    class Cell:
        def __init__(self, x, y):
            self.x, self.y = x, y
            self.walls = {'top': True, 'right': True, 'bottom': True, 'left': True}
            self.visited = False
            self.thickness = 4
        def draw(self, sc):
            x, y = self.x * TILE, self.y * TILE
            if self.walls['top']:
                pygame.draw.line(sc, pygame.Color('darkorange'), (x, y), (x + TILE, y), self.thickness)
            if self.walls['right']:
                pygame.draw.line(sc, pygame.Color('darkorange'), (x + TILE, y), (x + TILE, y + TILE), self.thickness)
            if self.walls['bottom']:
                pygame.draw.line(sc, pygame.Color('darkorange'), (x + TILE, y + TILE), (x , y + TILE), self.thickness)
            if self.walls['left']:
                pygame.draw.line(sc, pygame.Color('darkorange'), (x, y + TILE), (x, y), self.thickness)
        def get_rects(self):
            rects = []
            x, y = self.x * TILE, self.y * TILE
            if self.walls['top']:
                rects.append(pygame.Rect( (x, y), (TILE, self.thickness) ))
            if self.walls['right']:
                rects.append(pygame.Rect( (x + TILE, y), (self.thickness, TILE) ))
            if self.walls['bottom']:
                rects.append(pygame.Rect( (x, y + TILE), (TILE , self.thickness) ))
            if self.walls['left']:
                rects.append(pygame.Rect( (x, y), (self.thickness, TILE) ))
            return rects
        def check_cell(self, x, y):
            find_index = lambda x, y: x + y * cols
            if x < 0 or x > cols - 1 or y < 0 or y > rows - 1:
                return False
            return self.grid_cells[find_index(x, y)]
        def check_neighbors(self, grid_cells):
            self.grid_cells = grid_cells
            neighbors = []
            top = self.check_cell(self.x, self.y - 1)
            right = self.check_cell(self.x + 1, self.y)
            bottom = self.check_cell(self.x, self.y + 1)
            left = self.check_cell(self.x - 1, self.y)
            if top and not top.visited:
                neighbors.append(top)
            if right and not right.visited:
                neighbors.append(right)
            if bottom and not bottom.visited:
                neighbors.append(bottom)
            if left and not left.visited:
                neighbors.append(left)
            return choice(neighbors) if neighbors else False
    def remove_walls(current, next):
        dx = current.x - next.x
        if dx == 1:
            current.walls['left'] = False
            next.walls['right'] = False
        elif dx == -1:
            current.walls['right'] = False
            next.walls['left'] = False
        dy = current.y - next.y
        if dy == 1:
            current.walls['top'] = False
            next.walls['bottom'] = False
        elif dy == -1:
            current.walls['bottom'] = False
            next.walls['top'] = False
    def generate_maze():
        grid_cells = [Cell(col, row) for row in range(rows) for col in range(cols)]
        current_cell = grid_cells[0]
        array = []
        break_count = 1
        while break_count != len(grid_cells):
            current_cell.visited = True
            next_cell = current_cell.check_neighbors(grid_cells)
            if next_cell:
                next_cell.visited = True
                break_count += 1
                array.append(current_cell)
                remove_walls(current_cell, next_cell)
                current_cell = next_cell
            elif array:
                current_cell = array.pop()
        return grid_cells
    
    game_play = pygame.mixer.music.load('intro.mp3')
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.1)
    score = 0
    class Food:
        def __init__(self):
            self.img = pygame.image.load('food.png').convert_alpha()
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
            set_record(record, time)
            record = get_easy_2()
            
    def get_med_2():
        try:
            with open('record_3_2') as f:
                return f.readline()
        except FileNotFoundError:
            with open('record_3_2', 'w') as f:
                f.write('0')
                return 0
    def set_record(record, score):
        rec = max(int(record), score)
        with open('record_3_2', 'w') as f:
            f.write(str(rec))
    FPS = 60
    
    # get maze
    maze = generate_maze()
    # player settings
    player_speed = 5
    player_img = pygame.image.load('player2.png').convert_alpha()
    player_img = pygame.transform.scale(player_img, (TILE - 2 * maze[0].thickness, TILE - 2 * maze[0].thickness))
    player_rect = player_img.get_rect()
    player_rect.center = TILE // 2, TILE // 2
    directions = {'a': (-player_speed, 0), 'd': (player_speed, 0), 'w': (0, -player_speed), 's': (0, player_speed)}
    keys = {'a': pygame.K_LEFT, 'd': pygame.K_RIGHT, 'w': pygame.K_UP, 's': pygame.K_DOWN }
    direction = (0, 0)
    # food settings
    food_list = [Food() for i in range(1)]
    # collision list
    walls_collide_list = sum([cell.get_rects() for cell in maze], [])
    # timer, score, record
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    
    record = get_easy_2()
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
            if score == 1:
                set_record(record,time)
                if time >int(record):
                    print("New record")
                easy_3(100,15)
            if time == 0:
                set_record(record,time)
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
        surface.blit(text_font.render('record:', True, pygame.Color('magenta'), True), (WIDTH + 70, 300))
        surface.blit(font.render(f'{record}', True, pygame.Color('magenta')), (WIDTH + 70, 340))
        # print(clock.get_fps())
        pygame.display.flip()
        clock.tick(FPS)

def easy_3(TILE,time):
    pygame.display.set_caption('Easy level 3')
    RES = WIDTH, HEIGHT = 700, 500
    cols, rows = WIDTH // TILE, HEIGHT // TILE
    
    game_surface = pygame.Surface(RES)
    surface = pygame.display.set_mode((WIDTH + 300, HEIGHT))
    clock = pygame.time.Clock()
    # images
    bg_game = pygame.image.load('bg_1.jpeg').convert()
    bg = pygame.image.load('bg_main.png').convert()
    bg_intro = pygame.image.load('intro.jpeg')
    icon = pygame.image.load('icon.png')
    pygame.display.set_icon(icon)
    pygame.init()
    class Cell:
        def __init__(self, x, y):
            self.x, self.y = x, y
            self.walls = {'top': True, 'right': True, 'bottom': True, 'left': True}
            self.visited = False
            self.thickness = 4
        def draw(self, sc):
            x, y = self.x * TILE, self.y * TILE
            if self.walls['top']:
                pygame.draw.line(sc, pygame.Color('darkorange'), (x, y), (x + TILE, y), self.thickness)
            if self.walls['right']:
                pygame.draw.line(sc, pygame.Color('darkorange'), (x + TILE, y), (x + TILE, y + TILE), self.thickness)
            if self.walls['bottom']:
                pygame.draw.line(sc, pygame.Color('darkorange'), (x + TILE, y + TILE), (x , y + TILE), self.thickness)
            if self.walls['left']:
                pygame.draw.line(sc, pygame.Color('darkorange'), (x, y + TILE), (x, y), self.thickness)
        def get_rects(self):
            rects = []
            x, y = self.x * TILE, self.y * TILE
            if self.walls['top']:
                rects.append(pygame.Rect( (x, y), (TILE, self.thickness) ))
            if self.walls['right']:
                rects.append(pygame.Rect( (x + TILE, y), (self.thickness, TILE) ))
            if self.walls['bottom']:
                rects.append(pygame.Rect( (x, y + TILE), (TILE , self.thickness) ))
            if self.walls['left']:
                rects.append(pygame.Rect( (x, y), (self.thickness, TILE) ))
            return rects
        def check_cell(self, x, y):
            find_index = lambda x, y: x + y * cols
            if x < 0 or x > cols - 1 or y < 0 or y > rows - 1:
                return False
            return self.grid_cells[find_index(x, y)]
        def check_neighbors(self, grid_cells):
            self.grid_cells = grid_cells
            neighbors = []
            top = self.check_cell(self.x, self.y - 1)
            right = self.check_cell(self.x + 1, self.y)
            bottom = self.check_cell(self.x, self.y + 1)
            left = self.check_cell(self.x - 1, self.y)
            if top and not top.visited:
                neighbors.append(top)
            if right and not right.visited:
                neighbors.append(right)
            if bottom and not bottom.visited:
                neighbors.append(bottom)
            if left and not left.visited:
                neighbors.append(left)
            return choice(neighbors) if neighbors else False
    def remove_walls(current, next):
        dx = current.x - next.x
        if dx == 1:
            current.walls['left'] = False
            next.walls['right'] = False
        elif dx == -1:
            current.walls['right'] = False
            next.walls['left'] = False
        dy = current.y - next.y
        if dy == 1:
            current.walls['top'] = False
            next.walls['bottom'] = False
        elif dy == -1:
            current.walls['bottom'] = False
            next.walls['top'] = False
    def generate_maze():
        grid_cells = [Cell(col, row) for row in range(rows) for col in range(cols)]
        current_cell = grid_cells[0]
        array = []
        break_count = 1
        while break_count != len(grid_cells):
            current_cell.visited = True
            next_cell = current_cell.check_neighbors(grid_cells)
            if next_cell:
                next_cell.visited = True
                break_count += 1
                array.append(current_cell)
                remove_walls(current_cell, next_cell)
                current_cell = next_cell
            elif array:
                current_cell = array.pop()
        return grid_cells
    
    game_play = pygame.mixer.music.load('intro.mp3')
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.1)
    score = 0
    class Food:
        def __init__(self):
            self.img = pygame.image.load('food.png').convert_alpha()
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
            set_record(record, time)
            record = get_easy_3()
            
    def get_med_3():
        try:
            with open('record_3_3') as f:
                return f.readline()
        except FileNotFoundError:
            with open('record_3_3', 'w') as f:
                f.write('0')
                return 0
    def set_record(record, score):
        rec = max(int(record), score)
        with open('record_3_3', 'w') as f:
            f.write(str(rec))
    FPS = 60
    
    # get maze
    maze = generate_maze()
    # player settings
    player_speed = 5
    player_img = pygame.image.load('player2.png').convert_alpha()
    player_img = pygame.transform.scale(player_img, (TILE - 2 * maze[0].thickness, TILE - 2 * maze[0].thickness))
    player_rect = player_img.get_rect()
    player_rect.center = TILE // 2, TILE // 2
    directions = {'a': (-player_speed, 0), 'd': (player_speed, 0), 'w': (0, -player_speed), 's': (0, player_speed)}
    keys = {'a': pygame.K_LEFT, 'd': pygame.K_RIGHT, 'w': pygame.K_UP, 's': pygame.K_DOWN }
    direction = (0, 0)
    # food settings
    food_list = [Food() for i in range(1)]
    # collision list
    walls_collide_list = sum([cell.get_rects() for cell in maze], [])
    # timer, score, record
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    
    record = get_easy_3()
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
            if score == 1:
                set_record(record,time)
                if time >int(record):
                    print("New record")
                game_over()
            if time == 0:
                set_record(record,time)
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
        surface.blit(text_font.render('record:', True, pygame.Color('magenta'), True), (WIDTH + 70, 300))
        surface.blit(font.render(f'{record}', True, pygame.Color('magenta')), (WIDTH + 70, 340))
        # print(clock.get_fps())
        pygame.display.flip()
        clock.tick(FPS)

#medium levels
def med_1(TILE,time):
    pygame.display.set_caption('Medium level 1')
    RES = WIDTH, HEIGHT = 700, 500
    cols, rows = WIDTH // TILE, HEIGHT // TILE
    
    game_surface = pygame.Surface(RES)
    surface = pygame.display.set_mode((WIDTH + 300, HEIGHT))
    clock = pygame.time.Clock()
    # images
    bg_game = pygame.image.load('bg_1.jpeg').convert()
    bg = pygame.image.load('bg_main.png').convert()
    bg_intro = pygame.image.load('intro.jpeg')
    icon = pygame.image.load('icon.png')
    pygame.display.set_icon(icon)
    
    pygame.init()
    class Cell:
        def __init__(self, x, y):
            self.x, self.y = x, y
            self.walls = {'top': True, 'right': True, 'bottom': True, 'left': True}
            self.visited = False
            self.thickness = 4
        def draw(self, sc):
            x, y = self.x * TILE, self.y * TILE
            if self.walls['top']:
                pygame.draw.line(sc, pygame.Color('darkorange'), (x, y), (x + TILE, y), self.thickness)
            if self.walls['right']:
                pygame.draw.line(sc, pygame.Color('darkorange'), (x + TILE, y), (x + TILE, y + TILE), self.thickness)
            if self.walls['bottom']:
                pygame.draw.line(sc, pygame.Color('darkorange'), (x + TILE, y + TILE), (x , y + TILE), self.thickness)
            if self.walls['left']:
                pygame.draw.line(sc, pygame.Color('darkorange'), (x, y + TILE), (x, y), self.thickness)
        def get_rects(self):
            rects = []
            x, y = self.x * TILE, self.y * TILE
            if self.walls['top']:
                rects.append(pygame.Rect( (x, y), (TILE, self.thickness) ))
            if self.walls['right']:
                rects.append(pygame.Rect( (x + TILE, y), (self.thickness, TILE) ))
            if self.walls['bottom']:
                rects.append(pygame.Rect( (x, y + TILE), (TILE , self.thickness) ))
            if self.walls['left']:
                rects.append(pygame.Rect( (x, y), (self.thickness, TILE) ))
            return rects
        def check_cell(self, x, y):
            find_index = lambda x, y: x + y * cols
            if x < 0 or x > cols - 1 or y < 0 or y > rows - 1:
                return False
            return self.grid_cells[find_index(x, y)]
        def check_neighbors(self, grid_cells):
            self.grid_cells = grid_cells
            neighbors = []
            top = self.check_cell(self.x, self.y - 1)
            right = self.check_cell(self.x + 1, self.y)
            bottom = self.check_cell(self.x, self.y + 1)
            left = self.check_cell(self.x - 1, self.y)
            if top and not top.visited:
                neighbors.append(top)
            if right and not right.visited:
                neighbors.append(right)
            if bottom and not bottom.visited:
                neighbors.append(bottom)
            if left and not left.visited:
                neighbors.append(left)
            return choice(neighbors) if neighbors else False
    def remove_walls(current, next):
        dx = current.x - next.x
        if dx == 1:
            current.walls['left'] = False
            next.walls['right'] = False
        elif dx == -1:
            current.walls['right'] = False
            next.walls['left'] = False
        dy = current.y - next.y
        if dy == 1:
            current.walls['top'] = False
            next.walls['bottom'] = False
        elif dy == -1:
            current.walls['bottom'] = False
            next.walls['top'] = False
    def generate_maze():
        grid_cells = [Cell(col, row) for row in range(rows) for col in range(cols)]
        current_cell = grid_cells[0]
        array = []
        break_count = 1
        while break_count != len(grid_cells):
            current_cell.visited = True
            next_cell = current_cell.check_neighbors(grid_cells)
            if next_cell:
                next_cell.visited = True
                break_count += 1
                array.append(current_cell)
                remove_walls(current_cell, next_cell)
                current_cell = next_cell
            elif array:
                current_cell = array.pop()
        return grid_cells
    
    game_play = pygame.mixer.music.load('intro.mp3')
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.1)
    score = 0
    class Food:
        def __init__(self):
            self.img = pygame.image.load('food.png').convert_alpha()
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
            set_record(record, time)
            record = get_med_1()
            
    def get_med_1():
        try:
            with open('record_2_1') as f:
                return f.readline()
        except FileNotFoundError:
            with open('record_2_1', 'w') as f:
                f.write('0')
                return 0
    def set_record(record, score):
        rec = max(int(record), score)
        with open('record_2_1', 'w') as f:
            f.write(str(rec))
    FPS = 60
    
    # get maze
    maze = generate_maze()
    # player settings
    player_speed = 5
    player_img = pygame.image.load('player2.png').convert_alpha()
    player_img = pygame.transform.scale(player_img, (TILE - 2 * maze[0].thickness, TILE - 2 * maze[0].thickness))
    player_rect = player_img.get_rect()
    player_rect.center = TILE // 2, TILE // 2
    directions = {'a': (-player_speed, 0), 'd': (player_speed, 0), 'w': (0, -player_speed), 's': (0, player_speed)}
    keys = {'a': pygame.K_LEFT, 'd': pygame.K_RIGHT, 'w': pygame.K_UP, 's': pygame.K_DOWN }
    direction = (0, 0)
    # food settings
    food_list = [Food() for i in range(1)]
    # collision list
    walls_collide_list = sum([cell.get_rects() for cell in maze], [])
    # timer, score, record
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    
    record = get_med_1()
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
            if score == 1:
                set_record(record,time)
                if time >int(record):
                    print("New record")
                med_2(TILE,25)
            if time == 0:
                set_record(record,time)
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
        surface.blit(text_font.render('record:', True, pygame.Color('magenta'), True), (WIDTH + 30, 300))
        surface.blit(font.render(f'{record}', True, pygame.Color('magenta')), (WIDTH + 70, 340))
        # print(clock.get_fps())
        pygame.display.flip()
        clock.tick(FPS)

def med_2(TILE,time):
    pygame.display.set_caption('Medium level 2')
    RES = WIDTH, HEIGHT = 700, 500
    cols, rows = WIDTH // TILE, HEIGHT // TILE
    
    game_surface = pygame.Surface(RES)
    surface = pygame.display.set_mode((WIDTH + 300, HEIGHT))
    clock = pygame.time.Clock()
    # images
    bg_game = pygame.image.load('bg_1.jpeg').convert()
    bg = pygame.image.load('bg_main.png').convert()
    bg_intro = pygame.image.load('intro.jpeg')
    icon = pygame.image.load('icon.png')
    pygame.display.set_icon(icon)
    
    pygame.init()
    class Cell:
        def __init__(self, x, y):
            self.x, self.y = x, y
            self.walls = {'top': True, 'right': True, 'bottom': True, 'left': True}
            self.visited = False
            self.thickness = 4
        def draw(self, sc):
            x, y = self.x * TILE, self.y * TILE
            if self.walls['top']:
                pygame.draw.line(sc, pygame.Color('darkorange'), (x, y), (x + TILE, y), self.thickness)
            if self.walls['right']:
                pygame.draw.line(sc, pygame.Color('darkorange'), (x + TILE, y), (x + TILE, y + TILE), self.thickness)
            if self.walls['bottom']:
                pygame.draw.line(sc, pygame.Color('darkorange'), (x + TILE, y + TILE), (x , y + TILE), self.thickness)
            if self.walls['left']:
                pygame.draw.line(sc, pygame.Color('darkorange'), (x, y + TILE), (x, y), self.thickness)
        def get_rects(self):
            rects = []
            x, y = self.x * TILE, self.y * TILE
            if self.walls['top']:
                rects.append(pygame.Rect( (x, y), (TILE, self.thickness) ))
            if self.walls['right']:
                rects.append(pygame.Rect( (x + TILE, y), (self.thickness, TILE) ))
            if self.walls['bottom']:
                rects.append(pygame.Rect( (x, y + TILE), (TILE , self.thickness) ))
            if self.walls['left']:
                rects.append(pygame.Rect( (x, y), (self.thickness, TILE) ))
            return rects
        def check_cell(self, x, y):
            find_index = lambda x, y: x + y * cols
            if x < 0 or x > cols - 1 or y < 0 or y > rows - 1:
                return False
            return self.grid_cells[find_index(x, y)]
        def check_neighbors(self, grid_cells):
            self.grid_cells = grid_cells
            neighbors = []
            top = self.check_cell(self.x, self.y - 1)
            right = self.check_cell(self.x + 1, self.y)
            bottom = self.check_cell(self.x, self.y + 1)
            left = self.check_cell(self.x - 1, self.y)
            if top and not top.visited:
                neighbors.append(top)
            if right and not right.visited:
                neighbors.append(right)
            if bottom and not bottom.visited:
                neighbors.append(bottom)
            if left and not left.visited:
                neighbors.append(left)
            return choice(neighbors) if neighbors else False
    def remove_walls(current, next):
        dx = current.x - next.x
        if dx == 1:
            current.walls['left'] = False
            next.walls['right'] = False
        elif dx == -1:
            current.walls['right'] = False
            next.walls['left'] = False
        dy = current.y - next.y
        if dy == 1:
            current.walls['top'] = False
            next.walls['bottom'] = False
        elif dy == -1:
            current.walls['bottom'] = False
            next.walls['top'] = False
    def generate_maze():
        grid_cells = [Cell(col, row) for row in range(rows) for col in range(cols)]
        current_cell = grid_cells[0]
        array = []
        break_count = 1
        while break_count != len(grid_cells):
            current_cell.visited = True
            next_cell = current_cell.check_neighbors(grid_cells)
            if next_cell:
                next_cell.visited = True
                break_count += 1
                array.append(current_cell)
                remove_walls(current_cell, next_cell)
                current_cell = next_cell
            elif array:
                current_cell = array.pop()
        return grid_cells
    
    game_play = pygame.mixer.music.load('intro.mp3')
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.1)
    score = 0
    class Food:
        def __init__(self):
            self.img = pygame.image.load('food.png').convert_alpha()
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
            set_record(record, time)
            record = get_med_2()
            
    def get_med_2():
        try:
            with open('record_2_2') as f:
                return f.readline()
        except FileNotFoundError:
            with open('record_2_2', 'w') as f:
                f.write('0')
                return 0
    def set_record(record, score):
        rec = max(int(record), score)
        with open('record_2_2', 'w') as f:
            f.write(str(rec))
    FPS = 60
    
    # get maze
    maze = generate_maze()
    # player settings
    player_speed = 5
    player_img = pygame.image.load('player2.png').convert_alpha()
    player_img = pygame.transform.scale(player_img, (TILE - 2 * maze[0].thickness, TILE - 2 * maze[0].thickness))
    player_rect = player_img.get_rect()
    player_rect.center = TILE // 2, TILE // 2
    directions = {'a': (-player_speed, 0), 'd': (player_speed, 0), 'w': (0, -player_speed), 's': (0, player_speed)}
    keys = {'a': pygame.K_LEFT, 'd': pygame.K_RIGHT, 'w': pygame.K_UP, 's': pygame.K_DOWN }
    direction = (0, 0)
    # food settings
    food_list = [Food() for i in range(1)]
    # collision list
    walls_collide_list = sum([cell.get_rects() for cell in maze], [])
    # timer, score, record
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    
    record = get_med_2()
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
            if score == 1:
                set_record(record,time)
                if time >int(record):
                    print("New record")
                med_3(TILE,20)
            if time == 0:
                set_record(record,time)
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
        surface.blit(text_font.render('record:', True, pygame.Color('magenta'), True), (WIDTH + 30, 300))
        surface.blit(font.render(f'{record}', True, pygame.Color('magenta')), (WIDTH + 70, 340))
        # print(clock.get_fps())
        pygame.display.flip()
        clock.tick(FPS)

def med_3(TILE,time):
    pygame.display.set_caption('Medium level 3')
    RES = WIDTH, HEIGHT = 700, 500
    cols, rows = WIDTH // TILE, HEIGHT // TILE
    
    game_surface = pygame.Surface(RES)
    surface = pygame.display.set_mode((WIDTH + 300, HEIGHT))
    clock = pygame.time.Clock()
    # images
    bg_game = pygame.image.load('bg_1.jpeg').convert()
    bg = pygame.image.load('bg_main.png').convert()
    bg_intro = pygame.image.load('intro.jpeg')
    icon = pygame.image.load('icon.png')
    pygame.display.set_icon(icon)
    
    pygame.init()
    class Cell:
        def __init__(self, x, y):
            self.x, self.y = x, y
            self.walls = {'top': True, 'right': True, 'bottom': True, 'left': True}
            self.visited = False
            self.thickness = 4
        def draw(self, sc):
            x, y = self.x * TILE, self.y * TILE
            if self.walls['top']:
                pygame.draw.line(sc, pygame.Color('darkorange'), (x, y), (x + TILE, y), self.thickness)
            if self.walls['right']:
                pygame.draw.line(sc, pygame.Color('darkorange'), (x + TILE, y), (x + TILE, y + TILE), self.thickness)
            if self.walls['bottom']:
                pygame.draw.line(sc, pygame.Color('darkorange'), (x + TILE, y + TILE), (x , y + TILE), self.thickness)
            if self.walls['left']:
                pygame.draw.line(sc, pygame.Color('darkorange'), (x, y + TILE), (x, y), self.thickness)
        def get_rects(self):
            rects = []
            x, y = self.x * TILE, self.y * TILE
            if self.walls['top']:
                rects.append(pygame.Rect( (x, y), (TILE, self.thickness) ))
            if self.walls['right']:
                rects.append(pygame.Rect( (x + TILE, y), (self.thickness, TILE) ))
            if self.walls['bottom']:
                rects.append(pygame.Rect( (x, y + TILE), (TILE , self.thickness) ))
            if self.walls['left']:
                rects.append(pygame.Rect( (x, y), (self.thickness, TILE) ))
            return rects
        def check_cell(self, x, y):
            find_index = lambda x, y: x + y * cols
            if x < 0 or x > cols - 1 or y < 0 or y > rows - 1:
                return False
            return self.grid_cells[find_index(x, y)]
        def check_neighbors(self, grid_cells):
            self.grid_cells = grid_cells
            neighbors = []
            top = self.check_cell(self.x, self.y - 1)
            right = self.check_cell(self.x + 1, self.y)
            bottom = self.check_cell(self.x, self.y + 1)
            left = self.check_cell(self.x - 1, self.y)
            if top and not top.visited:
                neighbors.append(top)
            if right and not right.visited:
                neighbors.append(right)
            if bottom and not bottom.visited:
                neighbors.append(bottom)
            if left and not left.visited:
                neighbors.append(left)
            return choice(neighbors) if neighbors else False
    def remove_walls(current, next):
        dx = current.x - next.x
        if dx == 1:
            current.walls['left'] = False
            next.walls['right'] = False
        elif dx == -1:
            current.walls['right'] = False
            next.walls['left'] = False
        dy = current.y - next.y
        if dy == 1:
            current.walls['top'] = False
            next.walls['bottom'] = False
        elif dy == -1:
            current.walls['bottom'] = False
            next.walls['top'] = False
    def generate_maze():
        grid_cells = [Cell(col, row) for row in range(rows) for col in range(cols)]
        current_cell = grid_cells[0]
        array = []
        break_count = 1
        while break_count != len(grid_cells):
            current_cell.visited = True
            next_cell = current_cell.check_neighbors(grid_cells)
            if next_cell:
                next_cell.visited = True
                break_count += 1
                array.append(current_cell)
                remove_walls(current_cell, next_cell)
                current_cell = next_cell
            elif array:
                current_cell = array.pop()
        return grid_cells
    
    game_play = pygame.mixer.music.load('intro.mp3')
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.1)
    score = 0
    class Food:
        def __init__(self):
            self.img = pygame.image.load('food.png').convert_alpha()
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
            set_record(record, time)
            record = get_med_3()
            
    def get_med_3():
        try:
            with open('record_2_3') as f:
                return f.readline()
        except FileNotFoundError:
            with open('record_2_3', 'w') as f:
                f.write('0')
                return 0
    def set_record(record, score):
        rec = max(int(record), score)
        with open('record_2_3', 'w') as f:
            f.write(str(rec))
    FPS = 60
    
    # get maze
    maze = generate_maze()
    # player settings
    player_speed = 5
    player_img = pygame.image.load('player2.png').convert_alpha()
    player_img = pygame.transform.scale(player_img, (TILE - 2 * maze[0].thickness, TILE - 2 * maze[0].thickness))
    player_rect = player_img.get_rect()
    player_rect.center = TILE // 2, TILE // 2
    directions = {'a': (-player_speed, 0), 'd': (player_speed, 0), 'w': (0, -player_speed), 's': (0, player_speed)}
    keys = {'a': pygame.K_LEFT, 'd': pygame.K_RIGHT, 'w': pygame.K_UP, 's': pygame.K_DOWN }
    direction = (0, 0)
    # food settings
    food_list = [Food() for i in range(1)]
    # collision list
    walls_collide_list = sum([cell.get_rects() for cell in maze], [])
    # timer, score, record
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    
    record = get_med_3()
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
            if score == 1:
                set_record(record,time)
                if time >int(record):
                    print("New record")
                game_over()
            if time == 0:
                set_record(record,time)
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
        surface.blit(text_font.render('record:', True, pygame.Color('magenta'), True), (WIDTH + 30, 300))
        surface.blit(font.render(f'{record}', True, pygame.Color('magenta')), (WIDTH + 70, 340))
        # print(clock.get_fps())
        pygame.display.flip()
        clock.tick(FPS)

#hard levels
def hard_1(TILE,time):
    pygame.display.set_caption('Hard level 1')
    RES = WIDTH, HEIGHT = 700, 500
    cols, rows = WIDTH // TILE, HEIGHT // TILE
    
    game_surface = pygame.Surface(RES)
    surface = pygame.display.set_mode((WIDTH + 300, HEIGHT))
    clock = pygame.time.Clock()
    # images
    bg_game = pygame.image.load('bg_1.jpeg').convert()
    bg = pygame.image.load('bg_main.png').convert()
    bg_intro = pygame.image.load('intro.jpeg')
    icon = pygame.image.load('icon.png')
    pygame.display.set_icon(icon)
    pygame.init()
    class Cell:
        def __init__(self, x, y):
            self.x, self.y = x, y
            self.walls = {'top': True, 'right': True, 'bottom': True, 'left': True}
            self.visited = False
            self.thickness = 4
        def draw(self, sc):
            x, y = self.x * TILE, self.y * TILE
            if self.walls['top']:
                pygame.draw.line(sc, pygame.Color('darkorange'), (x, y), (x + TILE, y), self.thickness)
            if self.walls['right']:
                pygame.draw.line(sc, pygame.Color('darkorange'), (x + TILE, y), (x + TILE, y + TILE), self.thickness)
            if self.walls['bottom']:
                pygame.draw.line(sc, pygame.Color('darkorange'), (x + TILE, y + TILE), (x , y + TILE), self.thickness)
            if self.walls['left']:
                pygame.draw.line(sc, pygame.Color('darkorange'), (x, y + TILE), (x, y), self.thickness)
        def get_rects(self):
            rects = []
            x, y = self.x * TILE, self.y * TILE
            if self.walls['top']:
                rects.append(pygame.Rect( (x, y), (TILE, self.thickness) ))
            if self.walls['right']:
                rects.append(pygame.Rect( (x + TILE, y), (self.thickness, TILE) ))
            if self.walls['bottom']:
                rects.append(pygame.Rect( (x, y + TILE), (TILE , self.thickness) ))
            if self.walls['left']:
                rects.append(pygame.Rect( (x, y), (self.thickness, TILE) ))
            return rects
        def check_cell(self, x, y):
            find_index = lambda x, y: x + y * cols
            if x < 0 or x > cols - 1 or y < 0 or y > rows - 1:
                return False
            return self.grid_cells[find_index(x, y)]
        def check_neighbors(self, grid_cells):
            self.grid_cells = grid_cells
            neighbors = []
            top = self.check_cell(self.x, self.y - 1)
            right = self.check_cell(self.x + 1, self.y)
            bottom = self.check_cell(self.x, self.y + 1)
            left = self.check_cell(self.x - 1, self.y)
            if top and not top.visited:
                neighbors.append(top)
            if right and not right.visited:
                neighbors.append(right)
            if bottom and not bottom.visited:
                neighbors.append(bottom)
            if left and not left.visited:
                neighbors.append(left)
            return choice(neighbors) if neighbors else False
    def remove_walls(current, next):
        dx = current.x - next.x
        if dx == 1:
            current.walls['left'] = False
            next.walls['right'] = False
        elif dx == -1:
            current.walls['right'] = False
            next.walls['left'] = False
        dy = current.y - next.y
        if dy == 1:
            current.walls['top'] = False
            next.walls['bottom'] = False
        elif dy == -1:
            current.walls['bottom'] = False
            next.walls['top'] = False
    def generate_maze():
        grid_cells = [Cell(col, row) for row in range(rows) for col in range(cols)]
        current_cell = grid_cells[0]
        array = []
        break_count = 1
        while break_count != len(grid_cells):
            current_cell.visited = True
            next_cell = current_cell.check_neighbors(grid_cells)
            if next_cell:
                next_cell.visited = True
                break_count += 1
                array.append(current_cell)
                remove_walls(current_cell, next_cell)
                current_cell = next_cell
            elif array:
                current_cell = array.pop()
        return grid_cells
    
    game_play = pygame.mixer.music.load('intro.mp3')
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.1)
    score = 0
    class Food:
        def __init__(self):
            self.img = pygame.image.load('food.png').convert_alpha()
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
            set_record(record, time)
            record = get_hard_1()
            
    def get_hard_1():
        try:
            with open('record_1_1') as f:
                return f.readline()
        except FileNotFoundError:
            with open('record_1_1', 'w') as f:
                f.write('0')
                return 0
    def set_record(record, score):
        rec = max(int(record), score)
        with open('record_1_1', 'w') as f:
            f.write(str(rec))
    FPS = 60
    
    # get maze
    maze = generate_maze()
    # player settings
    player_speed = 5
    player_img = pygame.image.load('player2.png').convert_alpha()
    player_img = pygame.transform.scale(player_img, (TILE - 2 * maze[0].thickness, TILE - 2 * maze[0].thickness))
    player_rect = player_img.get_rect()
    player_rect.center = TILE // 2, TILE // 2
    directions = {'a': (-player_speed, 0), 'd': (player_speed, 0), 'w': (0, -player_speed), 's': (0, player_speed)}
    keys = {'a': pygame.K_LEFT, 'd': pygame.K_RIGHT, 'w': pygame.K_UP, 's': pygame.K_DOWN }
    direction = (0, 0)
    # food settings
    food_list = [Food() for i in range(1)]
    # collision list
    walls_collide_list = sum([cell.get_rects() for cell in maze], [])
    # timer, score, record
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    
    record = get_hard_1()
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
            if score == 1:
                set_record(record,time)
                if time >int(record):
                    print("New record")
                hard_2(30,35)
            if time == 0:
                set_record(record,time)
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
        surface.blit(text_font.render('record:', True, pygame.Color('magenta'), True), (WIDTH + 30, 300))
        surface.blit(font.render(f'{record}', True, pygame.Color('magenta')), (WIDTH + 70, 340))
        # print(clock.get_fps())
        pygame.display.flip()
        clock.tick(FPS)

def hard_2(TILE,time):
    pygame.display.set_caption('Hard level 2')
    RES = WIDTH, HEIGHT = 700, 500
    cols, rows = WIDTH // TILE, HEIGHT // TILE
    
    game_surface = pygame.Surface(RES)
    surface = pygame.display.set_mode((WIDTH + 300, HEIGHT))
    clock = pygame.time.Clock()
    # images
    bg_game = pygame.image.load('bg_1.jpeg').convert()
    bg = pygame.image.load('bg_main.png').convert()
    bg_intro = pygame.image.load('intro.jpeg')
    icon = pygame.image.load('icon.png')
    pygame.display.set_icon(icon)
    pygame.init()
    class Cell:
        def __init__(self, x, y):
            self.x, self.y = x, y
            self.walls = {'top': True, 'right': True, 'bottom': True, 'left': True}
            self.visited = False
            self.thickness = 4
        def draw(self, sc):
            x, y = self.x * TILE, self.y * TILE
            if self.walls['top']:
                pygame.draw.line(sc, pygame.Color('darkorange'), (x, y), (x + TILE, y), self.thickness)
            if self.walls['right']:
                pygame.draw.line(sc, pygame.Color('darkorange'), (x + TILE, y), (x + TILE, y + TILE), self.thickness)
            if self.walls['bottom']:
                pygame.draw.line(sc, pygame.Color('darkorange'), (x + TILE, y + TILE), (x , y + TILE), self.thickness)
            if self.walls['left']:
                pygame.draw.line(sc, pygame.Color('darkorange'), (x, y + TILE), (x, y), self.thickness)
        def get_rects(self):
            rects = []
            x, y = self.x * TILE, self.y * TILE
            if self.walls['top']:
                rects.append(pygame.Rect( (x, y), (TILE, self.thickness) ))
            if self.walls['right']:
                rects.append(pygame.Rect( (x + TILE, y), (self.thickness, TILE) ))
            if self.walls['bottom']:
                rects.append(pygame.Rect( (x, y + TILE), (TILE , self.thickness) ))
            if self.walls['left']:
                rects.append(pygame.Rect( (x, y), (self.thickness, TILE) ))
            return rects
        def check_cell(self, x, y):
            find_index = lambda x, y: x + y * cols
            if x < 0 or x > cols - 1 or y < 0 or y > rows - 1:
                return False
            return self.grid_cells[find_index(x, y)]
        def check_neighbors(self, grid_cells):
            self.grid_cells = grid_cells
            neighbors = []
            top = self.check_cell(self.x, self.y - 1)
            right = self.check_cell(self.x + 1, self.y)
            bottom = self.check_cell(self.x, self.y + 1)
            left = self.check_cell(self.x - 1, self.y)
            if top and not top.visited:
                neighbors.append(top)
            if right and not right.visited:
                neighbors.append(right)
            if bottom and not bottom.visited:
                neighbors.append(bottom)
            if left and not left.visited:
                neighbors.append(left)
            return choice(neighbors) if neighbors else False
    def remove_walls(current, next):
        dx = current.x - next.x
        if dx == 1:
            current.walls['left'] = False
            next.walls['right'] = False
        elif dx == -1:
            current.walls['right'] = False
            next.walls['left'] = False
        dy = current.y - next.y
        if dy == 1:
            current.walls['top'] = False
            next.walls['bottom'] = False
        elif dy == -1:
            current.walls['bottom'] = False
            next.walls['top'] = False
    def generate_maze():
        grid_cells = [Cell(col, row) for row in range(rows) for col in range(cols)]
        current_cell = grid_cells[0]
        array = []
        break_count = 1
        while break_count != len(grid_cells):
            current_cell.visited = True
            next_cell = current_cell.check_neighbors(grid_cells)
            if next_cell:
                next_cell.visited = True
                break_count += 1
                array.append(current_cell)
                remove_walls(current_cell, next_cell)
                current_cell = next_cell
            elif array:
                current_cell = array.pop()
        return grid_cells
    
    game_play = pygame.mixer.music.load('intro.mp3')
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.1)
    score = 0
    class Food:
        def __init__(self):
            self.img = pygame.image.load('food.png').convert_alpha()
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
            set_record(record, time)
            record = get_hard_2()
            
    def get_hard_2():
        try:
            with open('record_1_2') as f:
                return f.readline()
        except FileNotFoundError:
            with open('record_1_2', 'w') as f:
                f.write('0')
                return 0
    def set_record(record, score):
        rec = max(int(record), score)
        with open('record_1_2', 'w') as f:
            f.write(str(rec))
    FPS = 60
    
    # get maze
    maze = generate_maze()
    # player settings
    player_speed = 5
    player_img = pygame.image.load('player2.png').convert_alpha()
    player_img = pygame.transform.scale(player_img, (TILE - 2 * maze[0].thickness, TILE - 2 * maze[0].thickness))
    player_rect = player_img.get_rect()
    player_rect.center = TILE // 2, TILE // 2
    directions = {'a': (-player_speed, 0), 'd': (player_speed, 0), 'w': (0, -player_speed), 's': (0, player_speed)}
    keys = {'a': pygame.K_LEFT, 'd': pygame.K_RIGHT, 'w': pygame.K_UP, 's': pygame.K_DOWN }
    direction = (0, 0)
    # food settings
    food_list = [Food() for i in range(1)]
    # collision list
    walls_collide_list = sum([cell.get_rects() for cell in maze], [])
    # timer, score, record
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    
    record = get_hard_2()
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
            if score == 1:
                set_record(record,time)
                if time >int(record):
                    print("New record")
                hard_3(30,25)
            if time == 0:
                set_record(record,time)
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
        surface.blit(text_font.render('record:', True, pygame.Color('magenta'), True), (WIDTH + 30, 300))
        surface.blit(font.render(f'{record}', True, pygame.Color('magenta')), (WIDTH + 70, 340))
        # print(clock.get_fps())
        pygame.display.flip()
        clock.tick(FPS)

def hard_3(TILE,time):
    pygame.display.set_caption('Hard level 3')
    RES = WIDTH, HEIGHT = 700, 500
    cols, rows = WIDTH // TILE, HEIGHT // TILE
    
    game_surface = pygame.Surface(RES)
    surface = pygame.display.set_mode((WIDTH + 300, HEIGHT))
    clock = pygame.time.Clock()
    # images
    bg_game = pygame.image.load('bg_1.jpeg').convert()
    bg = pygame.image.load('bg_main.png').convert()
    bg_intro = pygame.image.load('intro.jpeg')
    icon = pygame.image.load('icon.png')
    pygame.display.set_icon(icon)
    pygame.init()
    class Cell:
        def __init__(self, x, y):
            self.x, self.y = x, y
            self.walls = {'top': True, 'right': True, 'bottom': True, 'left': True}
            self.visited = False
            self.thickness = 4
        def draw(self, sc):
            x, y = self.x * TILE, self.y * TILE
            if self.walls['top']:
                pygame.draw.line(sc, pygame.Color('darkorange'), (x, y), (x + TILE, y), self.thickness)
            if self.walls['right']:
                pygame.draw.line(sc, pygame.Color('darkorange'), (x + TILE, y), (x + TILE, y + TILE), self.thickness)
            if self.walls['bottom']:
                pygame.draw.line(sc, pygame.Color('darkorange'), (x + TILE, y + TILE), (x , y + TILE), self.thickness)
            if self.walls['left']:
                pygame.draw.line(sc, pygame.Color('darkorange'), (x, y + TILE), (x, y), self.thickness)
        def get_rects(self):
            rects = []
            x, y = self.x * TILE, self.y * TILE
            if self.walls['top']:
                rects.append(pygame.Rect( (x, y), (TILE, self.thickness) ))
            if self.walls['right']:
                rects.append(pygame.Rect( (x + TILE, y), (self.thickness, TILE) ))
            if self.walls['bottom']:
                rects.append(pygame.Rect( (x, y + TILE), (TILE , self.thickness) ))
            if self.walls['left']:
                rects.append(pygame.Rect( (x, y), (self.thickness, TILE) ))
            return rects
        def check_cell(self, x, y):
            find_index = lambda x, y: x + y * cols
            if x < 0 or x > cols - 1 or y < 0 or y > rows - 1:
                return False
            return self.grid_cells[find_index(x, y)]
        def check_neighbors(self, grid_cells):
            self.grid_cells = grid_cells
            neighbors = []
            top = self.check_cell(self.x, self.y - 1)
            right = self.check_cell(self.x + 1, self.y)
            bottom = self.check_cell(self.x, self.y + 1)
            left = self.check_cell(self.x - 1, self.y)
            if top and not top.visited:
                neighbors.append(top)
            if right and not right.visited:
                neighbors.append(right)
            if bottom and not bottom.visited:
                neighbors.append(bottom)
            if left and not left.visited:
                neighbors.append(left)
            return choice(neighbors) if neighbors else False
    def remove_walls(current, next):
        dx = current.x - next.x
        if dx == 1:
            current.walls['left'] = False
            next.walls['right'] = False
        elif dx == -1:
            current.walls['right'] = False
            next.walls['left'] = False
        dy = current.y - next.y
        if dy == 1:
            current.walls['top'] = False
            next.walls['bottom'] = False
        elif dy == -1:
            current.walls['bottom'] = False
            next.walls['top'] = False
    def generate_maze():
        grid_cells = [Cell(col, row) for row in range(rows) for col in range(cols)]
        current_cell = grid_cells[0]
        array = []
        break_count = 1
        while break_count != len(grid_cells):
            current_cell.visited = True
            next_cell = current_cell.check_neighbors(grid_cells)
            if next_cell:
                next_cell.visited = True
                break_count += 1
                array.append(current_cell)
                remove_walls(current_cell, next_cell)
                current_cell = next_cell
            elif array:
                current_cell = array.pop()
        return grid_cells
    
    game_play = pygame.mixer.music.load('intro.mp3')
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.1)
    score = 0
    class Food:
        def __init__(self):
            self.img = pygame.image.load('food.png').convert_alpha()
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
            set_record(record, time)
            record = get_hard_3()
            
    def get_hard_3():
        try:
            with open('record_1_3') as f:
                return f.readline()
        except FileNotFoundError:
            with open('record_1_3', 'w') as f:
                f.write('0')
                return 0
    def set_record(record, score):
        rec = max(int(record), score)
        with open('record_1_3', 'w') as f:
            f.write(str(rec))
    FPS = 60
    
    # get maze
    maze = generate_maze()
    # player settings
    player_speed = 5
    player_img = pygame.image.load('player2.png').convert_alpha()
    player_img = pygame.transform.scale(player_img, (TILE - 2 * maze[0].thickness, TILE - 2 * maze[0].thickness))
    player_rect = player_img.get_rect()
    player_rect.center = TILE // 2, TILE // 2
    directions = {'a': (-player_speed, 0), 'd': (player_speed, 0), 'w': (0, -player_speed), 's': (0, player_speed)}
    keys = {'a': pygame.K_LEFT, 'd': pygame.K_RIGHT, 'w': pygame.K_UP, 's': pygame.K_DOWN }
    direction = (0, 0)
    # food settings
    food_list = [Food() for i in range(1)]
    # collision list
    walls_collide_list = sum([cell.get_rects() for cell in maze], [])
    # timer, score, record
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    
    record = get_hard_3()
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
            if score == 1:
                set_record(record,time)
                if time >int(record):
                    print("New record")
                game_over()
            if time == 0:
                set_record(record,time)
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
        surface.blit(text_font.render('record:', True, pygame.Color('magenta'), True), (WIDTH + 30, 300))
        surface.blit(font.render(f'{record}', True, pygame.Color('magenta')), (WIDTH + 70, 340))
        # print(clock.get_fps())
        pygame.display.flip()
        clock.tick(FPS)

#main menu function
def welcome():
    icon = pygame.image.load('icon.png')
    pygame.display.set_icon(icon)
    pygame.display.set_caption('Main menu')
    exit_game = False
    music_welcome = pygame.mixer.music.load('cat.mp3')
    pygame.mixer.music.play(-1)
    while not exit_game:
        surface.blit(bg_intro,(0,0))
        surface.blit(text_font.render('Press "1"-hard ,"2"-medium or "3"-easy to play', False, pygame.Color('white'),True), (130,350))
        surface.blit(text_font.render('Press SPACE for leaderboards',False,pygame.Color('white'),True),(250,400))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_2:
                    med_1(50,30)
                if event.key == pygame.K_3:
                    easy_1(100,25)
                if event.key == pygame.K_1:
                    hard_1(30,50)
                if event.key == pygame.K_SPACE:
                    leaders()
        pygame.display.update()
        clock.tick(FPS)

#leaderboard function
def leaders():
    exit_game = False
    lead = pygame.image.load('lead.png')
    pygame.display.set_icon(lead)
    pygame.display.set_caption('leadership')
    while not exit_game:
        surface.fill(pygame.Color('darkorange'))
        surface.blit(font.render('Hard level:',True,pygame.Color('red'),True),(150,100))
        surface.blit(font.render(f'{get_hard_1()}', True, pygame.Color('darkred'),True), (400, 100))
        surface.blit(font.render(f'{get_hard_2()}', True, pygame.Color('darkred'),True), (480, 100))
        surface.blit(font.render(f'{get_hard_3()}', True, pygame.Color('darkred'),True), (530, 100))
        surface.blit(font.render('Medium level:',True,pygame.Color('yellow'),True),(150,200))
        surface.blit(font.render(f'{get_med_1()}', True, pygame.Color('yellow'),True), (450, 200))
        surface.blit(font.render(f'{get_med_2()}', True, pygame.Color('yellow'),True), (520, 200))
        surface.blit(font.render(f'{get_med_3()}', True, pygame.Color('yellow'),True), (590, 200))
        surface.blit(font.render('Easy level:',True,pygame.Color('green'),True),(150,300))
        surface.blit(font.render(f'{get_easy_1()}', True, pygame.Color('green'),True), (400, 300))
        surface.blit(font.render(f'{get_easy_2()}', True, pygame.Color('green'),True), (470, 300))
        surface.blit(font.render(f'{get_easy_3()}', True, pygame.Color('green'),True), (530, 300))
        surface.blit(text_font_1.render('Press "R" for main menu ', False, pygame.Color('white'), False), (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    welcome()

        
        pygame.display.update()
        clock.tick(FPS)

#game over page
def game_over():
    icon = pygame.image.load('icon.png')
    pygame.display.set_icon(icon)
    pygame.display.set_caption('Game over')
    gm_ovr = pygame.mixer.music.load('game_over.wav')
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(-1)
    exit_game = False
    while not exit_game:
        surface.fill(pygame.Color('black'))
        surface.blit(text_gm.render('GAME OVER', False, pygame.Color('darkred'), False), (250, 120))
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
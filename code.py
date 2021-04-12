import pygame, sys, os, time, random

clock = pygame.time.Clock()

from pygame.locals import *
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()

pygame.display.set_caption('mak gam')
screen_width=600; screen_height=400
global WINDOW_SIZE
WINDOW_SIZE = (600,400)

screen = pygame.display.set_mode(WINDOW_SIZE,0,32) 


CHUNK_SIZE = 15 ; font = "C:/WINDOWS/FONTS/TEMPSITC.ttf"

white=(255, 255, 255); black=(0, 0, 0); gray=(50, 50, 50); red=(255, 0, 0); green=(0, 255, 0); blue=(0, 0, 255); yellow=(255, 255, 0)

#Inventory
global inventory_size
inventory_size = [
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0]
    ]

def generate_chunk(x,y):
    chunk_data = []
    for y_pos in range(CHUNK_SIZE):
        for x_pos in range(CHUNK_SIZE):
            target_x = x * CHUNK_SIZE + x_pos
            target_y = y * CHUNK_SIZE + y_pos
            tile_type = 0 
            if target_y > 10:
                tile_type = 2
            elif target_y == 10:
                tile_type = 1
            elif target_y == 9:
                if random.randint(1,5) == 1:
                    tile_type = 3 
            if tile_type != 0:
                chunk_data.append([[target_x,target_y],tile_type])
    return chunk_data

global animation_frames
animation_frames = {}

def load_animation(path,frame_durations):
    global animation_frames
    animation_name = path.split('/')[-1]
    animation_frame_data = []
    n = 0
    for frame in frame_durations:
        animation_frame_id = animation_name + '_' + str(n)
        img_loc = path + '/' + animation_frame_id + '.png'
        animation_image = pygame.image.load(img_loc).convert()
        animation_image.set_colorkey((255,255,255))
        animation_frames[animation_frame_id] = animation_image.copy()
        for i in range(frame):
            animation_frame_data.append(animation_frame_id)
        n += 1
    return animation_frame_data

def change_action(action_var,frame,new_value):
    if action_var != new_value:
        action_var = new_value
        frame = 0
    return action_var,frame
        
def text_format(message, textFont, textSize, textColor):
    newFont=pygame.font.Font(textFont, textSize)
    newText=newFont.render(message, 0, textColor)
 
    return newText



def collision_test(rect,tiles):
    hit_list = []
    for tile in tiles:
        if rect.colliderect(tile):
            hit_list.append(tile)
    return hit_list

def move(rect,movement,tiles):
    collision_types = {'top':False,'bottom':False,'right':False,'left':False}
    rect.x += movement[0]
    hit_list = collision_test(rect,tiles)
    for tile in hit_list:
        if movement[0] > 0:
            rect.right = tile.left
            collision_types['right'] = True
        elif movement[0] < 0:
            rect.left = tile.right
            collision_types['left'] = True
    rect.y += movement[1]
    hit_list = collision_test(rect,tiles)
    for tile in hit_list:
        if movement[1] > 0:
            rect.bottom = tile.top
            collision_types['bottom'] = True
        elif movement[1] < 0:
            rect.top = tile.bottom
            collision_types['top'] = True
    return rect, collision_types

def mainmenu():
    
    menu=True
    selected="start"
    
    pygame.mixer.music.load('C:/Users/user/Documents/PyGameFolder/music/music.mp3')
    pygame.mixer.music.play(-1)
    while menu:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_UP:
                    selected="start"
                elif event.key==pygame.K_DOWN:
                    selected="quit"
                if event.key==pygame.K_RETURN:
                    if selected=="start":
                        choosecharc()
                    if selected=="quit":
                        pygame.quit()
                        quit()
                if event.key==pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
 

        screen.fill((52,62,67))
        title0=text_format("STUPID GAME", font, 25, (153,166,195))
        title=text_format("UP/DOWN ARROW KEY TO CHOOSE", font, 15, (153,166,195))
        title1=text_format("ENTER FOR CONFIRMATION", font, 15, (153,166,195))
        if selected=="start":
            text_start=text_format("START", font, 20, white)
        else:
            text_start = text_format("START", font, 20, black)
        if selected=="quit":
            text_quit=text_format("QUIT", font, 20, white)
        else:
            text_quit = text_format("QUIT", font, 20, black)
        title0_rect=title0.get_rect()
        title_rect=title.get_rect()
        title1_rect=title1.get_rect()
        start_rect=text_start.get_rect()
        quit_rect=text_quit.get_rect()



        screen.blit(title0, (screen_width/2 - (title0_rect[2]/2), 50))
        screen.blit(title, (screen_width/2 - (title_rect[2]/2), 80))
        screen.blit(title1, (screen_width/2 - (title1_rect[2]/2), 100))
        screen.blit(text_start, (screen_width/2 - (start_rect[2]/2), 300))
        screen.blit(text_quit, (screen_width/2 - (quit_rect[2]/2), 360))
        pygame.display.update()
        clock.tick(60)
        pygame.display.set_caption("mak gam")

def choosecharc():
    global num 
    num = 1
    pygame.mixer.music.load('C:/Users/user/Documents/PyGameFolder/music/lull.mp3')
    pygame.mixer.music.play(-1)
    menu=True
    selected="start"
    mage_img = pygame.image.load('C:/Users/user/Documents/PyGameFolder/mage.png').convert()
    mage_img.set_colorkey((255,255,255))
    gunner_img = pygame.image.load('C:/Users/user/Documents/PyGameFolder/pewpewanimation/idle/idle_0.png').convert()
    gunner_img.set_colorkey((255,255,255))
    while menu:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_UP:
                    selected="start"
                elif event.key==pygame.K_DOWN:
                    selected="quit"
                if event.key==pygame.K_RETURN:
                    if selected=="start":
                        num = 1
                        game(num)
                    if selected=="quit":
                        num = 2
                        game(num)
                if event.key==pygame.K_ESCAPE:
                    mainmenu()


        screen.fill((52,62,67))
        title0=text_format("CHOOSE CHARACTER", font, 25, (153,166,195))
        if selected=="start":
            text_start=text_format("GUNNER", font, 20, white)
        else:
            text_start = text_format("GUNNER", font, 20, black)
        if selected=="quit":
            text_quit=text_format("MAGE", font, 20, white)
        else:
            text_quit = text_format("MAGE", font, 20, black)
        title0_rect=title0.get_rect()
        start_rect=text_start.get_rect()
        quit_rect=text_quit.get_rect()

        screen.blit(title0, (screen_width/2 - (title0_rect[2]/2), 50))
        screen.blit(text_start, (screen_width/2 - (start_rect[2]/2), 300))
        screen.blit(text_quit, (screen_width/2 - (quit_rect[2]/2), 360))
        screen.blit(gunner_img, (screen_width/2 - (start_rect[2]), 300))
        screen.blit(mage_img, (screen_width/2 - (quit_rect[2] + 30), 340))
        pygame.display.update()
        clock.tick(60)
        pygame.display.set_caption("mak gam")

def inventory():
    global WINDOW_SIZE, num, inventory_size
    screen = pygame.display.set_mode(WINDOW_SIZE)
    screen.fill((52,62,67))
    inventory_img = pygame.image.load('C:/Users/user/Documents/PyGameFolder/inventory.png').convert()
    inventory_img.set_colorkey((255,255,255))
    biginventory_img = pygame.transform.smoothscale(inventory_img,(int(screen_width),int((screen_height/2))))
    inventory_rect = biginventory_img.get_rect()
    title = text_format("Inventory",font,50,(81,51,59))
    title_rect = title.get_rect()
    while True:
        screen.blit(biginventory_img, (screen_width/2 - (inventory_rect[2]/2), 130))
        screen.blit(title, (screen_width/2 - (title_rect[2]/2), 50))
        for event in pygame.event.get(): 
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE or event.key == K_e:
                        game(num)
                    else:
                        inventory()

        pygame.display.update()
        clock.tick(60)


def game(a):
    pygame.mixer.music.load('C:/Users/user/Documents/PyGameFolder/music/pop.mp3')
    pygame.mixer.music.play(-1)
    if a == 1:
        animation_database = {}
        animation_database['run'] = load_animation('C:/Users/user/Documents/PyGameFolder/pewpewanimation/run',[7,7])
        animation_database['idle'] = load_animation('C:/Users/user/Documents/PyGameFolder/pewpewanimation/idle',[7,7,40])
    elif a == 2:
        animation_database = {}
        animation_database['run'] = pygame.image.load('C:/Users/user/Documents/PyGameFolder/mage.png')
        animation_database['idle'] = pygame.image.load('C:/Users/user/Documents/PyGameFolder/mage.png')
    global display
    display = pygame.Surface((300,200)) ; moving_right = False ; moving_left = False ; move_down = False ;vertical_momentum = 0 ; air_timer = 0 ; true_scroll = [0,0] ; sprint = False
    

    game_map = {}

    grass_img = pygame.image.load('C:/Users/user/Documents/PyGameFolder/grass.png')
    dirt_img = pygame.image.load('C:/Users/user/Documents/PyGameFolder/dirt.png')
    plant_img = pygame.image.load('C:/Users/user/Documents/PyGameFolder/plant.png').convert()
    plant_img.set_colorkey((255,255,255))
    rock_img = pygame.image.load('C:/Users/user/Documents/PyGameFolder/rock.png')
    cobble_img = pygame.image.load('C:/Users/user/Documents/PyGameFolder/cobble.png')

    tile_index = {
        1:grass_img,
        2:dirt_img,
        3:plant_img,
        4:rock_img,
        5:cobble_img
        }


    jump_sound = pygame.mixer.Sound('C:/Users/user/Documents/PyGameFolder/jump.wav')
    grass_sounds = [pygame.mixer.Sound('C:/Users/user/Documents/PyGameFolder/grass_0.wav'),pygame.mixer.Sound('C:/Users/user/Documents/PyGameFolder/grass_1.wav')]
    grass_sounds[0].set_volume(0.2)
    grass_sounds[1].set_volume(0.2)



    player_action = 'idle'
    player_frame = 0
    player_flip = False

    grass_sound_timer = 0

    player_rect = pygame.Rect(100,100,23,23)

    background_objects = [[0.25,[120,10,70,400]],[0.25,[280,30,40,400]],[0.5,[30,40,40,400]],[0.5,[130,90,100,400]],[0.5,[300,80,120,400]]]

    while True: 

        display.fill((146,244,255)) 

        if grass_sound_timer > 0:
            grass_sound_timer -= 1

        true_scroll[0] += (player_rect.x-true_scroll[0]-152)/20
        true_scroll[1] += (player_rect.y-true_scroll[1]-106)/20
        scroll = true_scroll.copy()
        scroll[0] = int(scroll[0])
        scroll[1] = int(scroll[1])
        pygame.draw.rect(display,(7,80,75),pygame.Rect(0,120,300,80))
        for background_object in background_objects:
            obj_rect = pygame.Rect(background_object[1][0]-scroll[0]*background_object[0],background_object[1][1]-scroll[1]*background_object[0],background_object[1][2],background_object[1][3])
            if background_object[0] == 0.5:
                pygame.draw.rect(display,(14,222,150),obj_rect)
            else:
                pygame.draw.rect(display,(9,91,85),obj_rect)

        global tile_rects
        tile_rects = []
        for y in range(3):
            for x in range(4):
                target_x = x - 1 + int(round(scroll[0]/(CHUNK_SIZE*16)))
                target_y = y - 1 + int(round(scroll[1]/(CHUNK_SIZE*16)))
                target_chunk = str(target_x) + ';' + str(target_y)
                if target_chunk not in game_map:
                    game_map[target_chunk] = generate_chunk(target_x,target_y)
                for tile in game_map[target_chunk]:
                    display.blit(tile_index[tile[1]],(tile[0][0]*16-scroll[0],tile[0][1]*16-scroll[1]))
                    if tile[1] in [1,2]:
                        tile_rects.append(pygame.Rect(tile[0][0]*16,tile[0][1]*16,16,16))    

        global player_movement
        player_movement = [0,0]
        
        if moving_right == True:
            if sprint == True:
                player_movement[0] += 4
            else: 
                player_movement[0] += 2
        if moving_left == True:
            if sprint == True:
                player_movement[0] -= 4
            else:
                player_movement[0] -= 2
        if move_down == True:
            vertical_momentum += 2
        
        
        player_movement[1] += vertical_momentum
        vertical_momentum += 0.2
        if vertical_momentum > 3:
            vertical_momentum = 3
        
        if player_movement[0] == 0:
            player_action,player_frame = change_action(player_action,player_frame,'idle')
        if player_movement[0] > 0:
            player_flip = False
            player_action,player_frame = change_action(player_action,player_frame,'run')
        if player_movement[0] < 0:
            player_flip = True
            player_action,player_frame = change_action(player_action,player_frame,'run')

        player_rect,collisions = move(player_rect,player_movement,tile_rects)

        if collisions['bottom'] == True:
            air_timer = 0
            vertical_momentum = 0
            if player_movement[0] != 0:
                if grass_sound_timer == 0:
                    grass_sound_timer = 30
                    random.choice(grass_sounds).play()
        else:
            air_timer += 1

        player_frame += 1
        if player_frame >= len(animation_database[player_action]):
            player_frame = 0
        player_img_id = animation_database[player_action][player_frame]
        player_img = animation_frames[player_img_id]
        display.blit(pygame.transform.flip(player_img,player_flip,False),(player_rect.x-scroll[0],player_rect.y-scroll[1]))


        for event in pygame.event.get(): 
            if event.type == KEYDOWN:
                if event.key == K_DOWN or event.key == K_s:
                    move_down = True
                if event.key == K_q:
                    pygame.mixer.music.fadeout(1000)
                if event.key == K_RIGHT or event.key == K_d:
                    moving_right = True
                if event.key == K_LEFT or event.key == K_a:
                    moving_left = True
                if event.key == K_UP or event.key == K_SPACE or event.key == K_w:
                    if air_timer < 6:
                        jump_sound.play()
                        vertical_momentum = -5
                if event.key == K_ESCAPE:
                    mainmenu()
                if event.key == K_LSHIFT:
                    sprint = True
                if event.key == K_e:
                    inventory()
            if event.type == KEYUP:
                if event.key == K_DOWN or event.key == K_s:
                    move_down = False
                if event.key == K_RIGHT or event.key == K_d:
                    moving_right = False
                if event.key == K_LEFT or event.key == K_a:
                    moving_left = False
                if event.key == K_LSHIFT:
                    sprint = False
        
        screen.blit(pygame.transform.scale(display,WINDOW_SIZE),(0,0))
        pygame.display.update()
        clock.tick(60)



if __name__ == "__main__":
    mainmenu()

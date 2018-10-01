from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024

running = True
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
frame = 0
hide_cursor()

posX, posY = 400, 300
gotoX, gotoY = 0, 0
checkRight = 0
count = 101

def move_to_point_character():
    global posX
    global posY
    global count
    if count > 100:
        return
    count += 1
    posX += gotoX
    posY += gotoY


def handle_events():
    global running
    global x, y
    global gotoX
    global gotoY
    global checkRight
    global count
    #get_events()는 입력받은 event를 리스트로 가지고 온다.
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            x, y = event.x, KPU_HEIGHT - 1 - event.y
        elif event.type == SDL_MOUSEBUTTONDOWN:
            x, y = event.x, KPU_HEIGHT - 1 - event.y
            count = 0
            gotoX = (x - 50 - posX) / 100
            gotoY = (y + 50 - posY) / 100
            if (posX - x) > 0:
                checkRight = 0
            else:
                checkRight = 1
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


open_canvas(KPU_WIDTH, KPU_HEIGHT)
# fill here
kpu_ground = load_image('KPU_GROUND.png')
arrow = load_image('hand_arrow.png')
character = load_image('animation_sheet.png')



while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)

    move_to_point_character()

    arrow.clip_draw(0, 0, 100, 100, x, y)
    character.clip_draw(frame * 100, checkRight * 100, 100, 100, posX, posY)

    update_canvas()
    frame = (frame + 1) % 8
    delay(0.02)
    handle_events()

close_canvas()





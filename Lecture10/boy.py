from pico2d import *

# Boy State
IDLE, RUN, SLEEP = range(3)

# Boy Event
RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP, TIME_OUT = range(5)

# Dic type key_event_table
key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,  #KEYDOWN 이면서 RIGHT ARROW키를 눌렀을때
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,    #
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,      #
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP         #
}

# Dic type state_table
next_state_table = {
        # IDLE 일때
        IDLE: {RIGHT_UP: RUN, LEFT_UP: RUN, RIGHT_DOWN: RUN, LEFT_DOWN: RUN,
                TIME_OUT: SLEEP},
        # Run 일때
        RUN: {RIGHT_UP: IDLE, LEFT_UP: IDLE, RIGHT_DOWN: IDLE, LEFT_DOWN: IDLE},
        # Speed 일때
        SLEEP: {LEFT_DOWN: RUN, RIGHT_DOWN: RUN}
}

class Boy:

    def __init__(self):
        # ??
        self.event_que = []
        self.x, self.y = 800 // 2, 90
        self.image = load_image('animation_sheet.png')
        self.cur_state = IDLE
        self.dir = 1
        self.velocity = 0
        self.enter_state[IDLE](self)



    # IDLE state functions
    def enter_IDLE(self):
        self.timer = 1000
        self.frame = 0

    def exit_IDLE(self):
        # 특별히 할일 없음
        pass

    def do_IDLE(self):
        self.frame = (self.frame + 1) % 8
        # sleeptimer가 줄어들어 0이 되면 SLEEP함
        self.timer -= 1
        if self.timer == 0:
            # SLEEP 상태 이벤트를 add한다.
            self.add_event(SLEEP)

    def draw_IDLE(self):
        if self.dir == 1:
            self.image.clip_draw(self.frame * 100, 300, 100, 100, self.x, self.y)
        else:
            self.image.clip_draw(self.frame * 100, 200, 100, 100, self.x, self.y)




    # RUN state functions
    def enter_RUN(self):
        self.frame = 0
        self.dir = self.velocity

    def exit_RUN(self):
        pass

    def do_RUN(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.velocity
        # self.x를 25와 800 - 25 사이 값으로 만듬
        self.x = clamp(25, self.x, 800 - 25)

    def draw_RUN(self):
        if self.velocity == 1:
            self.image.clip_draw(self.frame * 100, 100, 100, 100, self.x, self.y)
        else:
            self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)


    # SLEEP state functions
    def enter_SLEEP(self):
        print('Enter SLEEP')
        self.frame = 0

    def exit_SLEEP(self):
        print('Exit SLEEP')

    def do_SLEEP(self):
        self.frame = (self.frame + 1) % 8

    def draw_SLEEP(self):
        if self.dir == 1:
            self.image.clip_composite_draw(self.frame * 100, 300, 100, 100, 3.141592/2, '', self.x-25, self.y-25, 100, 100)
        else:
            self.image.clip_composite_draw(self.frame * 100, 200, 100, 100, -3.141592/2, '', self.x+25, self.y-25, 100, 100)



    def add_event(self, event):
        # ??
        self.event_que.insert(0, event)


    def change_state(self,  state):
        # 빠져 나올 상태
        self.exit_state[self.cur_state](self)
        # 들어올 상태
        self.enter_state[state](self)
        # 현재 상태
        self.cur_state = state

    # Dic으로 처리해서 상태에 맞는 함수를 호출하게 한다.
    # C++에서 Function Pointer
    enter_state = {IDLE: enter_IDLE , RUN: enter_RUN, SLEEP: enter_SLEEP}
    exit_state  = {IDLE: exit_IDLE  , RUN: exit_RUN , SLEEP: exit_SLEEP}
    do_state    = {IDLE: do_IDLE    , RUN: do_RUN   , SLEEP: do_SLEEP}
    draw_state  = {IDLE: draw_IDLE  , RUN: draw_RUN, SLEEP: draw_SLEEP}


    def update(self):
        self.do_state[self.cur_state](self)
        # ??
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.change_state(next_state_table[self.cur_state][event])

    def draw(self):
       self.draw_state[self.cur_state](self)


    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            if key_event == RIGHT_DOWN:
                self.velocity += 1
            elif key_event == LEFT_DOWN:
                self.velocity -= 1
            elif key_event == RIGHT_UP:
                self.velocity -= 1
            elif key_event == LEFT_UP:
                self.velocity += 1
            # que
            self.add_event(key_event)


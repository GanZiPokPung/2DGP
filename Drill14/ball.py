import random
from pico2d import *
import game_world
import game_framework

class Ball:
    image = None
    sound = None
    def __init__(self):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y, self.fall_speed = random.randint(250, 1600-1), random.randint(60, 1100), 0

        if Ball.sound == None:
            Ball.sound = load_wav('pickup.wav')
            Ball.sound.set_volume(62)

    def get_bb(self):
        return  self.cx - 10, self.cy - 10, self.cx + 10, self.cy + 10

    def set_background(self, bg):
        self.bg = bg

    def collideFuction(self):
        Ball.sound.play()

    def draw(self):
        self.image.draw(self.cx, self.cy)
        draw_rectangle(*self.get_bb())

    def update(self):
        self.y -= self.fall_speed * game_framework.frame_time

        self.cx, self.cy = self.x - self.bg.window_left, self.y - self.bg.window_bottom




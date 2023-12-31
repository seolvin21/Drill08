from pico2d import *
import random


class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

    def update(self): pass


class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = random.randint(0, 7)
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)


class Ball:
    def __init__(self):
        self.x, self.y = random.randint(50, 750), 599
        self.size = random.choice([21, 41])
        if self.size == 21:
            self.image = load_image('ball21x21.png')
            self.ground = 58
        else:
            self.image = load_image('ball41x41.png')
            self.ground = 71
        self.speed = random.randint(5, 20)

    def update(self):
        if self.y > self.ground:
            self.y -= self.speed
        if self.y <= self.ground:
            self.y = self.ground

    def draw(self):
        self.image.clip_draw(0, 0, self.size, self.size, self.x, self.y)


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


def reset_world():
    global running
    global grass
    global team
    global balls

    running = True
    grass = Grass()
    team = [Boy() for i in range(11)]
    balls = [Ball() for i in range(20)]


def update_world():
    grass.update()
    for boy in team:
        boy.update()
    for ball in balls:
        ball.update()
    pass


def render_world():
    clear_canvas()
    grass.draw()
    for boy in team:
        boy.draw()
    for ball in balls:
        ball.draw()
    update_canvas()


open_canvas()

reset_world()

while running:
    handle_events()
    update_world()
    render_world()
    delay(0.05)

close_canvas()
#commit
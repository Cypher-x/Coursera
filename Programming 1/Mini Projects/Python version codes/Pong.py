# Implementation of classic arcade game Pong
try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
LEFT = False
RIGHT = True

#Player 1 paddle specifications
pad_x = [3,3]
pad_y = [150, 150+PAD_HEIGHT]
pad_vel = [0,0]
pad_acc = 0

#Player 2 paddle specifications
pad2_x = [WIDTH-5,WIDTH-5]
pad2_y = [150, 150+PAD_HEIGHT]
pad2_vel = [0,0]
pad2_acc = 0

#The Ball specifications
ball_pos = [WIDTH / 2, HEIGHT / 2]
ball_vel = [float(random.choice((-2,-1,1,2))), float(random.choice((-2,-1,1,2)))] #placeholder

#Time delay
count_sec = 2

#Score keeping
score1= 0
score2 = 0

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
#direction
#IMPORTANT: spawns toward the player that won the last point!
def spawn_left():
    global ball_pos, ball_vel, count_sec
    timer.stop()
    count_sec = 2
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    ball_vel = [random.randrange(-2,0), random.randrange(-2,0)]

def spawn_right():
    global ball_pos, ball_vel, count_sec
    timer.stop()
    count_sec = 2
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    ball_vel = [random.randrange(1,3), random.randrange(1,3)] #placeholder

#===== Define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2
    global ball_pos, ball_vel, count_sec
    score1 = 0
    score2 = 0
    timer.stop()
    count_sec = 2
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    ball_vel = [float(random.choice((-2,-1,1,2))), float(random.choice((-2,-1,1,2)))]

def time_delay():
    global count_sec
    count_sec += -1

def ball_delay():
    global ball_pos, ball_vel
    ball_pos[0] = WIDTH / 2
    ball_pos[1] = HEIGHT / 2
    ball_vel[0] = 0
    ball_vel[1] = 0

#======= Define Draw handler
def draw(canvas):
    global score1, score2, pad_y, pad_vel, pad2_y, pad2_vel, ball_pos, ball_vel, count_sec
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")

   # Player 1 paddle
    pad_y[0] += pad_vel[0]
    pad_y[1] += pad_vel[1]
    canvas.draw_line([pad_x[0], pad_y[0]],[pad_x[1], pad_y[1]], PAD_WIDTH, "White")
    y_top = (pad_y[0] <= 1)
    y_bot = (pad_y[1] >= HEIGHT - 1)
    if y_top == True:
        pad_vel[0] = 0
        pad_vel[1] = 0
        pad_y[0] = 1
        pad_y[1] = PAD_HEIGHT + 1
    elif y_bot == True:
        pad_vel[0] = 0
        pad_vel[1] = 0
        pad_y[0] = HEIGHT - PAD_HEIGHT - 1
        pad_y[1] = HEIGHT - 1
    else:
        pad_y[0] += pad_vel[0]
        pad_y[1] += pad_vel[1]

   # Player 2 paddle
    pad2_y[0] += pad2_vel[0]
    pad2_y[1] += pad2_vel[1]
    canvas.draw_line([pad2_x[0], pad2_y[0]],[pad2_x[1], pad2_y[1]], PAD_WIDTH, "White")
    y2_top = (pad2_y[0] <= 1)
    y2_bot = (pad2_y[1] >= HEIGHT - 1)
    if y2_top == True:
        pad2_vel[0] = 0
        pad2_vel[1] = 0
        pad2_y[0] = 1
        pad2_y[1] = PAD_HEIGHT + 1
    elif y2_bot == True:
        pad2_vel[0] = 0
        pad2_vel[1] = 0
        pad2_y[0] = HEIGHT - PAD_HEIGHT - 1
        pad2_y[1] = HEIGHT - 1
    else:
        pad2_y[0] += pad2_vel[0]
        pad2_y[1] += pad2_vel[1]

    #Ball mechanics
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]

    collide_pad1 = (ball_pos[0] <= pad_x[0]+BALL_RADIUS) and (
        ball_pos[1] >= pad_y[0]-5) and (
        ball_pos[1] <= pad_y[1]+5)

    collide_pad2 = (ball_pos[0] >= pad2_x[0]-BALL_RADIUS) and (
        ball_pos[1] >= pad2_y[0]-5) and (
        ball_pos[1] <= pad2_y[1]+5)

    gutter_1 = (collide_pad1 == False) and (
        ball_pos[0] <= BALL_RADIUS)

    gutter_2 = (collide_pad2 == False) and (
        ball_pos[0] >= (WIDTH - 1)-BALL_RADIUS)

    if collide_pad1 == True:
        ball_vel[0] = - ball_vel[0]*1.2
    elif collide_pad2 == True:
        ball_vel[0] = - ball_vel[0]*1.2
    elif ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
    elif ball_pos[1] >= (HEIGHT - 1)-BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
    elif gutter_1 == True:
        score2 += 1
        timer.start()
        while count_sec > 0:
            ball_delay()
        while count_sec <= 0:
            spawn_right()
    elif gutter_2 == True:
        score1 +=1
        timer.start()
        while count_sec > 0:
            ball_delay()
        while count_sec <= 0:
            spawn_left()

    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "White", "White")

    #draw scores
    canvas.draw_text(str(score1), [(WIDTH/2)-70, 60], 60, "White")
    canvas.draw_text(str(score2), [(WIDTH/2)+45, 60], 60, "White")


#==========Key Functions
def keydown(key):
    global pad_acc
    global pad2_acc
    pad_acc += 5
    pad2_acc += 5
    if (key == simplegui.KEY_MAP["s"]):
        pad_vel[0] += pad_acc
        pad_vel[1] += pad_acc
    elif (key == simplegui.KEY_MAP["w"]):
        pad_vel[0] -= pad_acc
        pad_vel[1] -= pad_acc
    elif (key == simplegui.KEY_MAP["down"]):
        pad2_vel[0] += pad2_acc
        pad2_vel[1] += pad2_acc
    elif (key == simplegui.KEY_MAP["up"]):
        pad2_vel[0] -= pad2_acc
        pad2_vel[1] -= pad2_acc
    else:
        pad_acc = 0
        pad2_acc = 0
        pad_vel[0] = 0
        pad_vel[1] = 0
        pad2_vel[0] = 0
        pad2_vel[1] = 0

def keyup(key):
    global pad_acc
    global pad2_acc
    pad_acc = 0
    pad2_acc = 0
    if key == simplegui.KEY_MAP["s"]:
        pad_vel[0] = pad_acc
        pad_vel[1] = pad_acc
    elif key == simplegui.KEY_MAP["w"]:
        pad_vel[0] = pad_acc
        pad_vel[1] = pad_acc
    elif key == simplegui.KEY_MAP["down"]:
        pad2_vel[0] = pad2_acc
        pad2_vel[1] = pad2_acc
    elif key == simplegui.KEY_MAP["up"]:
        pad2_vel[0] = pad2_acc
        pad2_vel[1] = pad2_acc
    else:
        pad_acc = 0
        pad2_acc = 0
        pad_vel[0] = 0
        pad_vel[1] = 0
        pad2_vel[0] = 0
        pad2_vel[1] = 0

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
timer = simplegui.create_timer(100,time_delay)
frame.add_label("Enjoy the game! :)")
frame.add_label(" ")
frame.add_button("Reset", new_game, 200)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

# start frame
frame.start()
new_game()

# Enjoy the game!
# Yours,
# Cypher

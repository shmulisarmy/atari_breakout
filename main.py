import pygame as pg, sys

def start():
    global ball, ballspeed, ballup, ballright
    ball = pg.Rect(width/2, height/2, 20, 20)
    ballspeed = 5
    ballup = False
    ballright = True

pg.init()

width, height = 800, 600
window = pg.display.set_mode((width, height))
clock = pg.time.Clock()
paddle = pg.Rect(width/2-100, height-10, 200, 10)
ballspeed = 5
paddlespeed = 10
level = 7
bricks = [[level for i in range(10)]for i in range(4)]
start()
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT: 
            pg.quit()
            sys.exit()
    clock.tick(80)
    window.fill('black')
    key = pg.key.get_pressed()
    if key[pg.K_LEFT]:
        lkey = True
        paddle.x -= paddlespeed
    elif key[pg.K_RIGHT]:
        lkey = False
        paddle.x += paddlespeed

    if ballright: ball.x += ballspeed
    else: ball.x -= ballspeed
    if ballup: ball.y -= ballspeed
    else: ball.y += ballspeed
    for i in range(int(ballspeed)):
        ballspeed *= .99999

    if not 0 < ball.x < width:
        ballright = not ballright
        ballspeed += .2
    if ball.y <= 0:
        ballup = not ballup
        ballspeed += .2
    if ball.colliderect(paddle):
        ballup = True
        if lkey: ballright = True
        else: ballright = False
    if ball.y > height:
        start()

    pg.draw.rect(window, (255, 255, 255), paddle)
    pg.draw.circle(window, (255, 255, 255), (ball.x, ball.y), 10)
    for i, row in enumerate(bricks):
        for j, col in enumerate(row):
            brick = pg.Rect(width/len(bricks)*(j+.2), height/len(row)*(i+.4), width/(len(bricks)*2), height/(len(row)*2))
            if ball.colliderect(brick) and col != 0:
                ballup = not ballup
                bricks[i][j] = col - 1
                ballspeed += .2
            if col != 0:
                pg.draw.rect(window, (255, 255-150//col, 150//col), brick)
    pg.display.update()
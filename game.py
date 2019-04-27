import pygame, sys, math, os, sys, time

class Spaceship():

    class Point():
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def rotate(self, angle, Cx, Cy):
            newx = math.cos(math.radians(angle)) * (self.x - Cx) - math.sin(math.radians(angle)) * (self.y - Cy) + Cx
            newy = math.sin(math.radians(angle)) * (self.x - Cx) + math.cos(math.radians(angle)) * (self.y - Cy) + Cy
            self.x = newx
            self.y = newy

    def __init__(self, Cx, Cy):
        self.Cx = Cx
        self.Cy = Cy
        self.points = []
        self.bullets = []
        self.angle = 0
        self.r = 25

        # define points on equilateral triangle
        self.CX = self.r * math.cos(0) + self.Cx
        self.CY = self.r * math.sin(0) + self.Cy
        self.BX = self.r * math.cos((1/3)*(2*math.pi)) + self.Cx
        self.BY = self.r * math.sin((1/3)*(2*math.pi)) + self.Cy
        self.AX = self.r * math.cos((2/3)*(2*math.pi)) + self.Cx
        self.AY = self.r * math.sin((2/3)*(2*math.pi)) + self.Cy

        # add points to object
        self.points.append(self.Point(self.CX, self.CY))
        self.points.append(self.Point(self.BX, self.BY))
        self.points.append(self.Point(self.Cx, self.Cy))
        self.points.append(self.Point(self.AX, self.AY))

        self.pointList = []
        for point in self.points:
            self.pointList.append((point.x, point.y))
        
        self.triangle = pygame.draw.polygon(canvas, (200, 200, 200), self.pointList)

    def draw(self, canvas):
        i = 0
        for point in self.points:
            self.pointList[i] = (point.x, point.y)
            i = i + 1
        pygame.draw.polygon(canvas, (200, 200, 200), self.pointList)

    def rotateShip(self, direction, canvas):
        if direction == "left":
            self.angle = -.5
            self.rotatePoints()
            self.draw(canvas)
        if direction == "right":
            self.angle = .5
            self.rotatePoints()
            self.draw(canvas)

    def rotatePoints(self):
        for point in self.points:
            point.rotate(self.angle, self.Cx, self.Cy)
    
    def shoot(self):
        tipx = self.pointList[0][0]
        tipy = self.pointList[0][1]
        diffx = (320 - tipx)*-1
        diffy = (320 - tipy)*-1
        self.bullets.append([(tipx, tipy), (tipx + diffx, tipy + diffy), (diffx, diffy)])

    def updateBullets(self, speed):
        index = 0
        for bullet in self.bullets:
            diffx = bullet[2][0]
            diffy = bullet[2][1]

            x1 = bullet[0][0]
            y1 = bullet[0][1]
            bullet[0] = (x1 + diffx/speed, y1 + diffy/speed)

            x2 = bullet[1][0]
            y2 = bullet[1][1]
            bullet[1] = (x2 + diffx/speed, y2 + diffy/speed)
            pygame.draw.aaline(canvas, (200,200,200), bullet[0], bullet[1])

            # if bullets go off screen, stop drawing them
            if not (x1 > 0 and x1 < 640 and y1 > 0 and y1 < 640):
                print(self.bullets[index])
                del self.bullets[index]
            index = index + 1

pygame.init()

size = width, height = 640, 640
black = 0, 0, 0

canvas = pygame.display.set_mode(size)
ship = Spaceship(width/2, height/2)
lastTime = 0
interval = 200
bulletSpeed = 50

while True:

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        # print("left key pressed")
        ship.rotateShip("left", canvas)
    if keys[pygame.K_RIGHT]:
        # print("right key pressed")
        ship.rotateShip("right", canvas)
    if keys[pygame.K_SPACE] and (int(round(time.time() * 1000)) > lastTime + interval):
        lastTime = int(round(time.time() * 1000))
        # print("space key pressed")
        ship.shoot()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    canvas.fill(black)
    ship.draw(canvas)
    ship.updateBullets(bulletSpeed)

    pygame.display.flip()
    # canvas.blit(ball, ballrect)
    # pygame.display.flip()

    pygame.display.update()

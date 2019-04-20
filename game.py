import pygame, sys, math

class Spaceship():

    class Point():
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def rotate(self, angle, Cx, Cy):
            print(angle)
            print("old x = ", (320 - self.x))
            print("old y = ", (320 - self.y))
            newx = math.cos(math.radians(angle)) * (self.x - Cx) - math.sin(math.radians(angle)) * (self.y - Cy) + Cx
            newy = math.sin(math.radians(angle)) * (self.x - Cx) + math.cos(math.radians(angle)) * (self.y - Cy) + Cy
            self.x = newx
            self.y = newy
            
            print("new x = ", (320 - newx))
            print("new y = ", (320 - newy))

    def __init__(self, Cx, Cy):
        self.Cx = Cx
        self.Cy = Cy
        self.angle = 0
        self.points = []
        self.r = 15

        # define points on equilateral triangle
        self.CX = Cx
        self.CY = Cy - self.r
        self.BX = self.CX * math.cos(math.radians(120)) - (self.CY * math.sin(math.radians(120)))
        self.BY = self.CX * math.sin(math.radians(120)) + (self.CY * math.cos(math.radians(120)))
        self.AX = self.CX * math.cos(math.radians(240)) - (self.CY * math.sin(math.radians(240)))
        self.AY = self.CX * math.sin(math.radians(240)) + (self.CY * math.cos(math.radians(240)))

        print("CX = ", self.CX)
        print("CY = ", self.CY)
        print("BX = ", self.BX)
        print("BY = ", self.BY)

        # add points to object
        self.points.append(self.Point(self.CX, self.CY))
        self.points.append(self.Point(self.BX, self.BY))
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
            self.angle -= 1 % 360
            self.rotatePoints()
            self.draw(canvas)
        if direction == "right":
            self.angle += 1 % 360
            self.rotatePoints()
            self.draw(canvas)

    def rotatePoints(self):
        for point in self.points:
            point.rotate(self.angle, self.Cx, self.Cy)

    def radius(self, x, y):
        newX = x - self.Cx
        newY = y - self.Cy
        return math.sqrt((newX * newX) + (newY * newY))



pygame.init()

size = width, height = 640, 640
speed = [2, 2]
black = 0, 0, 0

canvas = pygame.display.set_mode(size)
ship = Spaceship(width/2, height/2)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                ship.rotateShip("left", canvas)
            if event.key == pygame.K_RIGHT:
                ship.rotateShip("right", canvas)


    canvas.fill(black)
    ship.draw(canvas)
    pygame.display.flip()
    # canvas.blit(ball, ballrect)
    # pygame.display.flip()

    pygame.display.update()

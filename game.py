import pygame, sys, math

class Spaceship():

    class Point():
        def __init__(self, x, y, r):
            self.x = x
            self.y = y
            self.r = r

        # def rotate(self):

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angle = 0
        self.points = []
        
        self.points.append(self.Point(self.x, self.y-15, self.radius(self.x, self.y-15, self.x, self.y)))
        self.points.append(self.Point(self.x-15, self.y+15, self.radius(self.x-15, self.y+15, self.x, self.y)))
        self.points.append(self.Point(self.x+15, self.y+15, self.radius(self.x+15, self.y+15, self.x, self.y)))

        self.pointList = []
        for point in self.points:
            self.pointList.append((point.x, point.y))
        self.triangle = pygame.draw.polygon(canvas, (200, 200, 200), self.pointList)

    def draw(self, canvas):
        pygame.draw.polygon(canvas, (200, 200, 200), self.pointList)

    def rotateShip(self, direction, canvas):
        if direction == "left":
            self.angle += 1 % 360
            self.rotatePoints()
            self.draw(canvas)
        if direction == "right":
            self.angle -= 1 % 360
            self.rotatePoints()
            self.draw(canvas)

    def rotatePoints(self):
        for point in self.points:
            print(point.r)

    def radius(self, x, y, Cx, Cy):
        newX = x - Cx
        newY = y - Cy
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

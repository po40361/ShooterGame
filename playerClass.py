import pygame

walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]

walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]


class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.consecJumps = 0
        self.isJump = False
        self.jumpCount = 10
        self.left = False #check if moving left
        self.right = False #check if moving right
        self.walkCount = 0
        self.standing = True
        self.hitbox = (self.x + 20, self.y + 13, 26, 50) #defines hitbox as a class attribute
        self.health = 9

    def draw(self, win):
        if self.walkCount + 1 >= 54 : #sprite file only has 9 images and we're doing 3 frames per movement. so 27 or else it will have an index error
            self.walkCount = 0


        if not(self.standing):
            if man.left:
                win.blit(walkLeft[self.walkCount // 6], (self.x, self.y)) #uses above list 'walkleft', which is a list of images. prints the image at index walkcount//3
                self.walkCount += 1

            elif man.right:
                win.blit(walkRight[self.walkCount // 6], (self.x, self.y)) #same as above but for walking right
                self.walkCount += 1

        else:
            if self.right:          #makes it so whatever direction player was facing when moving will be the same direction they're facing when they stop
                win.blit(walkRight[0], (self.x, self.y))
            else:
                win.blit(walkLeft[0], (self.x, self.y))

        self.hitbox = (self.x + 20, self.y + 13, 26, 50) #updates hitbox coords

        if self.health > 0:
            pygame.draw.rect(win, (169,169,169), (self.hitbox[0]-13, self.hitbox[1] - 20, 53 , 10))
            pygame.draw.rect(win, (255, 0, 0), (self.hitbox[0]-13, self.hitbox[1] - 20, 53 - ((53/9) * (9 - self.health)), 10))
        else:
            pygame.draw.rect(win, (169,169,169), (self.hitbox[0]-13, self.hitbox[1] - 20, 53 , 10))

        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2) #draws hitbox

    def hit(self): #what happens when player is hit

        if self.health > 0:
            self.health = self.health - 0.5
        else:
            self.health = 0
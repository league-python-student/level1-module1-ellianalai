
def setup():
 
    pass
    # 1. Use the size function to set the size of your sketch
    size(475,500)
    # 2. Create 2 global variables for the background and the frog
    # using the loadImage("frog.png") function. For example:
    global bg, frog, frog_x, frog_y, hi
    hi = Car(20,100,150,20)
    frog_x = 290
    frog_y = 120
    
    bg = loadImage("froggerBackground.png")
    frog = loadImage("frog.png")
    # 3. Use the resize method to set the size of the background variable
    # to the width and height of the sketch. Resize the frog to an
    # appropriate size.
    bg.resize(475,500)
    frog.resize(20,25)
def draw():
    pass
    # 4. Use the background function to draw the background
    intersect()
    background(bg)
    image(frog,frog_x,frog_y)
    # 5. Use the image function to draw the frog.
    # Run the program and check the background and frog are displayed.
    
    hi.draw()
    hi.update()
def intersect():
    global frog_x,frog_y
    if frog_x + frog.width >hi.x and frog_x <hi.x +hi.length and frog_y+frog.height>hi.y and frog_y <hi.y +hi.length:
        frog_x = 200
        frog_y = 120
    # 6. Create global frog_x and frog_y variables in the setup function
    # and use them when drawing the frog. You will also have to put the
    # following in the draw function:
    # global frog_x, frog_y
   
    # 7. Use the Car class below to create a global car object in the
    # setup function and call the update and draw functions here.
    
    # 8. Create an intersects method that checks whether the frog collides
    # with the car. If there's a collision, move the frog back to the starting
    # point.
    
    # 9. Create more car objects of different lengths, speed, and size


def keyPressed():
    global frog_x, frog_y
    
    if key == CODED:
        if keyCode == UP:
            frog_y -= 5
        if ketCode == DOWN:
            frog_y+= 5
        if keyCode == Left:
            frog_x -= 5
        if keyCode == Right:
            frog_x += 5
            


class Car:
    def __init__(self, x, y, length, speed):
        self.x = x
        self.y = y
        self.length = length
        self.speed = speed
        
        self.car_image = loadImage("carRight.png")
        if self.speed < 0:
            self.car_image = loadImage("carLeft.png")
        
        self.car_image.resize(self.length, self.length / 3)
        
    def draw(self):
        image(self.car_image, self.x, self.y)
    
    def update(self):
        self.x += self.speed
        
        if self.x > width:
            self.x = -self.length
            
        if self.x < -self.length:
            self.x = width

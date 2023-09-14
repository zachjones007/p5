def setup():
    size(500, 500)
    global grid
    grid = loadImage('grid.png')

def draw():
    background(255)
    image(grid, 0, 0)
    noFill()
    strokeWeight(3)

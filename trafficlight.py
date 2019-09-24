#name: Gabi Gervasi
#marist email: Gabrielle.Gervasi1@marist.edu
#project description: creating a virtual stoplight using graphics.py

from graphics import *

def light ():
    win=GraphWin('traffic_light', 200, 150)

    rect= Rectangle (Point(30,10), Point (90, 150))
    rect.setOutline("Black")
    rect.setWidth(6)
    rect.setFill("white")
    rect.draw(win)

    red= Circle(Point(60,35),20)
    red.setFill("red")
    red.setOutline("black")
    red.setWidth(5)
    red.draw(win)

    yellow= Circle(Point(60,82),20)
    yellow.setFill("yellow")
    yellow.setOutline("black")
    yellow.setWidth(4)
    yellow.draw(win)

    green= Circle(Point(60,128),20)
    green.setFill("green")
    green.setOutline("black")
    green.setWidth(4)
    green.draw(win)
    
light()

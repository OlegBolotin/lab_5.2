from point import *
from figure import *
from turtle import *

def DrawLine (t, p1, p2):
    t.up()
    t.width(10)
    t.pencolor(1,0,0)
    t.goto(p1.get_x(), p1.get_y())
    t.down()
    t.goto(p2.get_x(), p2.get_y())


def main():
    t1Turtle()
    pA = Point(10,10)
    pB = Point(250,10)
    pC = Point(250, 300)
    pD = Point(10,300)
    rec = Figure([pA, pB, pC, pD])
    print(rec)

DrawLine(t1, pA,pB)
DrawLine(t1, pB, pC)
DrawLine(t1, pC, pD)
DrawLine(t1,pD, pA)

a = input()


def isInRectangle(fig, px):
    pts = fig.get_points()
    pA = pts[0]
    pB = pts[1]
    pC = pts[2]
    pD = pts[3]
    print("============")
    print("Наша точка")
    print(px)
    print("============")
    print("Прямоугольник")
    print(pts)

class Point:
    def __init__(s):
        x = int(input())
        y = int(input())
        x2 = int(input())
        y2 = int(input())
        s.x = x
        s.y = y
        s.x2 = x2
        s.y2 = y2
    def show(s):
        print(s.x, s.y)
    def move(s):
        s.x2 += s.x
        s.y2 += s.y
        print(s.x2, s.y2)
    def dist(s):
        d = sqrt((s.x2 - s.x)**2 + (s.y2 - s.y)**2)
        print(d)
pnt = Point()
pnt.show()
pnt.move()
pnt.dist()
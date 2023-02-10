class Shape:
    def area1(s):
        return 0
class Rectangle(Shape):
    def __init__(s):
        length = int(input())
        width = int(input())
        s.length = length
        s.width = width
    def area2(s):
        return s.length * s.width
x = Rectangle()
print(x.area1())
print(x.area2())
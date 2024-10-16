class Rectangle:
    def __init__(self,width,height):
        self._width=width
        self._height=height
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self,width):
        if width <= 0:
            raise ValueError('Wight must be positive')
        else:
            self._width = width
    @property
    def height(self):
        return self._height
    @height.setter
    def height(self,height):
        if height<=0:
            raise ValueError('Height must be positive')
        else:
            self._height=height
    def area(self):
        return 2*(self._width+self._height)
    def __str__(self):
        return 'Rectangle (wight={0},height={1})'.format(self._width,self._height)
    def __repr__(self):
        return 'Rectangle({0},{1})'.format(self._width,self._height)
r1=Rectangle(10,20)
print(r1)
print(r1.width)
r1.width=100
print(r1.width)
r1.height=-150
print(r1.height)



from base import Base


class Rectangle(Base):
    """
    Rectangle class inheriting from base class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        # Call the __init__ method of the base class
        super().__init__(id)  # constructor of parent class

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, new_width):
        self.__width = new_width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, new_height):
        self.__height = new_height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, new_x):
        self.__height = new_x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, new_y):
        self.__height = new_y

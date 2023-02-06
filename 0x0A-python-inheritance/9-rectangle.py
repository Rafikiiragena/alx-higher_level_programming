#!/usr/bin/python3


"""
creating a class Rectangle
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    class Rectangle inheriting BaseGeometry
    """

    def __init__(self, width, height):
        """
        function for class
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__height = height
        self.__width = width

    def area(self):
        """
        calculating the area of the Rectangle
        """
        return self.__height * self.__width

    def __str__(self):
        """
        returning the size of the Rectangle
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

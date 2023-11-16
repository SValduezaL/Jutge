import math
from yogi import read

def area_rectangle(length: float, width: float) -> float:
    """ Returns the area of a rectangle.
        Args:
            length (float): The length of the rectangle.
            width (float): The width of the rectangle.
    """
    return length * width

def area_circle(radius: float) -> float:
    """ Returns the area of a circle.
        Args:
            radius (float): The radius of the circle.
    """
    return math.pi * radius ** 2

def main() -> None:
    n = read(int)
    for _i in range(n):
        figure = read(str)
        if figure == "rectangle":
            length = read(float)
            width = read(float)
            print('{:.6f}'.format(area_rectangle(length, width)))
        elif figure == "circle":
            radius = read(float)
            print('{:.6f}'.format(area_circle(radius)))

if __name__ == "__main__":
    main()

import math
from yogi import scan

def sin_and_cos(angle: float) -> None:
    ''' Returns the sin and cos of the given angle in degrees.
            Args:
                angle (float): The angle in degrees.
    '''
    print (f'{math.sin(math.radians(angle)):.6f} {math.cos(math.radians(angle)):.6f}')

def main() -> None:
    angle = scan(float)
    while angle != None:
        sin_and_cos(angle)
        angle = scan(float)

if __name__ == "__main__":
    main()
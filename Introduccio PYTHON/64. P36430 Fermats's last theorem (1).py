import math
from yogi import read


def get_z_2_Fermat_last_theorem(a: int, b: int, c: int, d: int) -> None:
    for x in range(a, b + 1):
        for y in range(c, d + 1):    
            z_square = (x**2) + (y**2)
            z = math.sqrt(z_square)
            if z % 1 == 0:
                z = int(z)
                return print(f'{x}^2 + {y}^2 = {z}^2')
    return print('No solution!')


def main() -> None:
    
    a, b, c, d = read(int), read(int), read(int), read(int)
    
    get_z_2_Fermat_last_theorem(a, b, c, d)


if __name__ == "__main__":
    main()

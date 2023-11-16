from yogi import scan


def Tower_of_Hanoi(n: int, ori: str = "A", aux: str = "B", dst: str = "C") -> None:
    """
    The Towers of Hanoi is a game that consists of three rods and n disks of different sizes that can slide onto any rod.
    The game starts with the disks stacked in order of size on the left rod, the biggest disk at the bottom.
    The aim of the game is to move all the disks from the left rod (A) to the right rod (C), using the middle rod (B) as auxiliary.
    All the moves have to follow these rules:
        - In each step, only one disk can be moved.
        - Each move consists of taking the upper disk from one of the rods and sliding it onto another rod,
            over the other disks that may already be present on that rod.
        - No disk can be placed over a smaller disk.
    This program prints the movements to solve  the game with the minimum movements.
        Args:
            n(int): Number of disks in the first rod.
            ori(): The name of the first rod ("A" by default).
            aux(): The name of the second rod ("B" by default).
            dst(): The name of the third rod ("C" by default).
        Preconditions:
            1 < n < 18
    """
    if n > 0:
        Tower_of_Hanoi(n - 1, ori, dst, aux)
        print(f"{ori} => {dst}")
        Tower_of_Hanoi(n - 1, aux, ori, dst)
    return


def main():
    n = scan(int)
    while n != None:
        Tower_of_Hanoi(n, "A", "B", "C")
        n = scan(int)

if __name__ == "__main__":
    main()

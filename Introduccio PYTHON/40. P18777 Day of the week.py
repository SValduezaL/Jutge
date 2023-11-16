import math

def day_of_the_week(d: int, m: int, y: int) -> str:
    """
    Given a valid day d, month m and year y, returns its day of the week (from Monday to Sunday)
    Prec: Tha parameter y is between 1800 and 9999, both included. And the date must be valid.
    """

    m -= 2
    if m <= 0:
        m += 12
        y -= 1
    c = y // 100
    a = y % 100
    
    f = ((2.6*m) - 0.2) + d + a + (a//4) + (c//4) - (2*c)
    
    if math.floor(f)%7 == 0:
        return "Sunday"
    elif math.floor(f)%7 == 1:
        return "Monday"
    elif math.floor(f)%7 == 2:
        return "Tuesday"
    elif math.floor(f)%7 == 3:
        return "Wednesday"
    elif math.floor(f)%7 == 4:
        return "Thursday"
    elif math.floor(f)%7 == 5:
        return "Friday"
    elif math.floor(f)%7 == 6:
        return "Saturday"
    else:
        return ""


def main() -> None:
    print(day_of_the_week(28, 2, 2000))
    print(day_of_the_week(29, 2, 2000))
    print(day_of_the_week(1, 3, 2000))


if __name__ == "__main__":
    main()

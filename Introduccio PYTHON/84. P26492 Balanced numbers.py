def is_balanced(n: int) -> bool:
    """
    It says whether a number is balanced or not.
    That is to say whether the sum of the digits in even positions
    is equal to the sum of the digits in odd positions.
        Arguments:
            n(int): number to be checked
        Returns:
            1 is the number is balanced, 0 otherwise
    """
    number = str(n)
    
    evens = [0]
    for i in range(0,len(number),2):
        num = int(number[i])
        evens.append(num)
    evens_sum = sum(evens)
    
    odds = [0]
    for i in range(1,len(number),2):
        odds.append(int(number[i]))
    odds_sum = sum(odds)
    
    if evens_sum == odds_sum:
        return True
    else:
        return False
from yogi import tokens


def evaluate_parenthesized_expression(s: str) -> int:
    """
    Returns the result of evaluating the given parenthesized expression.
        Args:
            s (str): The parenthesized expression to evaluate.
        Returns:
            int: The value of the parenthesized expression.
    """
    if s[-1].isdigit():
        return int(s[-1])
    else:
        parenthesis = 1
        for i in range(1, len(s)):
            if s[i] == '(':
                parenthesis += 1
            elif s[i] == ')':
                parenthesis -= 1
            elif s[i] in ('+', '-', '*') and parenthesis == 1:
                operator = s[i]
                left_value = evaluate_parenthesized_expression(s[1:i])
                if s[i+1].isdigit():
                    right_value = int(s[i+1])
                else:
                    right_value = evaluate_parenthesized_expression(s[i+1:len(s)-1])
                if operator == '+':
                    return left_value + right_value
                elif operator == '-':
                    return left_value - right_value
                elif operator == '*':
                    return left_value * right_value


def main() -> None:
    expression = str()
    for token in tokens(str):
        expression += token
    
    print(evaluate_parenthesized_expression(expression))


if __name__ == "__main__":
    main()

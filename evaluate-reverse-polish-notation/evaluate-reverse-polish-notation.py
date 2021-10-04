class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "/": lambda a, b: int(a/b),
            "*": lambda a, b: a * b
        }
        current_position = 0
        while len(tokens) > 1:
            while tokens[current_position] not in "+-*/":
                current_position += 1
            operator = tokens[current_position]
            number_1 = int(tokens[current_position - 2])
            number_2 = int(tokens[current_position - 1])
            
            operation = operations[operator]
            tokens[current_position] = operation(number_1, number_2)
            tokens.pop(current_position - 2)
            tokens.pop(current_position - 2)
            current_position -= 1
        return tokens[0]
            
import re

def arithmeticExpressionCheck(expression: str) -> str:
    expression = expression.replace(" ", "")
    valid_symbols = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "+", "-", "*", "/", "(", ")"}
    if any(char not in valid_symbols for char in expression):
        return "invalid"
    if re.search(r'\d{2,}', expression):
        return "invalid"
    if re.search(r'[\+\-\*/]{2,}', expression):
        return "invalid"
 
    stack = []
    for char in expression:
        if char == "(":
            stack.append(char)
        elif char == ")":
            if not stack:
                return "invalid"
            stack.pop()
    if stack:
        return "invalid"
    try:
        compiled_code = compile(expression, "<string>", "eval")
        for node in compiled_code.co_names:
            if node not in valid_symbols:
                return "invalid"
        return "valid"
    except:
        return "invalid"

expression = input()
print(arithmeticExpressionCheck(expression))

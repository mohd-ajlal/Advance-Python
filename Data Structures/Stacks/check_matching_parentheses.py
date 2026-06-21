def check_matching_parentheses(s):
    stack = []

    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False
            stack.pop()

    return len(stack) == 0

# Example usage
input_string = "((()))"
print(check_matching_parentheses(input_string))  # Output: True

print(check_matching_parentheses("(()"))  # Output: False
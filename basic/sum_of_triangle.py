# Without using the formula n(n+1)/2, we can calculate the sum of the first n natural numbers using recursion. The function triangle(num) calculates the sum of the first num natural numbers, and the function square(num) calculates the sum of the first num triangular numbers, which is equivalent to the sum of the first num natural numbers squared.


def triangle(num):
    if num == 1:
        return num
    return num + triangle(num - 1)

def square(num):
    if num == 0:
        return 0
    return triangle(num) + triangle(num - 1)

print(square(4)) 
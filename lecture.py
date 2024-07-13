# def factorial(n):
#     print("Виклик функції factorial з n = ", n)
#     if n == 1:
#         print("Базовий випадок n = 1 ")
#         return 1
#     else:
#         result = n * factorial(n-1)
#         print("Повернення результату для n = ", n, ":", result)
#         return result

# factorial(5)


# Ітеррація
# def sum_iter(n):
#     result = 0
#     for i in range(1, n + 1):
#         result += i
#         print(i)
#     return result

# print(sum_iter(5))

# Рекурсія
# def sum_rec(n):
#     print("start:", n)
#     if n == 0:
#         return 0
#     else:
#         result = n + sum_rec(n - 1)
#         print("result for : ",n)
#         return result
    
# print(sum_rec(5))

# Ітерація по Фібоначчі
# def fibonacci_iterative(n):
#     if n <= 1:
#         return n
#     a, b = 0, 1
#     for _ in range(2, n + 1):
#         print("до : ", a, b)
#         a, b = b, a + b
#         print("после :", b)
#     return b

# print(fibonacci_iterative(10))

# рекурсія по Фібоначчі
# def fibonacci_recursive(n):
#     if n <= 1:
#         return n
#     else:
#         print("n :", n)
#         result = fibonacci_recursive(n -1) + fibonacci_recursive(n - 2)
#         print(result)
#         return result
    
# print(fibonacci_recursive(5))


# Мемоїзація
# def fibonacci_memo(n, memo={}):
#     if n in memo:
#         return memo[n]
#     if n <= 1:
#         return n
#     else:
#         value = fibonacci_memo(n-1, memo) + fibonacci_memo(n-2, memo)
    
#         memo[n] = value
#         print(value)
#         return value

# print(fibonacci_memo(7))

# Використання декоратору lru_cache
# from functools import lru_cache

# @lru_cache(maxsize=None)
# def fibonacci(n):
#     if n <= 1:
#         return n
#     else:
#         print("n :", n)
#         result = fibonacci(n -1) + fibonacci(n - 2)
#         print(result)
#         return result
    
# print(fibonacci(5))   


# import matplotlib.pyplot as plt
# import matplotlib.patches as patches

# def draw_triangle(vertices, ax):
#     triangle = patches.Polygon(vertices, fill=False, edgecolor='black')
#     ax.add_patch(triangle)

# def midpoint(point1, point2):
#     return [(point1[0] + point2[0]) / 2, (point1[1] + point2[1]) / 2]

# def sierpinski(vertices, level, ax):
#     draw_triangle(vertices, ax)
#     if level > 0:
#         sierpinski([vertices[0], midpoint(vertices[0], vertices[1]), midpoint(vertices[0], vertices[2])], level-1, ax)
#         sierpinski([vertices[1], midpoint(vertices[0], vertices[1]), midpoint(vertices[1], vertices[2])], level-1, ax)
#         sierpinski([vertices[2], midpoint(vertices[2], vertices[1]), midpoint(vertices[0], vertices[2])], level-1, ax)

# def main():
#     fig, ax = plt.subplots()
#     ax.set_aspect('equal')
#     ax.set_axis_off()
#     vertices = [[0, 0], [0.5, 0.75], [1, 0]]
#     sierpinski(vertices, 3, ax)
#     plt.show()

# main()

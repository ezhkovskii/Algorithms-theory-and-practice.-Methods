'''Нахождение числа Фибоначчи'''

'''
Cо списком
'''
def fib1(n):
    F = [0, 1]
    for i in range(2, n+1):
        F.append( F[i-1] + F[i-2])
    return F[n]

'''
Рекурсия
'''
def fib2(n):
    if n <= 1:
        return n
    else:
        return fib2(n-1) + fib2(n-2)

'''
Без списка
'''
def fib3(n):
    prev, current = 0, 1
    for i in range(n-1):
        prev, current = current, prev + current
    return current

def main():
    n = int(input())
    print(fib3(n))


if __name__ == "__main__":
    main()

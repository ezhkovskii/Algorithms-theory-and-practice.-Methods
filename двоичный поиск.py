'''
Задание:
В первой строке даны целое число n
и массив A[1…n] из n различных натуральных чисел,в порядке возрастания,
во второй — целое число k и k натуральных чисел b1,…,bk​.
Для каждого i от 1 до k необходимо вывести индекс 1≤j≤n,
для которого A[j]=bi​, или −1, если такого j нет.
'''
'''
Пример:
Ввод
5 1 5 8 12 13
5 8 1 23 1 11
Вывод
3 1 -1 1 -1
'''
def binary_search(A, b):
    l, r = 0, len(A)-1
    while(l<=r):
        m = (l + r)//2
        if(A[m] == b):
            return m+1
        elif(A[m] > b):
            r = m - 1
        else:
            l = m + 1
    return -1

def main():
    sort_array = list(map(int, input().split()))
    b = list(map(int, input().split()))
    del sort_array[0]
    for i in range(b[0]):
        print(binary_search(sort_array, b[i+1]), end = ' ')


if __name__ == "__main__":
    main()

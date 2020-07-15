'''
Задание:
Первая строка содержит количество предметов n и вместимость рюкзака W.
Каждая из следующих n строк задаёт стоимость c и объём w предмета (n, W, c, w​ — целые числа).
Выведите максимальную стоимость частей предметов (от каждого предмета можно отделить любую часть, стоимость и объём при этом пропорционально уменьшатся),
помещающихся в данный рюкзак, с точностью не менее трёх знаков после запятой.
'''

'''
Алгоритм:
Сортируем предметы по удельной стоимости c/w;
Проходим по сортированному списку;
Берем по максимуму текущий предмет;
Возвращаем решение.
'''
def knapsack(things, capacity):
    ans = 0.000
    sort_things = sorted(things, key = sort_unit_cost, reverse = True)
    for i in sort_things:
        if i[1] <= capacity:
            ans += i[0]
            capacity -= i[1]
        else:
            ans += i[0] * (capacity/i[1])
            break
    return '{:.3f}'.format(ans)
           
def sort_unit_cost(x):
    return x[2]

def main():
    n, W = map(int, input().split())
    things = []
    for i in range(n):
        c, w = map(int, input().split())
        things.append([c, w, c/w])
    print(knapsack(things.copy(), W))


if __name__ == "__main__":
    main()

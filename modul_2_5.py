# Функции
def get_matrix(n, m, value):
    matrix = []
    for i in range(n):  # функция возвращает последовательность чисел (n=4,n=5,n=6)
        matrix.append([])  # добавляет в конец списка элемент
        for j in range(m):
            matrix[i].append(value)

    return matrix  # команда прекращает работу функции


variant1 = get_matrix(4, 1, 7)
variant2 = get_matrix(5, 2, 8)
variant3 = get_matrix(6, 3, 9)

print(variant1)
print(variant2)
print(variant3)



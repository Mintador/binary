def binary(array, target):
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = (low + high) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return None

def sort_array(array):
    for i in range(len(array)):
        for j in range(i, len(array)):
            if array[j] < array[i]:
                array[i], array[j] = array[j], array[i]
    return array

sequence = input("Введите последовательность чисел через пробел: ")
try:
    sequence_list = [int(num) for num in sequence.split()]
except ValueError:
    print("Ошибка: введены некорректные данные")
    exit()

number = input("Введите ваше число: ")
try:
    target_number = int(number)
except ValueError:
    print("Ошибка: введено некорректное число")
    exit()

sorted_list = sort_array(sequence_list)
target_index = binary(sorted_list, target_number)

if target_index is None:
    print("Число не найдено")
else:
    for i in range(target_index, len(sorted_list)):
        if sorted_list[i] >= target_number:
            print("Номер позиции элемента, который меньше введенного числа, а следующий за ним больше или равен этому числу:", i)
            break
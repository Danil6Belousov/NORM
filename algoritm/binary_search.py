def binary_search(list, item): # В переменных low и high хранятся границы той
    low = 0                    # части списка, в которой выполняется поиск
    high = len(list)-1

    while low <= high:         # Пока эта часть не сократится до одного элемента
        mid = (low + high)     # проверим средний элемент
        guess = list[mid]
        if guess == item:      #Значение найдено
            return mid
        if guess > item:       #Много
            high = mid - 1
        else:                  #Мало
            low = mid + 1
    return None                #Значение не существует

my_list = [1, 3, 5, 7, 9]      #Тестируем функцию

print(binary_search(my_list, 3))
print(binary_search(my_list, -1))

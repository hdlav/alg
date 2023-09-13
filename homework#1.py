def heapify(arr, n, i):
    largest = i
    left_child = 2 * i + 1
    right_child = 2 * i + 2

    if left_child < n and arr[left_child] > arr[largest]:
        largest = left_child

    if right_child < n and arr[right_child] > arr[largest]:
        largest = right_child

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # Построение max-кучи (пирамиды)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Извлечение элементов из кучи и сортировка
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Обмен текущего элемента с корнем кучи
        heapify(arr, i, 0)

# Пример использования
if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6, 7]
    print("Исходный массив:")
    print(arr)
    heap_sort(arr)
    print("Отсортированный массив:")
    print(arr)

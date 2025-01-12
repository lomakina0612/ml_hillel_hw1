
import numpy as np

print('\n========== Task 1 ==============\n')
#todo 1 Створіть масив NumPy із 10 випадкових цілих чисел. Виконайте наступні операції:
# Знайдіть середнє, медіану та стандартне відхилення масиву.
# Замініть всі парні числа у масиві на 0.

arr = np.random.randint(0,100,10)

print(arr)

mean_value = np.mean(arr)

median_value = np.median(arr)

std_value = np.std(arr)

print("\nMean value:", mean_value)
print("Median:", median_value)
print("Standard deviation:", std_value)

arr[arr % 2 == 0] = 0

print("\nArray after replacing even numbers with 0:")
print(arr)


print('\n========== Task 2 ==============\n')
#todo 2 Індексація та зрізка в NumPy
# Створіть 2D масив NumPy (матрицю) розміром (3, 3) із випадковими цілими числами.
# Виведіть перший рядок матриці.
# Виведіть останній стовпець матриці.
# Виведіть діагональні елементи матриці.

arr = np.random.randint(0, 10, (3, 3))

print("Initial matrix:")
print(arr)

print("\nFirst row of the matrix:")
print(arr[0])

print("\nLast column of the matrix:")
print(arr[:, -1])

print("\nDiagonal elements of the matrix:")
print(arr.diagonal())


print('\n========== Task 3 ==============\n')
#todo Створіть 2D масив NumPy розміром (3, 3) та 1D масив розміром (3,). 
# Використайте broadcasting для додавання 1D масиву до кожного рядка 2D масиву.

arr_2d = np.random.randint(0, 10, (3, 3))
arr_1d = np.random.randint(0, 10, 3)

print("Initial 2D array:")
print(arr_2d)

print("\nInitial 1D array:")
print(arr_1d)

# Use broadcasting to add the 1D array to each row of the 2D array
result = arr_2d + arr_1d

print("\nResult of broadcasting:")
print(result)


print('\n========== Task 4 ==============\n')
#todo Створіть 2D масив NumPy розміром (5, 5) з випадковими цілими числами.
# Знайдіть та виведіть всі унікальні елементи у масиві.
# виведіть всі рядки, сума елементів у яких більша за певне значення. (значення оберіть самі)

arr_2d = np.random.randint(0, 10, (5, 5))

print("Initial 2D array:")
print(arr)

unique_elements = np.unique(arr)
print("\nUnique elements in the array:")
print(unique_elements)

row_sums = np.sum(arr, axis=1)

threshold = 15

print(f"\nRows with sum greater than {threshold}:")
print(arr[row_sums > threshold])


print('\n========== Task 5 ==============\n')
#todo Створіть 1D масив NumPy, що містить цілі числа від 1 до 20 (включно).
# Використайте оператор shape, щоб перетворити 1D масив у 2D масив розміром (4, 5). 
# Переконайтеся, що отриманий перетворений масив має бажаний розмір.


arr_1d = np.arange(1, 21)   # цілі числа від 1 до 20 (включно)

print("Initial 1D array:")
print(arr_1d)

arr_1d.shape = (4, 5)   # перетворити 1D масив у 2D масив розміром (4, 5)

print("\nReshaped 2D array (4x5):")
print(arr_1d)

# Verify the shape
print("\nShape of the reshaped array:")
print(arr_1d.shape)


print('\n========== pandas ==============\n')
#todo 
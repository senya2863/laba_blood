import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Чтение данных из файла 40mm.txt
with open("40mm.txt", 'r') as file:
    list40 = file.readlines()
list40 = [float(line.strip()) for line in list40]

# Чтение данных из файла 80mm.txt
with open("80mm.txt", 'r') as file:
    list80 = file.readlines()
list80 = [float(line.strip()) for line in list80]

# Чтение данных из файла 120mm.txt
with open("120mm.txt", 'r') as file:
    list120 = file.readlines()
list120 = [float(line.strip()) for line in list120]

# Чтение данных из файла 160mm.txt
with open("160mm.txt", 'r') as file:
    list160 = file.readlines()
list160 = [float(line.strip()) for line in list160]

# Вычисляем средние значения для каждого списка
mean_values = [np.mean(list40), np.mean(list80), np.mean(list120), np.mean(list160)]

# Оси x - индексы списков
x = np.array([40, 80, 120, 160])

# Определяем модель функции для аппроксимации (линейная функция)
def linear_model(x, a, b):
    return a * x + b

# Используем curve_fit для аппроксимации данных
params, covariance = curve_fit(linear_model, x, mean_values)

# Извлекаем параметры модели
a, b = params

# Строим график
plt.plot(x, mean_values, 'bo', label='Измерения')
plt.plot(x, linear_model(x, a, b), 'r-', label=f'Калибровка P={1/a:.2f}N - 7.24')

# Подписываем график
plt.title("Калибровочный график зависимости показаний АЦП от давления")
plt.xlabel("Давление (мм рт.ст.)")
plt.ylabel("Отсчёты АЦП")
plt.legend()
plt.grid(True, which='major', linestyle='-', color='black', alpha=0.5)  # Основная сетка
plt.minorticks_on()  # Включаем дополнительные деления на осях
plt.grid(True, which='minor', linestyle='--', color='gray', alpha=0.7)  # Дополнительная сетка

# Показываем график
plt.show()


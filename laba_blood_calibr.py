import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

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
x = [40, 80, 120, 160]

# Строим график
plt.plot(x, mean_values, 'bo', label='Измерения')

# Апроксимируем данные линейной регрессией
slope, intercept, r_value, p_value, std_err = stats.linregress(x, mean_values)
plt.plot(x, slope * np.array(x) + intercept, 'r-', label=f'Калиюровка (y={slope:.2f}x + {intercept:.2f})')

# Подписываем график
plt.title("Калибровочный график зависимости показаний АЦП от давления")
plt.xlabel("Давлениех (мм рт.ст.)")
plt.ylabel("Отсчёты АЦП")
plt.legend()
plt.grid(True, which='major', linestyle='-', color='black', alpha=0.5)  # Основная и дополнительная сетка
plt.minorticks_on()  # Включаем дополнительные деления на осях
plt.grid(True, which='minor', linestyle='--', color='gray', alpha=0.7)  # Дополнительная сетка (тонкая линия)


# Показываем график
plt.show()


import numpy as np
import matplotlib.pyplot as plt

# Чтение данных из файла quite.txt
with open("angry.txt", 'r') as file:
    x_values = file.readlines()

# Преобразуем данные из строкового формата в числовой (float)
x_values = [float(line.strip()) for line in x_values]

# Вычисляем давление по формуле p = 9.55x + 116
p_values = [0.10 * x - 7.24 for x in x_values]

# Время для каждого измерения (предполагается равномерное распределение на 60 секунд)
time = np.linspace(0, 60, len(p_values))

# Построение графика
plt.figure(figsize=(10, 6))
plt.plot(time, p_values, label='Давление', color='purple')

# Настройки графика
plt.title("Зависимость давления от времени в возбуждённом состоянии")
plt.xlabel("Время с")
plt.ylabel("Давление мм рт.ст.")
plt.grid(True, which='major', linestyle='-', color='black', alpha=0.5)  # Основная и дополнительная сетка
plt.minorticks_on()  # Включаем дополнительные деления на осях
plt.grid(True, which='minor', linestyle='--', color='gray', alpha=0.7)  # Дополнительная сетка (тонкая линия)
plt.scatter(6, 142.5, color='y', label='systole', zorder=5)
plt.scatter(38.1, 91, color='green', label='diastole', zorder=5)

plt.legend()

# Отображаем график
plt.show()

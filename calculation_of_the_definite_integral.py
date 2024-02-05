import matplotlib.pyplot as plt
import scipy.integrate as spi
import numpy as np


# Визначення функції та межі інтегрування
def f(x):
    return x**2

a = 0  # Нижня межа
b = 2  # Верхня межа

# Створення діапазону значень для x
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

# Створення графіка
fig, ax = plt.subplots()

# Малювання функції
ax.plot(x, y, "r", linewidth=2)

# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color="gray", alpha=0.3)

# Налаштування графіка
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel("x")
ax.set_ylabel("f(x)")

# Додавання меж інтегрування та назви графіка
ax.axvline(x=a, color="gray", linestyle="--")
ax.axvline(x=b, color="gray", linestyle="--")
ax.set_title("Графік інтегрування f(x) = x^2 від " + str(a) + " до " + str(b))
plt.grid()
plt.show()


# Метод Монте-Карло
def monte_carlo_integration(num_points, a, b, f):
    # Генеруємо випадкові значення x на інтервалі [a, b]
    random_x = np.random.uniform(a, b, num_points)

    # Генеруємо випадкові значення y на інтервалі [0, f(b)]
    random_y = np.random.uniform(0, f(b), num_points)

    # Кількість точок, які знаходяться під кривою (вище або на кривій)
    points_under_curve = sum(random_y <= f(random_x))

    # Відношення кількості точок під кривою до загальної кількості точок
    area_ratio = points_under_curve / num_points

    # Загальна площа області під кривою на інтервалі [a, b]
    total_area = (b - a) * f(b)

    # Наближене значення визначеного інтегралу
    integral_value = total_area * area_ratio

    return integral_value


# Перевірка правилності розрахунку за допомогою функції quad
result, error = spi.quad(f, a, b)
print("Інтеграл: ", result)

# Обчислення інтеграла за допомогою методу Монте-Карло
points_list = [10, 100, 1000, 10000, 20000, 50000, 100000, 1000000]

print("Обчислення інтеграла (метод Монте-Карло): ")
for points in points_list:
    print(f"Кількість точок: {points}, інтеграл: {monte_carlo_integration(points, a, b, f)}")
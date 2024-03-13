import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as spi


# Визначення функції та межі інтегрування
def f(x):
    return x ** 2


def main():
    a = 0  # Нижня межа
    b = 2  # Верхня межа

    # Створення діапазону значень для x
    x = np.linspace(-0.5, 2.5, 400)
    y = f(x)

    # Створення графіка
    fig, ax = plt.subplots()

    # Малювання функції
    ax.plot(x, y, 'r', linewidth=2)

    # Заповнення області під кривою
    ix = np.linspace(a, b)
    iy = f(ix)
    ax.fill_between(ix, iy, color='gray', alpha=0.3)

    # Налаштування графіка
    ax.set_xlim([x[0], x[-1]])
    ax.set_ylim([0, max(y) + 0.1])
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')

    # Додавання меж інтегрування та назви графіка
    ax.axvline(x=a, color='gray', linestyle='--')
    ax.axvline(x=b, color='gray', linestyle='--')
    ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
    plt.grid()

    # Виконання обчислення інтеграла за допомогою методу Монте-Карло
    N = 10000  # Кількість випробувань
    x_random = np.random.uniform(a, b, N)
    y_random = np.random.uniform(0, f(b), N)

    under_curve = y_random < f(x_random)
    above_curve = np.invert(under_curve)

    # Малювання точок
    ax.scatter(x_random[under_curve], y_random[under_curve], color='blue', marker='.', alpha=0.3)
    ax.scatter(x_random[above_curve], y_random[above_curve], color='red', marker='.', alpha=0.3)

    plt.show()

    # Обчислення інтеграла методом Монте-Карло
    monte_carlo_integral = (b - a) * f(b) * np.sum(under_curve) / N

    # Аналітичне обчислення інтеграла для порівняння
    analytical_integral, _ = spi.quad(f, a, b)

    print("Метод Монте-Карло: ", monte_carlo_integral)
    print("Аналітичний метод: ", analytical_integral)


if __name__ == "__main__":
    main()

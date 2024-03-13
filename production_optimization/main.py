from pulp import *


def main():
    # Ініціалізація моделі
    model = LpProblem("Maximize_Production", LpMaximize)

    # Змінні рішень
    lemonade = LpVariable("Lemonade", lowBound=0, cat='Integer')
    fruit_juice = LpVariable("Fruit_Juice", lowBound=0, cat='Integer')

    # Функція цілі: максимізувати загальну кількість продукції
    model += lemonade + fruit_juice

    # Обмеження за ресурсами
    model += 2*lemonade + fruit_juice <= 100, "Water_Limit"
    model += lemonade <= 50, "Sugar_Limit"
    model += lemonade <= 30, "Lemon_Juice_Limit"
    model += 2*fruit_juice <= 40, "Fruit_Puree_Limit"

    # Розв'язання моделі
    model.solve()

    # Виведення результатів
    print("Кількість Лимонаду для виробництва:", lemonade.varValue)
    print("Кількість Фруктового соку для виробництва:", fruit_juice.varValue)
    print("Загальна кількість продуктів:", pulp.value(model.objective))


if __name__ == "__main__":
    main()

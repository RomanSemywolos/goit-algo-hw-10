import pulp

# Ініціалізація моделі
model = pulp.LpProblem("Production_Optimization", pulp.LpMaximize)

# Визначення змінних (кількість лимонаду та фруктового соку)
lemonade = pulp.LpVariable(name="Lemonade", lowBound=0, cat="Integer")
fruit_juice = pulp.LpVariable(name="FruitJuice", lowBound=0, cat="Integer")

# Функція цілі (Максимізація кількісті продуктів)
model += lemonade + fruit_juice

# Додавання обмежень
model += 2 * lemonade + fruit_juice <= 100 
model += lemonade <= 50
model += lemonade <= 30
model += 2 * fruit_juice + lemonade <= 40

# Розв'язання моделі
model.solve()

print(f"Status: {model.status}")
print(f"Optimal quantity of lemonade: {lemonade.varValue}")
print(f"Optimal quantity of fruit juice: {fruit_juice.varValue}")
print(f"Total products: {model.objective.value()}")
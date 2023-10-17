import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Reds,
    edgecolor='none', s=40)

# Назначение заголовка диаграммы и меток осей
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# Назначение размера шрифта делений на осях
plt.tick_params(axis='both', which='major', labelsize=14)

# Назначение диапазона
plt.axis([0, 1100, 0, 1100000])

plt.show()

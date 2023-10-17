import matplotlib.pyplot as plt

x_values = list(range(1, 100))
y_values = [x**3 for x in x_values]

plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.plasma,
    edgecolor='none', s=40)

# Название заголовка диаграммы и меток
plt.title("Cubed numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Cube of Value", fontsize=14)

# Назначение размера шрифта делений на осях
plt.tick_params(axis='both', which='major', labelsize=14)

# Назначение диапазона
plt.axis([0, 100, 0, 1000000])

plt.savefig('cubes_plot.png', bbox_inches='tight')
plt.show()

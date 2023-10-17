import matplotlib.pyplot as plt
from die_matplotlib import Die

die_1 = Die()
die_2 = Die()

max_result = die_1.num_sides + die_2.num_sides
x_values = list(range(2, max_result+1))
# Список с результатами бросков
results = [die_1.roll() + die_2.roll() for roll_num in range(1000)]
y_values = [results.count(values) for values in range(2, max_result+1)]

# Назначение размера области блуждания
plt.figure(dpi=128, figsize=(9,4))

plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.plasma,
    edgecolor='none', s=40)

# Название заголовка диаграммы и меток
plt.title("Results of rolling two D6 dice 1000 times", fontsize=24)
plt.xlabel("Result", fontsize=14)
plt.ylabel("Frequency of Result", fontsize=14)

# Назначение размера шрифта делений на осях
plt.tick_params(axis='both', which='major', labelsize=14)

plt.savefig('die_matplotlib_visual.png', bbox_inches='tight')
plt.show()

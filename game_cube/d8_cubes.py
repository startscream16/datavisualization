import pygal
from die import Die

# Создание кубиков двух кубиков D8
die_1 = Die(8)
die_2 = Die(8)

# Моделирование серии бросков с сохранением результатов в списке
results = []
for roll_num in range(10000000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Анализ результатов
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)
    
# Визуализация результатов
hist = pygal.Bar()

hist.title = "Results of rolling two D8 1000 times"
hist.x_labels = list(range(2, max_result+1))
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D8 + D8', frequencies)
hist.render_to_file('d8_visual.svg')

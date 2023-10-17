import csv
from datetime import datetime
from matplotlib import pyplot as plt

# Чтение дат и температурных максимумов и минимумов из файла
filename = 'death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    dates, highs, lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

# Нанесение данных на диаграмму
fig = plt.figure(dpi=128, figsize =(9,4.5))
plt.plot(dates, highs, c='red', alpha=0.5, linewidth=1)
plt.plot(dates, lows, c='blue', alpha=0.5, linewidth=1)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Форматирование диаграммы
title = "Daily high and low temperatures - 2014\nDeath Valley, CA"
plt.title(title, fontsize=16)
plt.xlabel('', fontsize=16)

fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=12)
plt.tick_params(axis='both', which='major', labelsize=10)

#Назначение диапазона для каждой оси
plt.axis([dates[0], dates[-1], 10, 120])

plt.show()

import csv
from datetime import datetime
from matplotlib import pyplot as plt

# Чтение дат и температурных максимумов и минимумов из файла
filename = 'sitka_weather_2021_full.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)
    
    dates, highs, lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[2], '%Y-%m-%d')
            high = int(row[7])
            low = int(row[8])
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
            
# Нанесение данных на диаграмму
fig = plt.figure(dpi=128, figsize= (9, 4.5))
plt.plot(dates, highs, c='red', linewidth=1, alpha=0.5)
plt.plot(dates, lows, c='blue', linewidth=1, alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Форматирование диаграммы
title = "Daily high and low temperatures - 2021\nSitka, Alaska"
plt.title(title, fontsize=12)
plt.tick_params(axis='both', which='major', labelsize=10)

fig.autofmt_xdate()
plt.ylabel("Temperature(F)", fontsize=10)
plt.xlabel('', fontsize=10)

# Назначение диапазона для каждой оси
plt.axis([dates[0], dates[-1], 10, 120])

plt.show()

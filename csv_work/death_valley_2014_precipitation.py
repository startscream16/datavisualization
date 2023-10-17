import csv
from datetime import datetime
from matplotlib import pyplot as plt

# Чтение дат и осадков
filename = 'death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    dates, precipitations = [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], '%Y-%m-%d')
            precipitation = float(row[-4])
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates.append(current_date)
            precipitations.append(precipitation)
            
# Нанесение данных на диаграмму
fig = plt.figure(dpi=128, figsize=(9, 4.5))
plt.plot(dates, precipitations, c='green', linewidth=1)

# Форматирование диаграммы
title = "Precipitation in Death Valley - 2014"
plt.title(title, fontsize=16)
plt.xlabel('', fontsize=16)

fig.autofmt_xdate()
plt.ylabel("Precipitation (Inches)", fontsize=12)
plt.tick_params(axis='both', which='major', labelsize=10)

plt.show()

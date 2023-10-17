import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Новые блуждания строятся до тех пор, пока программа остается активной
while True:
    # Построение случайного блуждания
    rw = RandomWalk(10)
    rw.get_step()
    rw.fill_walk()
    
    # Назначение размера области просмотра
    plt.figure(dpi=128, figsize=(9, 4))
    
    point_numbers = list(range(rw.num_points))
    plt.plot(rw.x_values, rw.y_values, c='pink', linewidth=0.4)
        
    # Выделение первой и последней точек
    plt.scatter(0, 0, c='green', edgecolor='none', s=25)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolor='none',
        s=25)
    
    plt.show()
    
    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break

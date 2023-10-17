import pygal
from random_walk_pygal import RandomWalk

# Построение случайного блуждания
rw = RandomWalk()
rw.get_step()
rw.fill_walk()
    
hist = pygal.Bar()
    
hist.title = "Random Walk"
hist.x_labels = rw.x_values
hist.add('Random Walk', rw.y_values)
    
hist.render_to_file('rw_visual_pygal.svg')

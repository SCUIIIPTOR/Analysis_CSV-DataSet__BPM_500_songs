import pandas as pd
from matplotlib import pyplot as plt
from collections import Counter

plt.style.use("fivethirtyeight")

data_set = pd.read_csv('Blues end.csv')
index = data_set['number']
ranges = data_set['bpm_range']

counter = Counter()
for index in ranges:
	counter.update(index.split(';'))

range_bpm = []
value = []

for item in counter.most_common(100):
	range_bpm.append(item[0])
	value.append(item[1])

range_bpm.reverse()
value.reverse()

plt.barh(
	range_bpm, value,
	linewidth=.5,
	edgecolor='black',
	color='#e85b45',
	label='Количество точек на предыдущем графике'
)

plt.legend()

plt.title('Популярность интервала значений BPM в блюзе', fontsize=25)
plt.xlabel('Количество песен в диапазоне BPM', fontsize=18)
plt.ylabel('Диапазоны BPM', fontsize=18)

plt.tight_layout()
plt.show()

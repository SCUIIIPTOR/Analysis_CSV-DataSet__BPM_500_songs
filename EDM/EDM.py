from matplotlib import pyplot as plt                   # Первый каноничный импорт
import pandas as pd                                    # Второй каноничный импорт для обработки DataSet'а

plt.style.use('fivethirtyeight')                       # Назначаем стилистику визуализации

data_set = pd.read_csv('EDM.csv')                      # Считываем данные SCV-файла с DataSet'ом
bpm = data_set['bpm']                                  # Переменная для параметра BPM в каждой строке
year = data_set['year']                                # Переменная для параметра "год релиза" в каждой строке

plt.scatter(                                           # Построение точечного графика и его настройка
	bpm, year,
	c=bpm,
	s=bpm*1.5,
	cmap='gist_heat',
	edgecolor='black',
	linewidth=.7,
	alpha=.2
)

bar = plt.colorbar(                                    # Построение шкалы BPM
			orientation='horizontal',
			shrink=0.8,
			extend='both',
			extendfrac=.1
)

bar.set_label('Шкала ударов в минуту', fontsize=18)    # Подпись шкалы

plt.title('Популярность скорости '                     # Заголовок графика
		  'исполнения в EDM', fontsize=25)

plt.xlabel('BPM', fontsize=18)                         # Ось абсцисс
plt.ylabel('Год релиза', fontsize=18)                  # Ось ординат

plt.tight_layout()                                     # Настройка параметров подзаголовков в области отображения
plt.show()                                             # Вывод на экран

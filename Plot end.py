from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')

x = ['<60', '60-80', '80-100', '100-120', '120-140', '140-160', '160-180']
y = [2, 32, 144, 119, 135, 39, 29]

plt.plot(x, y, label='BPM', c='#e85b45')

plt.xlabel('Диапазон BPM')
plt.ylabel('Количество треков')
plt.title('Сравнение всех диапазонов BPM во всех жанрах')

plt.legend()

plt.tight_layout()

plt.show()
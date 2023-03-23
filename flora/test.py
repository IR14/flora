import matplotlib.pyplot as plt
import matplotlib as mpl
import random
import numpy as np

from io import StringIO


def return_graph():
    x = np.arange(0, np.pi * 3, .1)
    y = np.sin(x)

    fig = plt.figure()
    plt.plot(x, y)

    imgdata = StringIO()
    fig.savefig(imgdata, format='svg')
    imgdata.seek(0)

    data = imgdata.getvalue()
    return data


print(mpl.get_backend())
mpl.use('TkAgg')

names = ['Орхидея', 'Фиалка', 'Фикус', 'Антриум',
         'Замиокулькас', 'Гортезия', 'Монстера',
         'Кактус', 'Алоэ', 'Пеларгония']

values = [1065.0, 170.0, 1000.0, 550.0, 960.0, 620.0, 1660.0, 400.0, 280.0, 470.0]
values2 = [0.64, 0.48, 0.48, 0.43, 0.40, 0.36, 0.35, 0.32, 0.31, 0.31]
n = len(names)

plt.figure(figsize=(16, 9), dpi=80)
all_colors = list(plt.cm.colors.cnames.keys())
random.seed(100)
c = random.choices(all_colors, k=n)

plt.bar(names, values, width=0.3, color=c)

for i, val in enumerate(zip(values, names)):
    plt.text(i, val[0], val[0],
             horizontalalignment='center',
             verticalalignment='bottom',
             fontdict={'fontweight': 500, 'size': 9})

plt.gca().set_xticklabels(names, rotation=45, horizontalalignment='right')

# X/Y label Settings
plt.ylabel('Sales (RUB ₽)', fontsize=13)
plt.yticks(fontsize=10, alpha=.7)
plt.title("Flowers' prices", fontsize=13)
plt.grid(axis='y', alpha=.3)

plt.gca().spines["top"].set_alpha(0.0)
plt.gca().spines["bottom"].set_alpha(0.5)
plt.gca().spines["right"].set_alpha(0.0)
plt.gca().spines["left"].set_alpha(0.5)

plt.show()

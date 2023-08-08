import matplotlib.pyplot as plt


# plt.style.use('_mpl-gallery')

D = [[('khol', 9.0)], [('coding', 8.0)], [('wasted', 2.0)], [('work', 8.0)], [('coding', 2.0083333333333333)], [('wasted', 9.0)], [('kol', 0.008333333333333333)], [('coding', 12.0)], [('wasted', 0.01638888888888889)], [('var', 0.0)], [('coding', 20.0)], [('wasted', 23.0)], [('life', 0.0)], [('time', 9.0)], [('ok', 0.0)]]
# print(D[i][?])
# num1 = item1 = lambda i: i[1]
# num = list(map(num1, D))

# items = [item for sublist in D for item, _ in sublist]
# num = [value for sublist in D for _, value in sublist]
# print(items, num)
#
#
# fig, ax = plt.subplots()
# ax.boxplot(num, labels=items, widths=0.7, patch_artist=True, showmeans=True, showfliers=False)
#
# plt.show()












import numpy as np
import matplotlib.pyplot as plt

D = [
    [('khol', 9.0)], [('coding', 8.0)], [('wasted', 2.0)],
    [('work', 8.0)], [('coding', 2.0083333333333333)], [('wasted', 9.0)],
    [('kol', 0.008333333333333333)], [('coding', 12.0)], [('wasted', 0.01638888888888889)],
    [('var', 0.0)], [('coding', 20.0)], [('wasted', 23.0)],
    [('life', 0.0)], [('time', 9.0)], [('ok', 0.0)]
]

# Extracting item names and numerical values from the nested lists
import matplotlib.pyplot as plt

D = [[('khol', 9.0)], [('coding', 8.0)], [('wasted', 2.0)], [('work', 8.0)], [('coding', 2.0083333333333333)], [('wasted', 9.0)], [('kol', 0.008333333333333333)], [('coding', 12.0)], [('wasted', 0.01638888888888889)], [('var', 0.0)], [('coding', 20.0)], [('wasted', 23.0)], [('life', 0.0)], [('time', 9.0)], [('ok', 0.0)]]

# Extracting item names and numerical values from the nested lists
items = [item for sublist in D for item, _ in sublist]
num = [value for sublist in D for _, value in sublist]

plt.bar(items, num)

# Adding labels and title
plt.xlabel('Items')
plt.ylabel('Values')
plt.title('Bar Chart Example')

plt.xticks(rotation=45, ha="right")

# Display the plot
plt.tight_layout()
plt.show()



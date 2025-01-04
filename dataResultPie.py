
import pandas as pd

import matplotlib.pyplot as plt

import matplotlib.gridspec as grid

data = pd.read_csv('bigdata.csv')

fig = plt.figure(figsize=(10, 7))

gs = grid.GridSpec(1, 2)

# Minors -------------------------------------------->

ResultA = 0
ResultB = 0
ResultC = 0


for set in data["Age"]:
    if set <= 18:
        ResultA += 1
    elif set >= 18 and set <= 60:
        ResultB += 1
    elif set >= 60:
        ResultC += 1
    

# plot Result _________RRR

ax0 = plt.subplot(gs[0])
ax0.pie([ResultA, ResultB, ResultC],
        labels=["Minors", "Adult", "Senior"],
        colors=["#ff0000", "#00ff00", "#0000ff"],
        autopct='%1.1f%%', startangle=90)

ax0.set_title("Covid-19 Infected Status Distribution")

t0 = plt.subplot(gs[1])

t0data = [
    ["Covid-19 Infected STATUS", "COUNT"],
    ["Minors", ResultA],
    ["Adult", ResultB],
    ["Senior", ResultC]
]

t0.axis('off')
table = t0.table(cellText=t0data[1:], colLabels=t0data[0], loc="center", cellLoc="center")
for (row, col), cell in table.get_celld().items():
    if row == 0:  # Column index for "Values"
        cell.set_facecolor("#FFDDC1")


plt.tight_layout()

plt.show()
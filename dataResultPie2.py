
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
ResultD = 0
ResultE = 0
ResultG = 0
ResultH = 0


for set in data["HealthStatus"]:
    if set == "DIED":
        ResultA += 1
    elif set == "RECOVERED":
        ResultB += 1
    elif set == "ASYMPTOMATIC":
        ResultC += 1
    elif set == "MILD":
        ResultD += 1
    elif set == "MODERATE":
        ResultE += 1
    elif set == "SEVERE":
        ResultG += 1
    elif set == "CRITICAL":
        ResultH += 1

# plot Result _________RRR

ax0 = plt.subplot(gs[0])
ax0.pie([ResultA, ResultB, ResultC, ResultD, ResultE, ResultG, ResultH],
        labels=["DIED", "RECOVERED", "ASYMPTOMATIC", "MILD", "MODERATE", "SEVERE", "CRITICAL"],
        colors=["#ff0000", "#00ff00", "#0000ff"],
        autopct='%1.1f%%', startangle=90)

ax0.set_title("Covid-19 Health Status Distribution")

t0 = plt.subplot(gs[1])

t0data = [
    ["COVID-19 HEALTH STATUS", "COUNT"],
    ["DIED", ResultA],
    ["RECOVERED", ResultB],
    ["ASYMPTOMATIC", ResultC],
    ["MILD", ResultD],
    ["MODERATE", ResultE],
    ["SEVERE", ResultG],
    ["CRITICAL", ResultH],

]

t0.axis('off')
table = t0.table(cellText=t0data[1:], colLabels=t0data[0], loc="center", cellLoc="center")
for (row, col), cell in table.get_celld().items():
    if row == 0:  # Column index for "Values"
        cell.set_facecolor("#FFDDC1")


plt.tight_layout()

plt.show()
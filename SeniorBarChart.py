
import pandas as pd

import matplotlib.pyplot as plt

import matplotlib.gridspec as grid

import matplotlib.patches as mpatches

data = pd.read_csv('bigdata.csv')

fig = plt.figure(figsize=(10, 7))

gs = grid.GridSpec(1, 2)

# Senior -------------------------------------->

SeniorA = 0
SeniorB = 0
SeniorC = 0
SeniorD = 0
SeniorE = 0
SeniorG = 0
SeniorH = 0

for set, set2 in zip(data["Age"], data["HealthStatus"]):
    if set >= 60 and set2 == "DIED":
        SeniorA += 1
    elif set >= 60 and set2 == "RECOVERED":
        SeniorB += 1
    elif set >= 60 and set2 == "ASYMPTOMATIC":
        SeniorC += 1
    elif set >= 60 and set2 == "MILD":
        SeniorD += 1
    elif set >= 60 and set2 == "MODERATE":
        SeniorE += 1
    elif set >= 60 and set2 == "SEVERE":
        SeniorG += 1
    elif set >= 60 and set2 == "CRITICAL":
        SeniorH += 1

# plot Result _________RRR

ax0 = plt.subplot(gs[0])
ax0.bar(["1", "2", "3", "4", "5", "6", "7"],
        [SeniorA, SeniorB, SeniorC, SeniorD, SeniorE, SeniorG, SeniorH],
        color=["#ff0000", "#00ff00", "#0000ff", "#ffff00", "#00ffff", "#ff00ff", "#ffaa00"])

ax0.set_title("Senior Health Status Distribution (60 Years Old Above)", pad=20)
ax0.set_ylabel("Count")
ax0.set_ylim(0, 13000)

box = mpatches.Rectangle((1.05, 0.9), 0.05, 0.03, color="#ff0000", transform=ax0.transAxes, clip_on=False)
ax0.add_patch(box)
ax0.text(1.12, 0.91, "DIED", transform=ax0.transAxes, fontsize=10, va="center", ha="left")

box = mpatches.Rectangle((1.05, 0.86), 0.05, 0.03, color="#00ff00", transform=ax0.transAxes, clip_on=False)
ax0.add_patch(box)
ax0.text(1.12, 0.87, "RECOVERED", transform=ax0.transAxes, fontsize=10, va="center", ha="left")

box = mpatches.Rectangle((1.05, 0.82), 0.05, 0.03, color="#0000ff", transform=ax0.transAxes, clip_on=False)
ax0.add_patch(box)
ax0.text(1.12, 0.83, "ASYMPTOMATIC", transform=ax0.transAxes, fontsize=10, va="center", ha="left")

box = mpatches.Rectangle((1.05, 0.78), 0.05, 0.03, color="#ffff00", transform=ax0.transAxes, clip_on=False)
ax0.add_patch(box)
ax0.text(1.12, 0.79, "MILD", transform=ax0.transAxes, fontsize=10, va="center", ha="left")

box = mpatches.Rectangle((1.05, 0.74), 0.05, 0.03, color="#00ffff", transform=ax0.transAxes, clip_on=False)
ax0.add_patch(box)
ax0.text(1.12, 0.75, "MODERATE", transform=ax0.transAxes, fontsize=10, va="center", ha="left")

box = mpatches.Rectangle((1.05, 0.70), 0.05, 0.03, color="#ff00ff", transform=ax0.transAxes, clip_on=False)
ax0.add_patch(box)
ax0.text(1.12, 0.71, "SEVERE", transform=ax0.transAxes, fontsize=10, va="center", ha="left")

box = mpatches.Rectangle((1.05, 0.66), 0.05, 0.03, color="#ffaa00", transform=ax0.transAxes, clip_on=False)
ax0.add_patch(box)
ax0.text(1.12, 0.67, "CRITICAL", transform=ax0.transAxes, fontsize=10, va="center", ha="left")



t0 = plt.subplot(gs[1])

t0data = [
    ["SENIOR HEALTH STATUS", "COUNT"],
    ["DIED", SeniorA],
    ["RECOVERED", SeniorB],
    ["ASYMPTOMATIC", SeniorC],
    ["MILD", SeniorD],
    ["MODERATE", SeniorE],
    ["SEVERE", SeniorG],
    ["CRITICAL", SeniorH]
]

t0.axis('off')
table = t0.table(cellText=t0data[1:], colLabels=t0data[0], loc="center", cellLoc="center")
for (row, col), cell in table.get_celld().items():
    if row == 0:  # Column index for "Values"
        cell.set_facecolor("#FFDDC1")




plt.tight_layout()

plt.show()
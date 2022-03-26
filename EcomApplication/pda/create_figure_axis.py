import matplotlib.pyplot as plt
studentName = ['Sham', 'sagar', 'Sangram', 'Sanjay', 'Rahul']
srudentMarks = [150, 320, 315, 125, 240]

fig, ax = plt.subplot(figsize=(10, 5))
ax.plot(studentName, studentMarks)
plt.show()

import sys
sys.exit(0)
listofiqnumbers = [102, 134, 235, 320, 256, 110, 112, 134, 156, 135, 1230, 45, 132, 167, 190, 244, 343]
cat1 = 0
cat2 = 0
cat3 = 0
for i in listofiqnumbers:
    if i > 100 and i < 200:
        cat1 = cat1 + 1
    elif i > 200 and i < 300:
        cat2 = cat2 + 1
    else:
        cat3 = cat3 + 1
print("100-200:", cat1)
print("200-300", cat2)
print("300-400", cat3)

import sys

sys.exit(0)

import matplotlib.pyplot as plt

studentName = ['Sham', 'sagar', 'Sangram', 'Sanjay', 'Rahul']
srudentMarks = [150, 320, 315, 125, 240]
fig, ax = plt.subplot(figsize=(10, 5))
ax.plot(studentName, studentMarks)
plt.show()

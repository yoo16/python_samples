import matplotlib.pyplot as plt

labels = 'Apple', 'Banana', 'Cherry'
sizes = [35, 30, 35]

plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.show()
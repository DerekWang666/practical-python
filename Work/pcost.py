# pcost.py
#
# Exercise 1.27
list = []
with open('Data/portfolio.csv', 'rt') as f:
  for line in f:
    list.append(line)
    print(list)


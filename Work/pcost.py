# pcost.py

# find cwd of python instance
import os
pwd = os.getcwd()
print(pwd)

# Reading from the command line
import sys

# Exercise 1.27
def portfolio_cost(filename):
    '''
    Computes the total cost of a portfolio file (shares * price)
    '''
    
    results = []
    with open(f'{filename}', mode='rt') as file:
        next(file) # Skip the headers of the csv file
        for line in file:
            try:
                row = line.strip().split(',')
                shares = int(row[1])
                price = float(row[2])
            except ValueError:
                print(f"There was an issue with on of the values parsed in {row}")
            total = shares * price
            results.append(total)

    return f"Total Cost ${sum(results)}"

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Work/Data/portfolio.csv'


# Exercise 1.30
cost = portfolio_cost(filename)
print(cost)

# Exercise 1.28 - Other kinds of "files"

# import gzip # reads and writes gzip files

# with gzip.open('Work/Data/portfolio.csv.gz', mode='rt') as file:
#     for line in file:
#         print(line, end='')

# Exercise 1.32
import csv # Really useful module that deals with all the low level details like quotes, spaces, separators, etc.
with open("Work/Data/portfolio.csv") as f:
    total = 0
    rows = csv.reader(f)
    headers = next(rows) #skip headers
    #print(headers)
    for row in rows:
        shares = int(row[1])
        price = float(row[2])
        total += shares * price
    # print(total)

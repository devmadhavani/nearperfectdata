import csv

with open('nearperfs.csv', 'w') as nearperfs:
    writer = csv.writer(nearperfs)
    writer.writerow(('n', 'sig', 'd_1', 'd_2'))
# this line just gives us nice headers for the columns

with open('wee.csv', 'w') as wee:
    weewriter = csv.writer(wee)
    weewriter.writerow(('n', 'sig', 'd_1', 'd_2'))


def finder(x):
    for n in range(1, x + 1):
        sig = sigma(n)
        maxcheck = sig - 2 * n
        if maxcheck > 1:
            for d in range(1, int(maxcheck / 2)):
                if (n % d == 0):
                    if ((maxcheck - d) > 0 and n % (maxcheck - d) == 0 and (maxcheck - d) != d):
                        with open('nearperfs.csv', 'a') as nearperfs:
                            writer = csv.writer(nearperfs)
                            writer.writerow((n, sig, d, maxcheck - d))
    print("all done")


finder(10000)

# This just makes in into a pandas file
import pandas as pd

data = pd.read_csv("nearperfs.csv")
# data.columns=['n','sigma','d_1', 'd_2']
# this just renames the first row, but we wnat to save the first row of data, so we have it write this row waaay at the beginning
data


# this will add a column to the pandas table based on a function for each row
def test_a(rr):
    if (rr['n'] % 2 == 0):
        return true


data['even'] = data.apply(test, axis=1)
data


# This writes a NEW csv file that’s based on applying a function to the original file
def test(rr):
    if (rr['n'] % 2 == 0):
        with open('wee.csv', 'a') as wee:
            weewriter = csv.writer(wee)
            weewriter.writerow(rr)


data.apply(test, axis=1)
data
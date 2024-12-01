import pandas as pd

def qsort(inlist):
    if inlist == []: 
        return []
    else:
        pivot = inlist[0]
        lesser = qsort([x for x in inlist[1:] if x < pivot])
        greater = qsort([x for x in inlist[1:] if x >= pivot])
        return lesser + [pivot] + greater

csv_path = './day1.txt'
dataset = pd.read_csv(csv_path, sep="   ", header=None)

sorted_col1 = qsort((dataset.iloc[:,0]).to_list())
sorted_col2 = qsort(dataset.iloc[:,1].to_list())

subtracted = list()
for item1, item2 in zip(sorted_col1, sorted_col2):
    item = item1 - item2
    subtracted.append(abs(item))

print(sum(subtracted))


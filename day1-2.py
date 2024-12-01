import pandas as pd

csv_path = './day1.txt'
dataset = pd.read_csv(csv_path, sep="   ", header=None)

occurence_dict = dict()
total = 0

for item1 in dataset.iloc[:,0].to_list():
    item_occurence = 0
    if(item1 not in occurence_dict):
        for item2 in dataset.iloc[:,1].to_list():
            if(item1 == item2):
                item_occurence += 1
        occurence_dict[item1] = item_occurence
    total += item1 * occurence_dict[item1] 

print(total)
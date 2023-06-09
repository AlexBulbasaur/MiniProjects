import itertools
import matplotlib.pyplot as plt
import pandas as pd
# import numpy
import csv
from statistics import mean


def split_sequences(data, data2):
    """In column 1: Groups decreasing lines together. Groups increasing lines together.
     It save the corresponding values from column 2 based on column 1"""
    result = []
    result2 = []
    current_result = []
    current_result2 = []
    increasing = data[0] < data[1]
    for i in range(0, len(data)):
        current_result.append(data[i])
        current_result2.append(data2[i])
        if i + 1 >= len(data):
            result.append(current_result)
            result2.append(current_result2)
            break

        now_decreasing = increasing and data[i] > data[i + 1]
        now_increasing = (not increasing) and data[i] < data[i + 1]
        sequence_flipped = now_decreasing or now_increasing

        if sequence_flipped:
            result.append(current_result)
            result2.append(current_result2)
            current_result = []
            current_result2 = []
            increasing = not increasing
            continue

    return result, result2


def split_by_direction(to_split):
    """It uses the function above (split_sequences) and separates the result into all the lines that go up and all that
    go down"""
    decrease_lst = []
    increase_slt = []
    for i in range(len(to_split)):
        if i % 2 == 0:
            decrease_lst.append(to_split[i])
        else:
            increase_slt.append(to_split[i])
    return decrease_lst, increase_slt


with open('testing11.txt') as f:  #write name of file, it has to be .txt
    reader = csv.DictReader(f, delimiter='\t')
    rows = list(reader)
    # names = [i['name'] for i in rows]
    column1 = [float(i['E /V']) if i['E /V'] else 0.0 for i in rows]
    column2 = [float(i['I /mA']) if i['I /mA'] else 0.0 for i in rows]


def value_limits(data, data2):
    """picks data in first column in between certain values and collects the corresponding data to it in column 2"""
    result = []
    result2 = []
    for i in range(len(data)):
        if -1.3 <= data[i] <= -0.7:
            result.append(data[i])
            result2.append(data2[i])

    return result, result2


"""you sort them here"""
column_a = value_limits(column1, column2)[0]
column_b = value_limits(column1, column2)[1]
column1_sorted = split_sequences(column_a, column_b)[0]
column2_sorted = split_sequences(column_a, column_b)[1]
"""above is sorting happening"""
# column1_sorted = split_sequences(column1, column2)[0]
# column2_sorted = split_sequences(column1, column2)[1]
'''Above is the split_sequence function'''
decreased_lst1 = split_by_direction(column1_sorted)[0]
increased_lst1 = split_by_direction(column1_sorted)[1]

decreased_lst2 = split_by_direction(column2_sorted)[0]
increased_lst2 = split_by_direction(column2_sorted)[1]
"""Above is the split_by_direction"""

a = decreased_lst1[1:]
b = decreased_lst2[1:]
"""Above the first line is deleted to make data consistent"""
decrease_ave1 = [mean((x for x in xs if x is not None))
    for xs in itertools.zip_longest(*a)]

increase_ave1 = [mean((x for x in xs if x is not None))
    for xs in itertools.zip_longest(*increased_lst1)]

decrease_ave2 = [mean((x for x in xs if x is not None))
    for xs in itertools.zip_longest(*b)]

increase_ave2 = [mean((x for x in xs if x is not None))
    for xs in itertools.zip_longest(*increased_lst2)]
"""Above it averages all the points on  the graph"""

# plt.plot(column1, column2)
# plt.plot(increase_ave1, increase_ave2)
# plt.plot(decrease_ave1, decrease_ave2)
# plt.show()
"""Below you make a file out of the data"""
""""""
# df = pd.DataFrame(list(zip(increase_ave1, increase_ave2)),
#                   columns=['E /V', 'I /mA'])
""""""
# df = pd.DataFrame(list(zip(decrease_ave1, decrease_ave2)),
#                   columns=['E /V', 'I /mA'])
""""""


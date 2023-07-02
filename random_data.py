from pandas import DataFrame
import random

def randomIndustry():
    column_names = ['CPM', 'CPC', 'CTR', 'CPA']
    data = {}
    for col in column_names:
        data[col] = [random.randint(50, 100) for _ in range(10)]
    df = DataFrame(data)
    return df

def randomRevenue():
    column_names = ['Revenue']
    data = {}
    for col in column_names:
        data[col] = [random.randint(90, 150) for _ in range(24)]
    df = DataFrame(data)
    return df


import pandas as pd

# 从HDF5文件读取数据并转换为DataFrame对象
df = pd.read_hdf('/Users/syesw/Desktop/Easy_Alpha_Research/quant_factor_research/data/20170103-20180103-price.h5', key='price')

# 打印DataFrame对象
print(df)

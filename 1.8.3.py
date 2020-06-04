import pandas as pd 

subset_1 = my_stat.iloc[0: 10, [0, 2]]
bad_df = my_stat.index.isin([0, 4])
subset_df = my_stat[~bad_df]
subset_2 = subset_df.iloc[:, [1, 3]]

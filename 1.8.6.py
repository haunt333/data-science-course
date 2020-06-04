import pandas as pd    

my_stat = my_stat.rename(index=str, columns={'V1': 'session_value', 'V2': 'group', 'V3': 'time', 'V4': 'n_users'})

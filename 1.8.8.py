import pandas as pd

mean_session_value_data = my_stat.groupby(['group']).session_value.mean()\
    .reset_index()\
    .rename(columns={'session_value': 'mean_session_value'})

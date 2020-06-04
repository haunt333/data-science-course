import pandas as pd   

my_stat = my_stat.fillna(0)
my_stat.loc[my_stat.n_users<0, 'n_users']=my_stat.query("n_users>=0").n_users.median()

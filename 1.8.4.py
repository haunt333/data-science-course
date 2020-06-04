import pandas as pd    

subset_1 = my_stat.query("V1 > 0 & V3 == 'A'")
subset_2 = my_stat.query("V4 >= 1 | V2 != 10")

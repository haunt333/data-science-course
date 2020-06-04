import requests, zipfile, io
import pandas as pd
import numpy as np

dataset_url = 'http://stepik.org/media/attachments/course/4852/algae.csv'
r = requests.get(dataset_url)
concentrations = pd.read_csv(io.BytesIO(r.content))

mean_concentrations = concentrations.groupby(['genus']).mean()

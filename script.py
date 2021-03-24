import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import codecademylib3_seaborn
import glob

filesname = glob.glob('states*.csv')

all_data = []
for file in filesname:
  data = pd.read_csv(file)
  all_data.append(data)

us_census = pd.concat(all_data)

print(us_census.columns)
print(us_census.dtypes)

print(us_census.head())

us_census.Income = us_census['Income'].replace('[\$,]', '', regex=True)

us_census.Income = pd.to_numeric(us_census.Income)
print(us_census)

seperate = us_census.GenderPop.str.split("_")

us_census['Men'] = seperate.str.get(0)
us_census['Women'] = seperate.str.get(1)

us_census.Men = us_census['Men'].replace("M","",regex=True)
us_census.Women = us_census["Women"].replace("F","",regex = True)
us_census.Men = pd.to_numeric(us_census.Men)
us_census.Women = pd.to_numeric(us_census.Women)

print(us_census)

us_census['Women'] = us_census['Women'].fillna(us_census.TotalPop - us_census.Men)

print(us_census.Women)

duplicate=us_census.duplicated()

us_census.drop_duplicates()

plt.scatter(Women, Income)

census['Hispanic'] = census['Hispanic'].replace("%","",regex=True)
census['White'] = census['White'].replace("%","",regex=True)
census['Black'] = census['Black'].replace('%','',regex=True)
census['Asian'] = census['Asian'].replace('%','',regex=True)
census['Native']=census['Native'].replace('%','',regex=True)
census['Pacific']= census['Pacific'].replace('%','',regex=True)
census.Hispanic = pd.to_numeric(census.Hispanic)
census.White = pd.to_numeric(census.White)
census.Black = pd.to_numeric(census.Black)
census.Asian = pd.to_numeric(census.Asian)
census.Native = pd.to_numeric(census.Native)
census.Pacific= pd.to_numeric(census.Pacific)
print(census.dtypes)




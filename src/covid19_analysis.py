import pandas as pd

covid_data = './covid19/usa_county_wise.csv'
df = pd.read_csv(covid_data)

print(df.columns)
# Index(['UID', 'iso2', 'iso3', 'code3', 'FIPS', 'Admin2', 'Province_State',
#        'Country_Region', 'Lat', 'Long_', 'Combined_Key', 'Date', 'Confirmed',
#        'Deaths'],
#       dtype='object')
# print(df.shape)
# print(df.info)
# print(df.head())

# print(df.iloc[0:10, 4:15])
df_state_wise_deaths = df.groupby(df["Province_State"]).sum()
print(df_state_wise_deaths.columns)



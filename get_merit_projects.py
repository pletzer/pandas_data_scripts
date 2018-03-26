import pandas

# open the file
df = pandas.read_csv('2017-06-01-to-2018-07-31.csv')
mask = df['project class'] == 'Merit'
print(df.loc[mask].sort('core hours', ascending=False).ix[:, ['project code', 'facility', 'core hours']])



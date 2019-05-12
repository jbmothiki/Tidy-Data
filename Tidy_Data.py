import pandas as pd


# Column headers are Values, not Variable Names
pew = pd.read_csv("pew.csv")

# Each Variable forms a Column, Consolidating as 'income' and 'count'
pew_sin_var = pd.melt(pew, id_vars='religion', var_name='income', value_name='count')


# Column headers are Values, not Variable Names
billboard = pd.read_csv("billboard.csv")

# Each Variable forms a Column, Consolidating as 'week_num' and 'rating'
billboard_cons = pd.melt(billboard, id_vars=['year', 'artist', 'track', 'time', 'date.entered'],
                         var_name='week_num',
                         value_name='rating')


# Multiple Variables are stored in One Column
ebola = pd.read_csv("country_timeseries.csv")

# Each Observation forms a Row
ebola_cons = pd.melt(ebola, id_vars=['Date', 'Day'])

# Split 'Variable' Column & Creating 'Stats' 'Country'
variable_split = ebola_cons['variable'].str.split('_')

ebola_cons['stats'] = variable_split.str.get(0)
ebola_cons['country'] = variable_split.str.get(1)


# Variables are stored in both Rows & Columns
weather = pd.read_csv('weather.csv')

# Each type of observational unit forms a table
weather_melt = pd.melt(weather, id_vars=['id', 'year', 'month', 'element'],
                       var_name='day',
                       value_name='temp')

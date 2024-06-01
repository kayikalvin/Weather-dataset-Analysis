# Importing dependancies

import pandas as pd

# Importing the data to be used and turning it into a dataframe

df = pd.read_csv(r"filepath")

df

# how to analyze a dataframe

### .head()
# it shows the first n numbers of rows (default=5)

df.head()

### .shape
# Shows the total no of rows and no of columns of the dataframe

df.shape

### .index
# This attribute provides the index of the data frame

df.index

### .columns
# Shows the names of each column

df.columns

### .dtypes
# It shows the data-type of each column

df.dtypes

### .unique()
# In a column, it shows all thu unique  values.It can be applied on a single column only not on the whole dataframe

df["Weather"].unique()

### .nunique()
# It shows the total no of unique values in each column. It can be applied to a single column as well as the whole dataset

df.nunique()

### .count()
# It show the total no of non-null values in each column. It can be applied on a single column as well as on whole dataframe

df.count()

### .value_counts()
# In a column. it shows all the unique values with their count. It can be applied on only column only

df['Weather'].value_counts()

### .info()
# provides basic information about the dataframe

df.info()

# Q1. Find all the unique 'Wind Speed' values in the data-

#shows the number of unique values against each column

df.nunique() 

# this is correct since there are 34 unique values in the wind sped column as demonstrated by the 2 queries

df['Wind Speed_km/h'].nunique()

df['Wind Speed_km/h'].unique() #This is the answer

# Q2. Find the number of items when the "Weather is clear"

df.head()

#value_counts()
#it shows the unique values againt their count
df.Weather.value_counts()

#we can see the number of times the weather is clear is 1326

#filtering
#for filtering it displays all the records of when weather is clear it displays 1326 rows
df[df.Weather == 'Clear']

#groupby
#get_gruop is used to get an element in the Weather group
df.groupby('Weather').get_group('Clear')

# Q3. Find the number of times when the 'Wind Speedd was exactly 4 km/h'

df[df['Wind Speed_km/h'] == 4]
#we see the answer is 474 from the number of rows
#we also see the wind speed is 4

# Q4. Find out all the Null Values in the data

df.isnull().sum()
#shows that all the columns have 0 empty spaces

df.notnull().sum()
#shows that all columns have all their rows filled 

# Q5. Rename the column name 'Weather' of the dataframe to 'Weather Condition'

#here we use inplace = true to make the changes permanent in the dataframe

df.rename(columns= {'Weather': 'Weather Condition'}, inplace=True)

df

# Q6. What is the mean Visisbility

df['Visibility_km'].mean()

# Q7. What is the standard deviation of 'Pressure' in the data

df.Press_kPa.std()

# Q8. What is the variance of 'Relative Humidity' in this data

df['Rel Hum_%'].var()

# Q9. Find all instances when 'Snow' was recorded

df.head()

#value_counts()
df['Weather Condition'].value_counts()

#filtering
df[df['Weather Condition'] == 'Snow']

#str.contains
# we use this becauese there are other instances of snow that are nor being caught by the other queries
df[df['Weather Condition'].str.contains('Snow')]

#ANSWER
#we find that snow has been mentioned 583 times in the column
#It captures all instances of Snow

# Q10. Find all the instances where 'Wind Speed is above 24' and 'Visibility is 25'

#filtering
df[(df['Wind Speed_km/h'] > 24) & (df['Visibility_km'] == 25)]

# Q11. What is the mean value of each column against each 'Weather Condition'

#here we are writing the collumns as a list because mean can only take a maximum of 4 arguments and we had 7

columns = ('Temp_C', 'Dew Point Temp_C', 'Rel Hum_%',
       'Wind Speed_km/h', 'Visibility_km', 'Press_kPa')

df.groupby('Weather Condition').mean(columns)


# Q12. What is the Minimum and Maximun value of each column against 'Weather Condition'

columns = ('Temp_C', 'Dew Point Temp_C', 'Rel Hum_%',
       'Wind Speed_km/h', 'Visibility_km', 'Press_kPa')

df.groupby('Weather Condition').min(columns)

columns = ('Temp_C', 'Dew Point Temp_C', 'Rel Hum_%',
       'Wind Speed_km/h', 'Visibility_km', 'Press_kPa')

df.groupby('Weather Condition').max(columns)

# Q13. Show all the records when the weather is 'Fog'

#Here we are using filtering

df[df['Weather Condition'] == 'Fog']

# Q14. Find all instances where weather is 'Clear' or 'Visibility is above 40'

df.head()

df[(df['Weather Condition'] == 'Clear') | (df['Visibility_km'] > 40)]

# Q15. Find all instances when :
### 'Weather is clear' and 'Relative Humidity is greater than 50'
### or
### 'Visibility is above 40'

df.head()

df[(df['Weather Condition'] == 'Clear') & ( df['Rel Hum_%'] > 50 ) | (df['Visibility_km'] > 40)]











# Data modelling code



import pandas as pd

df = pd.read_csv(r"filepath")

df.head()

df.isnull().sum()

df.info()

#converting date/time to a date time data type
df['Date/Time'] = pd.to_datetime(df['Date/Time'])

df.info()

# convert weather column from object to string
df['Weather'] = df['Weather'].astype(pd.StringDtype())

df.info()

df.head()

# checking  out from duplicated values
df[df.duplicated()]

datetime_dim= pd.DataFrame(columns = ['date_id','date','hour', 'day', 'month', 'year','weekday'])


datetime_dim['date'] = df['Date/Time']
datetime_dim['date_id'] = datetime_dim['date'].index
datetime_dim['hour'] = df['Date/Time'].dt.hour
datetime_dim['day'] = df['Date/Time'].dt.day
datetime_dim['month'] = df['Date/Time'].dt.month
datetime_dim['year'] = df['Date/Time'].dt.year
datetime_dim['weekday'] = df['Date/Time'].dt.weekday

# Define a dictionary to map numerical weekdays to their respective names
weekday_names = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}

# Use the map function to apply the mapping to convert numerical weekdays to weekday names
datetime_dim['weekday'] = datetime_dim['weekday'].map(weekday_names)

datetime_dim.set_index('date_id', inplace=True)


datetime_dim

datetime_dim.drop(columns='datetime_id',inplace = True)
datetime_dim

weather_dim = pd.DataFrame(columns=['weather_id','weather_type'])
weather_dim

weather_dim['weather_type'] = df['Weather']
weather_dim['weather_id'] = weather_dim['weather_type'].index

weather_dim.set_index('weather_id', inplace=True)

weather_dim

columns = ['id','temp_C','dew_point_temp_C','rel hum_%','wind speed_km/h','visibility_km','date_id','weather_id']

weather_fact_table = pd.DataFrame(columns = columns )

weather_fact_table['id'] = df['Date/Time']
weather_fact_table['temp_C'] = df['Temp_C']
weather_fact_table['dew_point_temp_C'] = df['Dew Point Temp_C']
weather_fact_table['rel hum_%'] = df['Rel Hum_%']
weather_fact_table['wind Speed_km/h'] = df['Wind Speed_km/h']
weather_fact_table['visibility_km'] = df['Visibility_km']
weather_fact_table['press_kPa'] = df['Press_kPa']
weather_fact_table['date_id'] = df['Date/Time'].index
weather_fact_table['weather_Id'] = weather_dim['weather_type'].index

weather_fact_table


df.columns

weather_fact_table.drop(columns = 'wind speed_km/h',inplace =True)

weather_fact_table

weather_fact_table

weather_dim

datetime_dim


# craeting the final model table from the remodelled data

full_table = pd.DataFrame()full_table['id'] = df['Date/Time']

full_table['date'] = df['Date/Time']
full_table['date_id'] = datetime_dim['date'].index
full_table['hour'] = df['Date/Time'].dt.hour
full_table['day'] = df['Date/Time'].dt.day
full_table['month'] = df['Date/Time'].dt.month
full_table['year'] = df['Date/Time'].dt.year
full_table['weekday'] = df['Date/Time'].dt.weekday
full_table['temp_C'] = df['Temp_C']
full_table['dew_point_temp_C'] = df['Dew Point Temp_C']
full_table['rel hum_%'] = df['Rel Hum_%']
full_table['wind Speed_km/h'] = df['Wind Speed_km/h']
full_table['visibility_km'] = df['Visibility_km']
full_table['press_kPa'] = df['Press_kPa']
full_table['date_id'] = df['Date/Time'].index
full_table['weather_Id'] = weather_dim['weather_type'].index
full_table['weather_type'] = weather_dim['weather_type']
           
# Define a dictionary to map numerical weekdays to their respective names
weekday_names = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}

# Use the map function to apply the mapping to convert numerical weekdays to weekday names
full_table['weekday'] = datetime_dim['weekday'].map(weekday_names)
           
full_table


# Intro to Programming Using Python
# Author of Assignment: Yusuf Bolden (email: ajb2316@columbia.edu, slack: @Yusuf(Instructor))
# Completed by:

# Be sure to read the instructions carefully!
# For this HW assignment, we'll be working with the Dark Sky API.
# You can register for a free API key here: https://darksky.net/dev
# There's also many options for Python libraries to use to interact with it.
# I'd recommend this one to start: https://github.com/Detrous/darksky

# 1. Install the Python library using pip install darksky_weather. Then, import
# the Python Package DarkSky from darksky.api.


# 2. Get an API key for Dark Sky and save it to a file named: "dark_sky_api_key.txt".
# Then, read the API key into a variable and use it to connect to the Dark Sky API.
from darksky.api import DarkSky

dark_sky = DarkSky("f8b6e39c75c4724cb7bc9ccdcfdf7ee8")

# 3. Using the provided longitude and latitude values, get the forecast
# and assign it to a variable named forecast.

latitude = 40.8075
longitude = -73.9626

forecast = dark_sky.get_forecast(latitude, longitude)

# 4. Using the forecast variable from question, print out the current temperature, humidity, and wind speed.
# (Hint: You may want to look at the CurrentlyForecast object in forecast.py
# in the github repo: https://github.com/Detrous/darksky)

current_forecast = forecast.currently
print("The current temperature is: ", current_forecast.temperature)
print("The current humidty is: ", current_forecast.humidity)
print("The current wind speed is: ", current_forecast.wind_speed)

# 5. Let's get some more precise data. Still using the same forecast variable, now get the minutely
# forecast and assign it to a variable named minutely_forecast. Print out the first thing in minutely_forecast.data.
# You should see that it prints out a MinutelyForecastItem object.
# Using the definition found in forecast.py, print out the time of the first MinutelyForecastItem.

minutely_forecast = forecast.minutely
print(minutely_forecast.data[0])
print(minutely_forecast.data[0].time)

# 6. Now that we understand how the minute-by-minute information is saved,
# create a DataFrame named "minutely_df" where each row is one object from minutely_forecast.data.
# I've started the process for you by converting minutely_forecast.data into a dictionary.

time = []
precip_intensity = []
precip_intensity_error = []
precip_probability = []
precip_type = []

for forecast in minutely_forecast.data:
	time.append(forecast.time)
	precip_intensity.append(forecast.precip_intensity)
	precip_intensity_error.append(forecast.precip_intensity_error)
	precip_probability.append(forecast.precip_probability)
	precip_type.append(forecast.precip_type)

minutely_dictionary = {
	1: time,
	2: precip_intensity,
	3: precip_intensity_error,
	4: precip_probability,
	5: precip_type
}

from pandas import DataFrame
minutely_df = DataFrame.from_dict(minutely_dictionary)
print(minutely_dictionary)

# 7. If you print out the DataFrame from question 6, you'll notice that the column names are just numbers.
# Rename the columns in place so the names are: time, precip_intensity, precip_intensity_error, precip_probability, precip_type.

minutely_df.rename(columns = {1: 'time', 2: 'precip_intensity', 3: 'precip_intensity_error', 4: 'precip_probability', 5: 'precip_type'}, inplace=True)

print(minutely_df.head)

# 8. Using Seaborn, plot precip_probability on the x-axis and precip-intensity on the y-axis.
# Bonus: You might not see much because there isn't enough precipitation.
# See if you can find a location for which there is precipitation.

import seaborn as sns
sns.lineplot(x= 'precip_probability', y= 'precip_intensity', data=minutely_df)

---
# Module 10 Challenge
---
For this challenge, I am completing a climate analysis for an upcoming trip to Honolulu, Hawaii.

## Part 1: Analyze and Explore the Climate Data

In this section, I used Python and SQLAlchemy to do a basic climate analysis and explore my climate database. One of the new things I worked with was SQLAlchemy ORM queries, along with tools like automap, which detects tables in a database, and create_engine, which connects to a SQLite database. I also used func to apply aggregate functions like min, max, and average.

Overall, I still feel a bit shaky with SQL and SQLAlchemy, but I felt most comfortable working with libraries I’m more familiar with, like Pandas and Matplotlib.

### Precipitation Analysis

The most recent data in this dataset is from August 23, 2017. Looking at precipitation over the past year from that date, I noticed a distinct pattern. The bar graph I created shows highs and lows scattered randomly, which initially led me to believe that encountering precipitation on my trip would be likely.

However, after analyzing the statistical data, I saw a different story. The mean precipitation is 0.178 inches, suggesting that most rainfall is significantly less than an inch, often closer to zero. The min (0), 25% (0), and 50% (0.02) indicate that at least half the days had little to no precipitation. Even at the 75th percentile (0.13 inches), rainfall remains relatively low.

The maximum precipitation recorded was 6.7 inches, meaning there were occasional extreme rainfall events. These high values likely skewed the data and may have made the bar graph appear more rain-heavy than it actually was. The standard deviation (0.46), which is quite large compared to the mean, reinforces this variability—some days had significantly more rain than others, while many remained dry.

Initially, the graph made it seem like rain was frequent, but after breaking down the numbers, it's clear that rainfall is sporadic, with most days being dry or experiencing minimal precipitation.

### Station Analysis

For the station analysis, I started by identifying nine stations in the dataset. I then created a query to organize them by station ID and count how active they are in the database. From there, I focused on the most active station, Waihee, and calculated its lowest, highest, and average temperatures.

To my delight, the maximum recorded temperature at Waihee was 85°F, while the lowest was 51°F. Coming from Minnesota in the winter, that sounds pretty amazing! Looking at the histogram, I noticed that the most frequently recorded temperature is around 76°F—not bad at all.

What I’m really curious about now is how temperatures fluctuate throughout the year. Are there times when they dip into the 60s versus staying in the 80s? Does Waihee experience seasonal temperature changes, and if so, what does that pattern look like? That’s something I’d love to explore further.

## Part 2: Design Your Climate App

### 📌 Available API Endpoints

#### 1️⃣ Homepage (`/`)
   - Lists all available routes.  

#### 2️⃣ Precipitation Data (`/api/v1.0/precipitation`)
   - Returns the last 12 months of precipitation data.  

#### 3️⃣ Station List (`/api/v1.0/stations`)
   - Returns a list of all weather stations.  

#### 4️⃣ Temperature Observations (`/api/v1.0/tobs`)
   - Returns temperature observations for the most active station (`USC00519281`) for the past year.  

#### 5️⃣ Temperature Statistics for a Start Date (`/api/v1.0/<start>`)
   - Returns the **minimum, maximum, and average** temperatures from a specified start date onward.  

#### 6️⃣ Temperature Statistics for a Date Range (`/api/v1.0/<start>/<end>`)
   - Returns the **min, max, and avg** temperatures between two dates.  


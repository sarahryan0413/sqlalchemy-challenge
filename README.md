# 📊 SQLAlchemy Climate Analysis
For this challenge, I am completing a climate analysis for an upcoming trip to Honolulu, Hawaii.
## 🌦️ Part 1: Analyze and Explore the Climate Data
In this section, I used Python and SQLAlchemy to explore climate data and perform basic analysis. This involved SQLAlchemy ORM queries, automap (which detects tables in a database), and create_engine (which connects to a SQLite database). I also used func to apply aggregate functions like min, max, and average.  

Overall, I still feel a bit shaky with SQL and SQLAlchemy, but I felt most comfortable working with libraries I’m more familiar with, like Pandas and Matplotlib.
### 📉 Precipitation Analysis
The most recent data in this dataset is from August 23, 2017. Looking at precipitation over the past year from that date, I initially thought rainfall would be frequent, as highs and lows appeared scattered across the graph.  

However, breaking down the numbers told a different story:
- Mean precipitation: 0.178 inches
- 50% percentile: 0.02 inches (suggesting at least half of the days had little to no rainfall)
- Maximum precipitation: 6.7 inches (indicating occasional extreme rainfall events)
- Standard deviation: 0.46 (showing variability—some days had a lot of rain, while others had none)  

While the bar graph may have suggested frequent rain, this analysis revealed that rainfall was sporadic, with many dry days or minimal precipitation.

### 📍 Station Analysis
For the station analysis, I identified nine stations in the dataset and ranked them by activity. The most active station was Waihee (USC00519281), so I focused my temperature analysis there.
- Max temperature: 85°F
- Min temperature: 51°F
- Most frequent temperature: ~76°F  

Coming from Minnesota in the winter, those temperatures sound amazing! 🌴 I’d love to explore how temperatures fluctuate throughout the year—does Waihee experience seasonal changes? That’s a question I’d love to dive into next.

## 🚀 Part 2: Design Your Climate App
Now that I’ve explored the dataset, I created a Flask API to serve climate data. Below are the available API endpoints:

### 📌 Available Routes
1. Homepage (/)
   - Lists all available API routes.
2. Precipitation Data (/api/v1.0/precipitation)
   - Returns the last 12 months of precipitation data.
3. Station List (/api/v1.0/stations)
   - Returns a list of all weather stations.
4. Temperature Observations (/api/v1.0/tobs)
   - Returns temperature observations for the most active station (USC00519281) for the past year.
5. Temperature Statistics (Start Date) (/api/v1.0/<start>)
   - Returns the minimum, maximum, and average temperatures from a specified start date onward.
6. Temperature Statistics (Date Range) (/api/v1.0/<start>/<end>)
   - Returns the min, max, and avg temperatures between two dates.  

📊 Data provided by edX Boot Camps LLC for educational purposes.

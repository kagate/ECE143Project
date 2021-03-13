## Exploratory analysis of movies and TV show on different streaming platforms

### (ECE143 Final Project)
### Team Members: Katrina Agate, Shivani Athavale, Laura Becerra, Jake Daly, Jinyu Zhao

---


**Problem:** <br>
Comparing movies and tv shows available on different platforms. <br>

**Datasets:** <br>
Movies on Netflix, Prime Video, Hulu, and Disney+ (production year, target age group, ratings, platform availability) <br>
(https://www.kaggle.com/ruchi798/movies-on-netflix-prime-video-hulu-and-disney) <br>
TV shows on Netflix, Prime Video, Hulu, and Disney+ (production year, target age group, ratings, platform availability)  <br>
(https://www.kaggle.com/ruchi798/tv-shows-on-netflix-prime-video-hulu-and-disney) <br>
MovieLens 20M (for movie genre information): <br>
(https://www.kaggle.com/grouplens/movielens-20m-dataset?select=tag.csv) <br>
Prime TV shows (for tv shows genre information): <br>
(https://www.kaggle.com/nilimajauhari/amazon-prime-tv-shows) <br>
Most popular movies on IMDB over 10 year period (for list of most popular movies): <br>
(https://www.kaggle.com/PromptCloudHQ/imdb-data) <br>

**Code:** <br>
**Platform Analysis Code** <br>
To generate a subset of the plots we used in our platform analysis, run the ECE143Project.py script.  It generates numerous plots, several of which were not included in our final presentation (for time purposes). The plots generated are listed below. <br>
-Pie charts displaying the breakdown of age ratings of movies and tv shows on each platform <br>
-Pie charts showing the genre breakdown of movies and tv shows on each platform <br>
-Swarmplots showing the IMDB scores and age rating of movies and tv shows on each platform (each plotted point represents a movie on a certain streaming platform. Its y-value represents the IMDB score and its color represents the age rating) <br>
-Swarmplots showing the Rotten Tomato scores and age rating of movies and tv shows on each platform (each plotted point represents a movie on a certain streaming platform. Its y-value represents the Rotton Tomato score and its color represents the age rating) <br>
-Bar chart showing the number of movies on the 1000 most popular IMDB movies list each streaming platform contains <br>
-Stacked bar charts showing the number of movies available in different languages on each streaming platform <br>

Note: the ECE143Project.py script imports platform_plots.py, which includes the plotting functions which generate the pie charts, swarmplots, bar chart, and stacked bar charts. <br>
**Recommender System Code** <br>

**Libraries:** <br>
The ECE143Project.py file requires the following libraries: csv, numpy, collections, platform_plots <br>
The platform_plots file requires the following libraries: pandas, seaborn, matplotlib, numpy <br>

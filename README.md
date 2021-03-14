## Exploratory analysis of movies and TV show on different streaming platforms

### (ECE143 Final Project)
### Team Members: Katrina Agate, Shivani Athavale, Laura Becerra, Jake Daly, Jinyu Zhao

---
**Install Dependencies:**<br>
To install the dependencies that we used for this project, run the following commands. <br>
`pip install requirements.txt`

**Problem:** <br>
Comparing movies and tv shows available on different platforms. <br>

**Datasets:** <br>
Movies on Netflix, Prime Video, Hulu, and Disney+ (production year, target age group, ratings, platform availability) <br>
(https://www.kaggle.com/ruchi798/movies-on-netflix-prime-video-hulu-and-disney) <br>
TV shows on Netflix, Prime Video, Hulu, and Disney+ (production year, target age group, ratings, platform availability)  <br>
(https://www.kaggle.com/ruchi798/tv-shows-on-netflix-prime-video-hulu-and-disney) <br>
Most popular movies on IMDB over 10 year period (for list of most popular movies): <br>
(https://www.kaggle.com/PromptCloudHQ/imdb-data) <br>
TvMaze API (for TV shows actors, producers, language, genres) <br>
(https://github.com/yakupadakli/python-tvmaze) <br>

**Code:** <br>
**Platform Analysis Code** <br>
To generate a subset of the plots we used in our platform analysis, run the ECE143Project.py script.  It generates numerous plots, several of which were not included in our final presentation (for time purposes). The plots generated are listed below. <br>
-Pie charts displaying the breakdown of age ratings of movies and tv shows on each platform <br>
-Pie charts showing the genre breakdown of movies and tv shows on each platform <br>
-Swarmplots showing the IMDB scores and age rating of movies and tv shows on each platform (each plotted point represents a movie on a certain streaming platform. Its y-value represents the IMDB score and its color represents the age rating) <br>
-Swarmplots showing the Rotten Tomato scores and age rating of movies and tv shows on each platform (each plotted point represents a movie on a certain streaming platform. Its y-value represents the Rotton Tomato score and its color represents the age rating) <br>
-Bar chart showing the number of movies on the 1000 most popular IMDB movies list each streaming platform contains <br>
-Stacked bar charts showing the number of movies available in different languages on each streaming platform <br>
Note: the `ECE143Project.py` script imports `platform_plots.py`, which includes the plotting functions which generate the pie charts, swarmplots, bar chart, and stacked bar charts. <br>
This part of the code is also used for platform analysis however runs two different files `Stackedbarchart_year_plots.py` and `Wordcloud_description_plots.py` to generate the plots<br>
The outputs have been displayed in the FinalNotebook.ipynb jupyter notebook.<br>
-Stacked bar charts showing the year wise distribution of number of movies across all platforms<br>
-Stacked bar charts showing the year wise distribution of number of TV Shows across all platforms<br>
-Wordclouds showing the description data<br>
-The jupyter notebook 143project_plots-tvdataset_.ipynb displays the charts for TV Shows dataset:<br>
-wordclouds for platform wise producers<br>
-wordclouds for platform wise actors<br>
-Stacked bar chart for year wise distribution of TV Shows across platforms<br>
-The corresponding python files have also been included as:<br>
-wordclouds for platform wise producers : `producer_tv.py`<br>
-wordclouds for platform wise actors : `actors_wc_tv.py`  <br>
-Stacked bar chart for year wise distribution of TV Shows across platforms: Stackedbarchart_year_plots.py<br>
-The jupyter notebook 143project_plots-moviesdataset_.ipynb displays the charts for movies dataset:<br>
-wordcloud for platform wise directors<br>
-wordcloud for platform wise actors<br>
-wordcloud for movie descriptions<br>
-Stacked bar chart for year wise distribution of number of movies<br>
-The corresponding python files have also been included as:<br>
-wordcloud for platform wise directors: `director_wc.py`<br>
-wordcloud for platform wise actors: `actors_wc.py` <br>
-wordcloud for movie descriptions: `desc.py`<br>
-Stacked bar chart for year wise distribution of number of movies: `Stackedbarchart_year_plots.py`<br>
-Uses the data files TV_shows_all_features.csv, MoviesOnStreamingPlatforms_updated.csv, IMDB-Movie-Data.csv from the data folder<br>
**TV Show Data Extraction Code** <br>
To extract additional TV show data, the functions in process_TVshows.py each extract a different TV show feature for each TV show in the original Kaggle dataset from an API called TvMaze. The last function in the py file consolidates all of these extracted features into one csv file. All functions take in the original Kaggle TV show dataset titled "tv_shows.csv" <br>
-add_TVshow_decade outputs TV_shows_decade.csv --> original TV show csv with added decade column <br>
-add_TVshow_actor outputs TV_shows_actors.csv --> original TV show csv with added actors column (each entry has list of actors) <br>
-add_TVshow_producer outputs TV_shows_producers.csv --> original TV show csv with added producers column (each entry has list of executive producers) <br>
-add_TVshow_genre outputs TV_shows_genres.csv --> original TV show csv with added genres column (each entry has list of genres) <br>
-add_TVshow_language outputs TV_shows_languages.csv --> original TV show csv with added language column <br>
-consolidated_TVshow_data outputs TV_shows_all_features.csv --> original tv_shows.csv with all new columns generated in above functions <br>

**Recommender System Code** <br>
To generate the platform recommendation and peresonal portfolio, use the function called in the `FinalNotebook.ipynb`. <br>
All the helper functions are stored in `recommender/recommender_system.py` including the TF-IDF statistics generation, recommendation algorithm and personal portforlio plot generation. <br>
Note that the recommendation plot can not be seen in from the GitHub preview due to the incompatibility of plotly.

**Third-Party Modules:** <br>
The ECE143Project.py file requires the following libraries: numpy <br>
The platform_plots file requires the following libraries: pandas, seaborn, matplotlib, numpy <br>
The process_TVshows.py file requires the following: pandas, tvmaze.api which can be pulled from PyPI (pip install python-tvmaze) <br>   
The Stackedbarchart_year_plots.py file requires the following libraries: numpy, csv, collections, pandas, matplotlib, wordcloud, itertools, random<br>
The producer_tv.py file requires the following libraries: xlrd, pandas, numpy, matplotlib, os, collections, itertools, wordcloud, random<br>
The Wordcloud_description_plots.py file requires the following libraries: csv, numpy, collections, pandas, matplotlib, wordcloud, itertools, random<br>
The actors_wc_tv.py file requires the following libraries: xlrd, pandas, numpy, matplotlib, os, collections, itertools, wordcloud<br>
The director_wc.py file requires the following libraries: xlrd, pandas, numpy, matplotlib, os, collections, itertools, wordcloud<br>
The actors_wc.py file requires the following libraries: xlrd, pandas, numpy, matplotlib, os, collections, itertools, wordcloud<br>
The desc.py file requires the following libraries: xlrd, pandas, numpy, matplotlib, os, collections, itertools, wordcloud<br>



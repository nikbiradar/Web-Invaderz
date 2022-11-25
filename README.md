# Cinema A-Z(CS 251)

![Made with love in India](https://madewithlove.now.sh/in) <br>
Here, we've build a one stop user-friendly solution which will help the user by giving all the ratings, cast, category/genre, user reviews, and so on given the title of a movie. 

## Packages Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/)
```bash
pip install python
```
```bash
pip install requests
```
```bash
pip install requests-html
```
```bash
pip install bs4
```
```bash
pip install selenium
```
```bash
pip install django
```
## Database Creation
We have scraped our data, from top 500 movies on IMDB worldwide, and details about it from different websites like Metacritic and Rotten Tomatoes.
To do the same, enter the python shell inside the activated environment by using the following command
```bash
python manage.py runserver
```
We then call our scraping functions defined in extract_data.py and save.py created in the base app
In the shell type the following
```python
from base.extract_data extract *
extract_all()
```
It shall definitely consume heavy time as scraping is now an easy task for sure, and we are scraping 500 movies at once, to scrape a limited number of movies, you can manipulate the arrays in the extract(url) function by slicing it to a smaller size 

## Usage
On Windows, first activate the environment, by running the following command in the project directory where Scripts folder is present
```bash
Scripts\activate.bat
```
The above is not required for Ubuntu<br>
Now enter the Cinema folder
```bash
cd Cinema
```
To run the server
```bash
python manage.py runserver
```
Now open the url displayed on the terminal, it opens up the server on the browser. Your first see the home page, which woul display you the Top IMDB Movies, Latest Movies and Top Horror Movies. You cannot yet access the Favorite Movies, WatchList and Watched Movies pages, as you aren't signed in.<br>
Clicking on them would redirect you to the Login Page, SignUp if you are a new User. <br>
Tada! You are now ready to explore the website <br>
You can search for a movie from the Search Bar, and it will give you all possible movie suggestions for some entry.<br>
Clicking on a movie element, will take you into its own page, here you will find all the information related to the movie. You would find
* Directors, Actors and Cast
* Language and Genre
* Running Time
* Ratings from various platforms(IMDB, Metacritic and Rotten Tomatoes)
* Plot and Summary 
* Trailer and Gallery
* Additional Details(like the BoxOffice, Distributor, etc)
* User Reviews(Scraped from IMDB and Metacritic)
* Critic Reviews(Scraped from Rotten Tomatoes)
* Related Movies

You can add movies to your favorites, watchlist and if you have already watched, you can mark them watched. Based on your favorites, you will get recommendations on your home page. <br>

Happy Movie Binging!

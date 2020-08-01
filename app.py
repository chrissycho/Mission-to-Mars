# Where we will use Flask & Mongo to begin creating Robin's web app

from flask import Flask, render_template
# First line says that we'll use Falsk to render a template
from flask_pymongo import PyMongo
# Use PyMongo to interact with our Mongo database
import scraping
# Use scraping code --> we will convert from Jupyter notebook to Python

# Set up Flask
app = Flask(__name__)
# Tell Python how to connect to Mongo using PyMongo
# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)
# 1) app.config["MONGO_URI"] tells Python that our app will connect to 
# Mongo using a URI (a uniform resource identifier similar to a URL)
# 2) mongo://... is the URI we will use to connect our app to Mongo
# This URI is saying that the app can reach Mongo through our localhost server, using port 27017, using a db named "mars_app"

# Set up App Route (Visual representation route)
@app.route("/")
#@app.route("/") tells Flask what to display when we are looking at the home page, index.html
def index():
   mars = mongo.db.mars.find_one()
   return render_template("index.html", mars=mars)
# mars=...find_one() uses PyMongo to find "mars" collection in our database
    # which we will create when we convert our Jupyter scraping code to Python Script
    # also assign that path to the mars variable for use later
# return render_template("index.html" tells Flask to return an HTML template using an index.html file 
    # we will create this file after we build the Flask routes
    # , mars=mars) tells Python to use the "mars" collection in MongoDB
# This function is what links our visual representation of our work, web app, to the code that powers it

# Set up scraping route ("the button" of the web application-- the one that will scrape updated data)
@app.route("/scrape") #defines the route that Flask will be using 
def scrape(): # "/scrape" runs this function 
   mars = mongo.db.mars # assign a new variable to Mongo database
   mars_data = scraping.scrape_all() # a new variable to hold the newly scraped data-- referencing scrape_all() function in the scraping.py file
   mars.update({}, mars_data, upsert=True) # update the db with the new data 
   return "Scraping Successful!"
# .update(query_parameter, data, options) is the syntax 
    # we are inserting data into an empty JSON object with {}, 
    # use the data stored in mars_data, and 
    # upsert=True for Mongo to create a new document if it's not already there 

# Tell Flask to run 
if __name__ == "__main__":
    app.run()
    
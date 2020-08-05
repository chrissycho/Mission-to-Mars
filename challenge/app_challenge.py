# Where we will use Flask & Mongo to begin creating Robin's web app

from flask import Flask, render_template
# First line says that we'll use Falsk to render a template
from flask_pymongo import PyMongo
# Use PyMongo to interact with our Mongo database
import test

# Set up Flask
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

# Set up App Route (Visual representation route)
@app.route("/")
#@app.route("/") tells Flask what to display when we are looking at the home page, index.html
def index():
   mars = mongo.db.mars.find_one()
   return render_template("index_challenge.html", mars=mars)

# Set up scraping route ("the button" of the web application-- the one that will scrape updated data)
@app.route("/scrape") #defines the route that Flask will be using 
def scrape(): # "/scrape" runs this function 
   mars = mongo.db.mars # assign a new variable to Mongo database
   mars_data = test.scrape_all() # a new variable to hold the newly scraped data-- referencing scrape_all() function in the scraping.py file
   mars.update({}, mars_data, upsert=True) # update the db with the new data 
   return "Scraping Successful!"

# Tell Flask to run 
if __name__ == "__main__":
    app.run()
# Chrissy Cho's Mission-to-Mars
### Table of Contents
[ 1. Project Overview ](#desc)<br /> 
[ 2. Resources ](#resc)<br /> 
[ 3. Objectives ](#obj)<br /> 
[ 4. Summary ](#sum)<br /> 
[ 5. Challenge Overview ](#chal)<br /> 
[ 6. Challenge Summary ](#chalsum)<br /> 
[ 7. Challenge Findings ](#find)<br />

<a name="desc"></a>
## Project Overview
In this module, we've learned to automate scraping using Splinter and grab the data written in html to extract the information we want to put on our own Web App. 
For this process, we created scraping codes written in python, storing data into MongoDB for Flask to access, and showing the data with some styling using Bootstrap on html file. Throughout the module, we've factored the scraping codes into a few different functions so that we can scrape new data everytime the website updates their information. For the final display, we used the html with Bootstrap components to add some styling to the Web App with the newest article on Mars, summary of the article, featured image of Mars, and table of Mars' information. During running the server to access the Web Page, we had some issues displaying scraped data on the Web App. The issues will be discussed in the later section. 

<a name="resc"></a>
## Resources
- Data Source: [data.js](https://github.com/chrissycho/UFOs/blob/master/data.js), [app.js](https://github.com/chrissycho/UFOs/blob/master/static/js/app.js), [index.html](https://github.com/chrissycho/UFOs/blob/master/index.html), [style.css](https://github.com/chrissycho/UFOs/blob/master/static/css/style.css)
- Software: CSS, HTML, JavaScript, Jupyter Notebook

<a name="obj"></a>
## Objectives
- Explain the strengths and weaknesses of JavaScript “standard” and JavaScript version ES6+. 
- Describe JavaScript syntax and ideal use cases. 
- Build and deploy JavaScript functions, including built-in functions. 
- Convert JavaScript functions to arrow functions. 
- Build and deploy forEach (JavaScript for loop). 
- Create, populate, and dynamically filter a table using JavaScript and HTML.

<a name="sum"></a>
## Summary
We've completed ...

<a name="chal"></a>
## Challenge Overview
In this challenge, you will be finding a few key aspects of Oahu’s seasonal weather data. The investors want to ensure you’ve hit all of the key points before opening the surf shop.

### Challenge Objective
- Determine key statistical data about the month of June.
- Determine key statistical data about the month of December.
- Compare your findings between the month of June and December.
- Make 2 or 3 recommendations for further analysis.
- Share your findings in the Jupyter Notebook.

<a name="chalsum"></a>
## Challenge Summary
For the purpose of the challenge, we have determined minimum, average and maximum temperature of all stations in June and December throughout 2015-2017. We also examined the precipitation data on count, mean, std, min, 25%, 50%, 75%, and max precipitation across all stations in June and December through 2015-2017. We have found interesting findings (See below).

<a name="find"></a>
## Challenge Findings
1) Key Differences in Weather Between June and December
The statistical analysis on the precipitation weather data for June throughtout 2015 to 2017 suggests that the maximum precipitation goes down as the year increases. However, the average precipitation is around 0.12-0.2 in both June and December regardless of year. However, the average temperature throughout December is much lower than that of June regardless of year.

2) Recommendations for further analysis
Although looking at particular months is a great way to start investigating factors that might be affecting the business, I'd recommend investigating all of the months from January to December using a pie chart to see which month in general has higher precipitation percentage. I would also recommend using line graphs for temperatures throughout months for all the years so that we can easily visualize and compare three different years at the same time for each month. 

Most importantly, we need to further investigate on the sales of surfing equipment and ice cream of different stations as there are many factors contributing to the sales. We can start by looking at the profits for each store, highest month of sales, and location of the station. It is important to note that every piece of information is crucial only when we know what we are looking for. Along with the weather data, the sales data can help us decide where and when to open up the new surf and ice cream store. 
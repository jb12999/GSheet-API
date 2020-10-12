# GreenDeck
Question 1
Your task is to create a REST API using Python and host it locally using Docker.
You will be working on two of the most important concepts of software engineering for this task. APIs and Containerization.

We highly encourage you to read more about this if you are unaware about any of these concepts. It is fairly simple. Try to attempt this even if you are new to them.

We have a customer for which we have dump of 5000 products in JSON format. These products are sold on their E-Commerce platform. The data contains the product name, price and other information. The goal of this task is to allow the user to interact with a database of products using APIs which are available on localhost via Docker.

1) Download the CSV file or the JSON file. It is a list of ~5000 e-commerce products and its information.
2) Host the data on preferably, MongoDB or any database of your choice (SQL or No-SQL, both are fine). You can easily get a free server from MongoDB Atlas or CockroachDB.
3) We want you to create a REST API that allows the user to do basic CRUD operations on the data. You will have to use the python library of the database to perform these operations on the objects.
4) The user can Create new objects, Read the data, Update or Delete the objects in the database you selected before.
5) Dockerize your REST API application. The docker run command would deploy the REST API on localhost at a specific port. The user can then use the API endpoints to perform CRUD operations.
6) Test the endpoints using Postman or Curl and share screenshots.
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Question 2
Your task is to create a Python Library and host it on PyPi.

We highly encourage you to read more about this if you are unaware about any of these concepts. It is fairly simple. Try to attempt this even if you are new to them.

GSheets or gsheets is a small wrapper around the Google Sheets API (v4) to provide more convenient access to Google Sheets from Python scripts.
It allows you to read data from your google sheets. Go through the documentation of this library clearly and try to access your google sheets data using this library.
You can use any such library you want. There is no compulsion to use Gsheets.

So, the goal of this task is to allow the user to select a google sheet from their Google drive and plots a chart with the values on the sheet. The user should be given an option to select the column for the x-axis and the y-axis. All this should happen using the library you have created and is available via pip install .

To test if your library is working properly, we want you add this sheet to your Google Drive. It has three columns called timestamp , average_sales  and offer_price . We want the library to read this sheet and plot a chart for average_sales  (y-axis)vs. timestamp (x-axis) and save it as an image file on the local disk.

1) Your task is to write a wrapper around GSheets library and host your library on PyPi. The user should be able to install your library using the pip install command and use it to plot graphs and save the image files.
2) Understand and implement the Gsheets Library to read a sheet.
3) Create your own library that reads a sheet and plots a graph by selecting 2 columns for 2 axis.
4) Add the sheet in your own drive and read it using the library and plot  average_sales  (y-axis)vs. timestamp (x-axis).
5) Bundle the library code and host on PyPi. Hosting your own library on PyPi is extremely easy. Use this blog to host your library on PyPi.

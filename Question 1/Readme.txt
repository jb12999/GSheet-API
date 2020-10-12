GreenDeck Assignment Question 1
Firstly I created an ID on MongoAtlas and then a cluster  in Mongo nameed as cluster1. Added certain values for desktop and json file and then database access is provided for the data. Name and password is provided for the database making it fairly usable.
Installed mongoclient from pymongo and established a connection with id and password. Then i provided a name to the database and created a product inside it. I named the database as data and the collection as product. Then follwo the series of steps in start.py to get the data in our collection product.
 Mongo is established and data is added to it next step is creating a REST API provided in main.py and perform basic CRUD operations 
through it.Basic Create, read, update and delete functions are required from it. and then host this data on docker using docker run.

1) data.json contains the credentials with 5000 product data
2) start.py contains files for execution along with steps
3)mongo.txt - link for establishing connection
4) outer.txt - get mongo uri

Important Links:
1) MongoAtlas-starting - https://docs.atlas.mongodb.com/getting-started/
2) CRUD operation - https://docs.atlas.mongodb.com/data-explorer/
3) Creation and connecting to cluster - https://docs.atlas.mongodb.com/connect-to-cluster/
4) Pstman - https://www.postman.com/
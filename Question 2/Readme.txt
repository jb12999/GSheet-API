GreenDeck Assignment Question 2
First and foremost ghseets is installed .Then I logged into the Google Developers Console with the Google account whose spreadsheets I wanted to access.
Created the project and enabled the Drive API and Sheets API. Then I went to the Credentials for my project and created New credentials > OAuth client ID > of type Other.
In the list of my OAuth 2.0 client IDs click Download JSON for the Client ID you just created. Then I Saved the file as client_secrets.json in my home directory (user directory).
Then I added credentials.json form from Link (2) and and saved it in home directory. Then follow the steps as mentioned.
Run series of commands available there and the values are dumped into Spam.csv. I Ran _init_.py and at the runtime I selected columns for x axis and y-axis.
A graph will be displayed for so. Package and documentation are mentioned in link (4) and host it on pypi for using as a library.


1) Package can be called using pip install GreenDeck. 
2) The file setup.py the package is build and dependencies are passed.Name of the package is GreenDeck and find_packages() will fetch values form _init_.py.
3) The _init_.py contains graph execution with the help of pandas and matplotlib. It contains a dataframe df which reads values from Spam.csv and plots it 
4) quickstart.py file contains inbuild api to access the gdrive and fetch values for execution. It takes the values of credential.json for it.
5) gsheets.py contains google sheets commands to import values dump it into Spam.csv and excution of these values. The url contains url of csv file present in drive.
6) client_secret.json contains the Oauth 2.0 file to client_id and uri for user.
7) credentials.json contains cred for credentials in quickstart.py.
8) Spam.csv contains csv file along with 3 field values timestamp, average_sales and offer_price.

Important Links
1) ghseets 0.5.1 - https://pypi.org/project/gsheets/
2) Google sheets API v4 - https://developers.google.com/sheets/api/quickstart/python
3) Assignment csv - https://docs.google.com/spreadsheets/d/1SrZfvr2ee54r7HR1jGtAE9zHIj_Y-UzK9ok8bdwkpqc/edit#gid=0
4) Packaging and documentation - https://medium.com/little-big-engineering/lets-talk-about-python-packaging-6d84b81f1bb5
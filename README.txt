RSS Feed Classifier
---------------------
README
---------------------
Submitted By:
Name	-	RollNo	-	E-Mail
12IT16	-	Bhuvan M S	-	msbhuvanbhuvi@gmail.com
12IT33	-	Kartik Koralla	-	k.koralla@gmail.com
12IT78	-	Siddharth Jain	-	sid.j1501@gmail.com
12IT94	-	Vinay Rao D	-	vinayraod@gmail.com
---------------------
Instructions:

Dependencies:
Python 2.7
Python Packages:
	feedparser
	flask
	nltk
	nltk data
	rdflib
	sqlite3
---------------------
All codes have to be run from the 'Code folder'.
1. Running the Web App from shell, Normal Version, which categorizes news based on Ontology only: 
$python flask/rss_web_app.py

WebApp opens at: http://127.0.0.1:5050/
(If it gives Internal Server Error, restart the code.)

2. Running the Web App from shell, PLUS version, which categorizes news based on both Ontology and bag of words: 
$python flask_plus/rss_web_app.py

3. Update the database: Can be run as daemon which dynamically keeps updating (every 2 hours) the rss news feeds to the sqlite3 database and categorizes them.
$python dynamic_feed_updater.py


# RSS Feed Classifier

A TF-IDF based RSS Feed Classified to automatically categorize RSS feeds into relevent groups which can help in organizing and retreiving RSS Feeds.

Submitted By:
Name	-	RollNo  	-	E-Mail<br/><br/>
12IT16	-	Bhuvan M S	-	msbhuvanbhuvi@gmail.com<br/><br/>
12IT33	-	Kartik Koralla	-	k.koralla@gmail.com<br/><br/>
12IT78	-	Siddharth Jain	-	sid.j1501@gmail.com<br/><br/>
12IT94	-	Vinay Rao D	-	vinayraod@gmail.com<br/><br/>

Instructions:<br/><br/>

Dependencies:
Python 2.7<br/><br/>
Python Packages:<br/><br/>
	feedparser<br/><br/>
	flask<br/><br/>
	nltk<br/><br/>
	nltk data<br/><br/>
	rdflib<br/><br/>
	sqlite3<br/><br/>

All codes have to be run from the 'Code folder'.
1. Running the Web App from shell, Normal Version, which categorizes news based on Ontology only: 
$python flask/rss_web_app.py

WebApp opens at: http://127.0.0.1:5050/
(If it gives Internal Server Error, restart the code.)

2. Running the Web App from shell, PLUS version, which categorizes news based on both Ontology and bag of words: 
$python flask_plus/rss_web_app.py

3. Update the database: Can be run as daemon which dynamically keeps updating (every 2 hours) the rss news feeds to the sqlite3 database and categorizes them.
$python dynamic_feed_updater.py


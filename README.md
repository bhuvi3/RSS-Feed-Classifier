# RSS Feed Classifier

A TF-IDF based RSS Feed Classified to automatically categorize RSS feeds into relevent groups which can help in organizing and retreiving RSS Feeds.

##### Instructions:
Dependencies (python packages)
	feedparser
	flask
	nltk
	nltk data
	rdflib
	sqlite3

All codes have to be run from the 'Code folder'.
1. Running the Web App from shell, Normal Version, which categorizes news based on Ontology only: 
$python flask/rss_web_app.py

WebApp opens at: http://127.0.0.1:5050/
(If it gives Internal Server Error, restart the code.)

2. Running the Web App from shell, PLUS version, which categorizes news based on both Ontology and bag of words: 
$python flask_plus/rss_web_app.py

3. Update the database: Can be run as daemon which dynamically keeps updating (every 2 hours) the rss news feeds to the sqlite3 database and categorizes them.
$python dynamic_feed_updater.py


import sqlite3
import threading
import time
import Queue
from time import strftime
import re  #regular expression lib
from HTMLParser import HTMLParser #analyses text formatted in html
import feedparser     #To handle RSS. Parses feeds in all known formats(Atom,RDF,RSS)
import time

#HTML remover
class MLStripper(HTMLParser):  #subclass to override functionalities of methods of HTMLParser
	def __init__(self):
		self.reset()  #Reset the instance. Loose all unprocessed data.
		self.fed = [] 
	def handle_data(self, d): #function defined to handle the data.
		self.fed.append(d)
	def get_data(self):
		return ''.join(self.fed)

def strip_tags(html):
	s = MLStripper()
	s.feed(html)
	return s.get_data()

"""
THREAD_LIMIT = 20
jobs = Queue.Queue(0) #a queue "jobs" of size infinite. 
rss_to_process = Queue.Queue(THREAD_LIMIT) #a queue of size of our thread limit
#"""

DATABASE = "rss_feed_classification.sqlite"

conn = sqlite3.connect(DATABASE) #making a connection to database. Conn is the connection object that represents database now.
conn.row_factory = sqlite3.Row   #we can access rows by indices as well as names now 
c = conn.cursor()  #SQL commands executed using a cursor object

#insert initial values into feed database
c.execute('CREATE TABLE IF NOT EXISTS RSSFeeds (id INTEGER PRIMARY KEY AUTOINCREMENT, url VARCHAR(1000));')
q2 = "CREATE TABLE IF NOT EXISTS RSSEntries (entry_id INTEGER PRIMARY KEY AUTOINCREMENT, feed_id INTEGER, feed_url, title, description, date, category default 'general');"
c.execute(q2) #category attribute needed during classification.

feed_urls = open("rss_feedurls.txt")
print "\n***READING FEEDS FROM THE FOLLOWING URLS***\n"
for x in feed_urls:
	y = str(x[:-1]) #removing \n from end
	print y
	c.execute('INSERT INTO RSSFeeds(url) VALUES(?)',(y,))
feed_urls.close()
print "\n***FEED AGGREGATION STARTED***\n"

rss_feeds = c.execute('SELECT id, url FROM RSSFeeds').fetchall() #putting everything in feeds and later used to enqueue in jobs.
 
for feed in rss_feeds:
    feed_id = feed['id']
    feed_url = feed['url']
    entries = feedparser.parse(feed_url).entries
    for news_item in entries:
        """
        try:
            doSomething()
        except:
            pass
        """
        title = news_item.title
        description = ""
        try:
            description = strip_tags(news_item.description)
        except:
            pass
        #print title + '\n\t' + description + '\n'
        date = time.strftime("%Y-%m-%d %H:%M:%S")
        try:
            date = strftime("%Y-%m-%d %H:%M:%S",news_item.updated_parsed)
        except:
            pass
        c.execute('INSERT INTO RSSEntries (feed_id, feed_url, title, description, date) VALUES (?,?,?,?,?)', (feed_id, feed_url, title, description, date))
    print "Feed Entries updated for: " + feed_url
print "\nAll feeds entries aggregated from all given feed urls"

conn.commit()
conn.close()
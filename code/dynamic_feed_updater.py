import os;
import time;

while(True):
    os.system('rm rss_feed_classification.sqlite');
    os.system('rm rss_feed_classification_plus.sqlite');
    
    os.system('ipython feed_aggregator.py');
    os.system('cp rss_feed_classification.sqlite rss_feed_classification_plus.sqlite');
    
    os.system('ipython feed_categorizer.py');
    os.system('ipython feed_categorizer_plus.py');
    
    time.sleep(7200);

    



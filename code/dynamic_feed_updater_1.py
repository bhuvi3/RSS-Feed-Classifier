import os;
import time;

while(True):
    os.system('rm rss_feed_classification_temp.sqlite');
    os.system('rm rss_feed_classification_plus_temp.sqlite');
    
    os.system('ipython feed_aggregator_1.py');
    os.system('cp rss_feed_classification_temp.sqlite rss_feed_classification_plus_temp.sqlite');
    
    os.system('ipython feed_categorizer_1.py');
    os.system('ipython feed_categorizer_plus_1.py');
    
    os.system('cp rss_feed_classification_temp.sqlite rss_feed_classification.sqlite');
    os.system('cp rss_feed_classification_plus_temp.sqlite rss_feed_classification_plus.sqlite');
    
    time.sleep(7200);

    



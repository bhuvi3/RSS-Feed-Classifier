import pickle
import sqlite3
import time
from time import strftime
import re  #regular expression li
import sys
import os
import rdflib
import operator
from nltk.corpus import stopwords
from nltk.stem.porter import *

#Defining CF-IDF class with functions
class cfidf:
	def __init__(self):
		self.weighted = False
		self.documents = []
		self.corpus_dict = {}
	
	def addDocument(self, doc_name, list_of_words):
		# building a dictionary
		doc_dict = {}
		for w in list_of_words:
			doc_dict[w] = doc_dict.get(w, 0.) + 1.0
			self.corpus_dict[w] = self.corpus_dict.get(w, 0.0) + 1.0
		
		# normalizing the dictionary
		length = float(len(list_of_words))
		for k in doc_dict:
			doc_dict[k] = doc_dict[k] / length
		
		# add the normalized document to the corpus
		self.documents.append([doc_name, doc_dict])

	def similarities(self, list_of_words):
		"""Returns a list of all the [docname, similarity_score] pairs relative to a list of words."""
		
		# building the query dictionary
		query_dict = {}
		for w in list_of_words:
			query_dict[w] = query_dict.get(w, 0.0) + 1.0
		
		# normalizing the query
		length = float(len(list_of_words))
		for k in query_dict:
			query_dict[k] = query_dict[k] / length

		# computing the list of similarities
		sims = []
		for doc in self.documents:
			score = 0.0
			doc_dict = doc[1]
			for k in query_dict:
				if doc_dict.has_key(k):
					score += (query_dict[k] / self.corpus_dict[k]) + (doc_dict[k] / self.corpus_dict[k])
			sims.append([doc[0], score])
		
		return sims

#start
#acquiring the news 
def build_ontology_dict():
	with open('onto.txt', 'rb') as handle:
		onto = pickle.loads(handle.read())
	return onto

#weighted cf-idf algorithm
def weighted_CF_IDF(scores):
	title_scores = scores[0]
	description_scores = scores[1]
	weigted_scores = {}
	for concept in title_scores.keys():
		#weigted_scores[concept] = (title_scores[concept] * 1.25) + description_scores[concept]
		#weigted_scores[concept] = title_scores[concept] + (description_scores[concept] * 1.25)
		weigted_scores[concept] = title_scores[concept] + description_scores[concept]
	
	best_matched_category = max(weigted_scores.iteritems(), key=operator.itemgetter(1))[0]
	if weigted_scores[best_matched_category] == 0:
		best_matched_category = 'general'
	return best_matched_category

def get_additional_words():
    #lookup in additional word list table
    #query for words related to con then return
    add_word_dict = {}
    with open('additional_words.txt') as file_reader:
        for line in file_reader:
            split1 = line.split('|')
            category = split1[0]
            split2 = split1[1].split(',')
            add_word_dict[category] = split2		
    return add_word_dict

def preprocess_input_string(phrase):
    stemmer = PorterStemmer()
    stop = stopwords.words('english')
    phrase = re.sub('[^A-Za-z0-9 ]+', '', phrase)
    phrase = ' '.join(phrase.split())
    word_list = [i for i in phrase.split() if i not in stop]
    word_list = [stemmer.stem(word) for word in word_list]
    return word_list

#getting feed cursor from database
DATABASE = "rss_feed_classification_plus_temp.sqlite"
conn = sqlite3.connect(DATABASE)
conn.row_factory = sqlite3.Row
select_query = "SELECT ENTRY_ID,TITLE,DESCRIPTION FROM RSSEntries"
feed_cursor = conn.execute(select_query)

#Object of cfidf class
table = cfidf()
ontology = {} #key=concept, value= [list of all terms related to the concept]
ontology = build_ontology_dict()
concepts = ontology.keys()

for con in concepts:
    phrase_list = ontology[con]
    #"""
    new_row = []
    for i in phrase_list:
        if isinstance(i, (int, long, float, complex)):
            new_row.append(str(int(i)))
        else:
            new_row.append(i.encode('utf-8'))
    phrase_list = new_row
    #"""
    #table.addDocument(con, ontology[con])
    #preprocessed_word_list = input_phrase_list_preprocessor(phrase_list)
    preprocessed_word_list = []
    for phrase in phrase_list:
        preprocessed_word_list.extend(preprocess_input_string(phrase))
    #"""
    additional_word_dict = get_additional_words()
    additional_word_list = additional_word_dict[con]
    related_word_list = preprocessed_word_list + additional_word_list
    #"""
    #related_word_list = preprocessed_word_list
    table.addDocument(con, related_word_list)
    #print table
    #print con, phrase_list
#print con, phrase_list

#"""
#updating database
for row in feed_cursor:
    rss_entry_id = row[0]
    title = row[1]
    description = row[2]
    #making a list of words/terms after preprocessing the string 
    #getting cf-idf scores
    title_res = table.similarities(preprocess_input_string(title))
    description_res = table.similarities(preprocess_input_string(description))
    #print description_res
    scores = [dict(title_res), dict(description_res)]
    cur_category = weighted_CF_IDF(scores);
    #update database
    update_query = "UPDATE RSSEntries SET CATEGORY=" + "'" + str(cur_category) + "'" + " WHERE ENTRY_ID=" + str(rss_entry_id)
    #print update_query
    conn.execute(update_query)
    conn.commit()

conn.close()
#"""
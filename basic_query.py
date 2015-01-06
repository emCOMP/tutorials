# this script illustrates the basics of python, mongodb, and pymongo
# it finds the 2 tweets with hashtags and prints the tweet id and text

from pymongo import MongoClient

# this block creates the connection between python and mongodb
# we connect to the database 'sydneysiege' and the collection 'tweets'

dbclient = MongoClient('z')
mongo = dbclient['sydneysiege']
db = mongo['tweets']

# use our mongo connection to find 2 documents where the counts.hashtags field
# is > 0 and save to the variable called 'data'

data = db.find({'counts.hashtags':1}).limit(2)

# iterate through  the documents from our mongo query. print the tweet id and
# the tweet text

for x in data:
    print x['id'],x['text']

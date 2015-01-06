# this script illustrates the basics of python, mongodb, and pymongo
# it finds the 10 most common hashtags and writes it to a file along with the number
# of occurrences.  it will take a while to run.

from collections import Counter
from pymongo import MongoClient

# this block creates the connection between python and mongodb
# we connect to the database 'sydneysiege' and the collection 'tweets'

dbclient = MongoClient('z')
mongo = dbclient['sydneysiege']
db = mongo['tweets']

# create a new file named 'test_document.csv'
# write a header with columns 'hashtag name' and 'count'

f = open('test_document.csv','w')
f.write('hashtag_name,count\n')

# use our mongo connection to find 100 documents where the counts.hashtags field
# is > 0 and save to the variable called 'data'
# in the terminal this would look like db.tweets.find({'counts.hashtags':{$gt:0}})

data = db.find({
    'counts.hashtags':{
        '$gt':0
    }
}).limit(100)

print 'finished query'

# Create a new counter object called.  This is a good basic way of counting in
# python

count = Counter()

# iterate through all the documents from our mongo query. count each hashtag.

for x in data:
    count.update(x['hashtags'])

print 'finished counting'

# iterate through the 10 most common hashtags.  then write the hashtag and the
# count to our file

for x in count.most_common(10):
    result = '"%s",%s\n' % (x[0],x[1])
    f.write(result.encode('utf-8'))

print 'finished writing'

#New York Times
import urllib
import urllib2
import json
import test

#Needed throughout the project 
def pretty(obj):
    return json.dumps(obj, sort_keys=True, indent=2)

#Step 1
d = {}
d['api-key'] = '678eeafb3f2b698e01865592a3de62ab:7:70254372'
d['list-name'] = 'hardcover-fiction'
d['date'] = '2014-12-07'
e =  urllib.urlencode(d)
param_str = e

#Step 2
baseurl = "http://api.nytimes.com/svc/books/v2/lists"
nyt_request = baseurl + "?" + param_str

#Step 3
result = urllib2.urlopen(nyt_request)
nyt_json_str = result.read() 


#Step 4 
nyt_data = json.loads(nyt_json_str)

#Step 5-append the url of each book to a list 
hardcover_fiction = []
for a in nyt_data["results"][:10]:
    hardcover_fiction.append(a["amazon_product_url"])
print pretty(hardcover_fiction)


hardcoverfiction_booknames = []
for a in hardcover_fiction:
    b = a.split('/')
    hardcoverfiction_booknames.append(b[3])


def fix_data(x):
    one = [a.replace("ebook", "") for a in x]
    two= [a.replace("Novel", "") for a in one]
    three= [a.replace("book", "") for a in two]
    four= [a.replace("Book", "") for a in three]
    five = [a.lower() for a in four]
    list_novels = [a.replace("-", " ") for a in five]
    return list_novels 
novellist1 = fix_data(hardcoverfiction_booknames) 
print "Here's the best seller list of the top 10 hardcover fiction books"
print pretty(novellist1)
    
#Step 6-10 repeat same process but with next list
d = {}
d['api-key'] = '678eeafb3f2b698e01865592a3de62ab:7:70254372'
d['list-name'] = 'hardcover-nonfiction'
d['date'] = '2014-12-07'
e =  urllib.urlencode(d)
param_str = e

baseurl = "http://api.nytimes.com/svc/books/v3/lists"
nyt_request = baseurl + "?" + param_str

result = urllib2.urlopen(nyt_request)
nyt_json_str = result.read() 

nyt_data = json.loads(nyt_json_str) 

hardcover_nonfiction = []
for a in nyt_data["results"][:10]:
    hardcover_nonfiction.append(a["amazon_product_url"])

hardcovernonfiction_booknames = []
for a in hardcover_nonfiction:
    b = a.split('/')
    hardcovernonfiction_booknames.append(b[3])

def fix_data(x):
    one = [a.replace("ebook", "") for a in x]
    two= [a.replace("Novel", "") for a in one]
    three= [a.replace("book", "") for a in two]
    four= [a.replace("Book", "") for a in three]
    five = [a.lower() for a in four]
    list_novels = [a.replace("-", " ") for a in five]
    return list_novels 
novellist2 = (fix_data(hardcovernonfiction_booknames))
print "Here's the best seller list of the top 10 hardcover non fiction books"
print pretty(novellist2)

print "Tests"
try:
    test.testEqual(type(novellist2), type([]))
    test.testEqual(len(novellist2), 10)
except:
    print "Check that you are performing the list comprehensions correctly in order to collect the names of only ten novels in an iterable list"
    
#Steps 11-15 repeat same process but with third list 
d = {}
d['api-key'] = '678eeafb3f2b698e01865592a3de62ab:7:70254372'
d['list-name'] = 'e-book-fiction'
d['date'] = '2014-12-07'
e =  urllib.urlencode(d)
param_str = e

baseurl = "http://api.nytimes.com/svc/books/v3/lists"
nyt_request = baseurl + "?" + param_str

result = urllib2.urlopen(nyt_request)
nyt_json_str = result.read() 

nyt_data = json.loads(nyt_json_str) 

ebook_fiction = []
for a in nyt_data["results"][:10]:
    ebook_fiction.append(a["amazon_product_url"])
print pretty(ebook_fiction)

ebookfiction_booknames = []
for a in ebook_fiction:
    b = a.split('/')
    ebookfiction_booknames.append(b[3])

def fix_data(x):
    one = [a.replace("ebook", "") for a in x]
    two= [a.replace("Novel", "") for a in one]
    three= [a.replace("book", "") for a in two]
    four= [a.replace("Book", "") for a in three]
    five = [a.lower() for a in four]
    list_novels = [a.replace("-", " ") for a in five]
    return list_novels 
    return list_novels 
novellist3 = fix_data(ebookfiction_booknames) 

print "Here's the best seller list of the top 10 ebook fiction books"
print pretty(novellist3)

#Steps 16-20 repeat same process but with fourth list
d = {}
d['api-key'] = '678eeafb3f2b698e01865592a3de62ab:7:70254372'
d['list-name'] = 'e-book-nonfiction'
d['date'] = '2014-12-07'
e =  urllib.urlencode(d)
param_str = e

baseurl = "http://api.nytimes.com/svc/books/v3/lists"
nyt_request = baseurl + "?" + param_str

result = urllib2.urlopen(nyt_request)
nyt_json_str = result.read() 

nyt_data = json.loads(nyt_json_str) 

ebook_nonfiction = []
for a in nyt_data["results"][:10]:
    ebook_nonfiction.append(a["amazon_product_url"])

ebooknonfiction_booknames = []
for a in ebook_nonfiction:
    b = a.split('/')
    ebooknonfiction_booknames.append(b[3])

def fix_data(x):
    one = [a.replace("ebook", "") for a in x]
    two= [a.replace("Novel", "") for a in one]
    three= [a.replace("book", "") for a in two]
    four= [a.replace("Book", "") for a in three]
    five = [a.lower() for a in four]
    list_novels = [a.replace("-", " ") for a in five]
    return list_novels 
novellist4 = fix_data(ebooknonfiction_booknames) 

print "Here's the best seller list of the top 10 ebook non fiction books"
print pretty(novellist4)

#Twitter
import requests_oauthlib
import webbrowser
import json
import csv

#needed for emoscore
pos_ws = []
f = open('positive-words.txt', 'r')

for l in f.readlines()[35:]:
    pos_ws.append(unicode(l.strip()))
f.close()

neg_ws = []
f = open('negative-words.txt', 'r')
for l in f.readlines()[35:]:
    neg_ws.append(unicode(l.strip()))

client_key = 'zFhthkjO43XERrfcBOWHc8L9G'
client_secret = 'Pu6aJbKWK7ESjxX1nTDtpzsBU9UHuq8DmLBHicG5hvzkHEsVDa'

def get_tokens():
    oauth = requests_oauthlib.OAuth1Session(client_key, client_secret=client_secret) 
    request_token_url = 'https://api.twitter.com/oauth/request_token' 
    fetch_response = oauth.fetch_request_token(request_token_url) 
    resource_owner_key = fetch_response.get('oauth_token')
    resource_owner_secret = fetch_response.get('oauth_token_secret') 
    base_authorization_url = 'https://api.twitter.com/oauth/authorize' 
    authorization_url = oauth.authorization_url(base_authorization_url) 
    webbrowser.open(authorization_url)
    verifier = raw_input('4626449')

    oauth = requests_oauthlib.OAuth1Session(client_key,
                              client_secret=client_secret,
                              resource_owner_key=resource_owner_key,
                              resource_owner_secret=resource_owner_secret,
                              verifier=verifier)
    access_token_url = 'https://api.twitter.com/oauth/access_token'
    oauth_tokens = oauth.fetch_access_token(access_token_url)
    resource_owner_key = oauth_tokens.get('oauth_token')
    resource_owner_secret = oauth_tokens.get('oauth_token_secret')
    
    return (client_key, client_secret, resource_owner_key, resource_owner_secret, verifier)
try:
    f = open("creds.txt", 'r')
    (client_key, client_secret, resource_owner_key, resource_owner_secret, verifier) = json.loads(f.read())
    f.close()
except:
    tokens = get_tokens()
    f = open("creds.txt", 'w')
    f.write(json.dumps(tokens))
    f.close()
    (client_key, client_secret, resource_owner_key, resource_owner_secret, verifier) = tokens
  
search_url = 'https://api.twitter.com/1.1/search/tweets.json'
protected_url = 'https://api.twitter.com/1.1/account/settings.json'
oauth = requests_oauthlib.OAuth1Session(client_key,
                        client_secret=client_secret,
                        resource_owner_key=resource_owner_key,
                        resource_owner_secret=resource_owner_secret) 
print "Now searching each book on the hardcover fiction best seller list on twitter..."
def get_tweetlist(x):
    tweetlist = []
    for a in x:
        search_url = 'https://api.twitter.com/1.1/search/tweets.json'
        resp = oauth.get(search_url, params ={'q': a, 'lang':'en', 'count':25})                          
        tweetdict = resp.json() 
        tweetlist.append((tweetdict, a)) 
    return tweetlist 
dictionary1= get_tweetlist(novellist1) 


print "Tests"
try:
    test.testEqual(type(dictionary1), type([]))
    test.testEqual(len(dictionary1), 10)
except:
    print "Dictionary 1 should be a list of 10 dictionaries of tweets for each novel" 

print "Now collecting 25 tweets for each book..."     
def all_tweetlist(x):
    alltweetslist = []
    for item in x:
        a = item[0]
        for b in a['statuses']:
            alltweetslist.append((b, item[1])) 
    return alltweetslist 
dictionary2 = (all_tweetlist(dictionary1)) 

print "Tests"
try:
    test.testEqual(type(dictionary2), type([]))
    test.testEqual(len(dictionary2[0]), 2)
except:
    print "Dictionary 2 should be a list of all tweets and each item in the dictionary should have two values as it is a tuple" 

class Tweet():
    """object representing one tweet"""
    def __init__(self, tweet_dict, novelname):
        if 'text' in tweet_dict:
            self.text = tweet_dict['text']
        else:
            self.text = ""
        if 'user' in tweet_dict:
            self.favouritescount = tweet_dict['user']['favourites_count']
        else:
            self.favouritescount = 0
        if 'retweet_count' in tweet_dict:
            self.retweet_count = tweet_dict['retweet_count']
        else:
            self.retweet_count = 0
        self.novelname = novelname
        
            
    def positive(self):
        accum_pos = 0
        for a in pos_ws:
            if a in self.text:
                accum_pos = accum_pos + 1 
        return accum_pos
        
    def negative(self):
        accum_neg = 0
        c = self.text.split()
        for b in c:
            if b in neg_ws:
                accum_neg = accum_neg + 1 
        return accum_neg

    def emo_score(self):
        return (self.positive()- self.negative())
        
print "Now collecting the name of the book, the emo score, the favorites counts, and the retweets counts for each tweet..."
for a in dictionary2: # in your list of tuples
    b = Tweet(a[0], a[1]) 

print "Now writing the name, the emo score, the favorites counts, and the retweets counts for each tweet to a csv file..."      
outfile = open("bestsellinglists1.csv","w")
total_tweets = dictionary2
outfile.write('"novel name", "emo score", favourites counts, retweets counts\n')
for a in total_tweets:
    b = Tweet(a[0], a[1]) 
    tweets = (b.novelname, b.emo_score(), b.favouritescount, b.retweet_count)
    outfile.write('"%s","%d", %d, %d\n' % tweets)
outfile.close()

print "Lastly, to see the books in order of popularity in terms of their average favorites/retweets overall..."
outfile = open("bestsellinglists1.csv", 'r')
a = outfile.readlines()
c = sorted(a, key = lambda x: x.count('0'), reverse = True)
print pretty(c[1:]) 

print "Now searching each book on the hardcover non fiction best seller list on twitter..."
def get_tweetlist(x):
    tweetlist = []
    for a in x:
        search_url = 'https://api.twitter.com/1.1/search/tweets.json'
        resp = oauth.get(search_url, params ={'q': a, 'lang':'en', 'count':25})                          
        tweetdict = resp.json() 
        tweetlist.append((tweetdict, a)) 
    return tweetlist 
dictionary1= get_tweetlist(novellist2) 

print "Now collecting 25 tweets for each book..."  
def all_tweetlist(x):
    alltweetslist = []
    for item in x:
        a = item[0]
        for b in a['statuses']:
            alltweetslist.append((b, item[1])) 
    return alltweetslist 
dictionary2 = (all_tweetlist(dictionary1)) 



class Tweet():
    """object representing one tweet"""
    def __init__(self, tweet_dict, novelname):
        if 'text' in tweet_dict:
            self.text = tweet_dict['text']
        else:
            self.text = ""
        if 'user' in tweet_dict:
            self.favouritescount = tweet_dict['user']['favourites_count']
        else:
            self.favouritescount = 0
        if 'retweet_count' in tweet_dict:
            self.retweet_count = tweet_dict['retweet_count']
        else:
            self.retweet_count = 0
        self.novelname = novelname
        
            
    def positive(self):
        accum_pos = 0
        for a in pos_ws:
            if a in self.text:
                accum_pos = accum_pos + 1 
        return accum_pos
        
    def negative(self):
        accum_neg = 0
        c = self.text.split()
        for b in c:
            if b in neg_ws:
                accum_neg = accum_neg + 1 
        return accum_neg

    def emo_score(self):
        return (self.positive()- self.negative())

print "Now collecting the name of the book, the emo score, the favorites counts, and the retweets counts for each tweet..."
for a in dictionary2: # in your list of tuples
    b = Tweet(a[0], a[1]) 

print "Now writing the name, the emo score, the favorites counts, and the retweets counts for each tweet to a csv file..."      
outfile = open("bestsellinglists2.csv","w")
total_tweets = dictionary2
outfile.write('"novel name", "emo score", favourites counts, retweets counts\n')
for a in total_tweets:
    b = Tweet(a[0], a[1]) 
    tweets = (b.novelname, b.emo_score(), b.favouritescount, b.retweet_count)
    outfile.write('"%s","%d", %d, %d\n' % tweets)
outfile.close()


print "Lastly, to see the books in order of popularity in terms of their average favorites/retweets overall..."
outfile = open("bestsellinglists2.csv", 'r')
a = outfile.readlines()
c = sorted(a, key = lambda x: x.count('0'), reverse = True)
print pretty(c[1:]) 

print "Now searching each book on the ebook fiction best seller list on twitter..."
def get_tweetlist(x):
    tweetlist = []
    for a in x:
        search_url = 'https://api.twitter.com/1.1/search/tweets.json'
        resp = oauth.get(search_url, params ={'q': a, 'lang':'en', 'count':25})                          
        tweetdict = resp.json() 
        tweetlist.append((tweetdict, a)) 
    return tweetlist 
dictionary1= get_tweetlist(novellist3) 

print "Now collecting 25 tweets for each book..."  
def all_tweetlist(x):
    alltweetslist = []
    for item in x:
        a = item[0]
        for b in a['statuses']:
            alltweetslist.append((b, item[1])) 
    return alltweetslist 
dictionary2 = (all_tweetlist(dictionary1)) 



class Tweet():
    """object representing one tweet"""
    def __init__(self, tweet_dict, novelname):
        if 'text' in tweet_dict:
            self.text = tweet_dict['text']
        else:
            self.text = ""
        if 'user' in tweet_dict:
            self.favouritescount = tweet_dict['user']['favourites_count']
        else:
            self.favouritescount = 0
        if 'retweet_count' in tweet_dict:
            self.retweet_count = tweet_dict['retweet_count']
        else:
            self.retweet_count = 0
        self.novelname = novelname
        
            
    def positive(self):
        accum_pos = 0
        for a in pos_ws:
            if a in self.text:
                accum_pos = accum_pos + 1 
        return accum_pos
        
    def negative(self):
        accum_neg = 0
        c = self.text.split()
        for b in c:
            if b in neg_ws:
                accum_neg = accum_neg + 1 
        return accum_neg

    def emo_score(self):
        return (self.positive()- self.negative())
        
print "Now collecting the name of the book, the emo score, the favorites counts, and the retweets counts for each tweet..."
for a in dictionary2: # in your list of tuples
    b = Tweet(a[0], a[1]) 
 
print "Now writing the name, the emo score, the favorites counts, and the retweets counts for each tweet to a csv file..."     
outfile = open("bestsellinglists3.csv","w")
total_tweets = dictionary2
outfile.write('"novel name", "emo score", favourites counts, retweets counts\n')
for a in total_tweets:
    b = Tweet(a[0], a[1]) 
    tweets = (b.novelname, b.emo_score(), b.favouritescount, b.retweet_count)
    outfile.write('"%s","%d", %d, %d\n' % tweets)
outfile.close()

print "Lastly, to see the books in order of popularity in terms of their average favorites/retweets overall..."
outfile = open("bestsellinglists3.csv", 'r')
a = outfile.readlines()
c = sorted(a, key = lambda x: x.count('0'), reverse = True)
print pretty(c[1:]) 

print "Now searching each book on the ebook non fiction best seller list on twitter..."
def get_tweetlist(x):
    tweetlist = []
    for a in x:
        search_url = 'https://api.twitter.com/1.1/search/tweets.json'
        resp = oauth.get(search_url, params ={'q': a, 'lang':'en', 'count':25})                          
        tweetdict = resp.json() 
        tweetlist.append((tweetdict, a)) 
    return tweetlist 
dictionary1= get_tweetlist(novellist4) 

print "Now collecting 25 tweets for each book..."  
def all_tweetlist(x):
    alltweetslist = []
    for item in x:
        a = item[0]
        for b in a['statuses']:
            alltweetslist.append((b, item[1])) 
    return alltweetslist 
dictionary2 = (all_tweetlist(dictionary1)) 


class Tweet():
    """object representing one tweet"""
    def __init__(self, tweet_dict, novelname):
        if 'text' in tweet_dict:
            self.text = tweet_dict['text']
        else:
            self.text = ""
        if 'user' in tweet_dict:
            self.favouritescount = tweet_dict['user']['favourites_count']
        else:
            self.favouritescount = 0
        if 'retweet_count' in tweet_dict:
            self.retweet_count = tweet_dict['retweet_count']
        else:
            self.retweet_count = 0
        self.novelname = novelname
        
            
    def positive(self):
        accum_pos = 0
        for a in pos_ws:
            if a in self.text:
                accum_pos = accum_pos + 1 
        return accum_pos
        
    def negative(self):
        accum_neg = 0
        c = self.text.split()
        for b in c:
            if b in neg_ws:
                accum_neg = accum_neg + 1 
        return accum_neg

    def emo_score(self):
        return (self.positive()- self.negative())

print "Now collecting the name of the book, the emo score, the favorites counts, and the retweets counts for each tweet..."
for a in dictionary2: # in your list of tuples
    b = Tweet(a[0], a[1]) 

print "Now writing the name, the emo score, the favorites counts, and the retweets counts for each tweet to a csv file..."     
outfile = open("bestsellinglists4.csv","w")
total_tweets = dictionary2
outfile.write('"novel name", "emo score", favourites counts, retweets counts\n')
for a in total_tweets:
    b = Tweet(a[0], a[1]) 
    tweets = (b.novelname, b.emo_score(), b.favouritescount, b.retweet_count)
    outfile.write('"%s","%d", %d, %d\n' % tweets)
outfile.close()

print "Lastly, to see the books in order of popularity in terms of their average favorites/retweets overall..."
outfile = open("bestsellinglists4.csv", 'r')
a = outfile.readlines()
c = sorted(a, key = lambda x: x.count('0'), reverse = True)
print pretty(c[1:]) 


    
##WARNING: There is a limit for number of calls to API per hour, when this happens a key error comes up on line 256 with 'statuses', yet when you actually print, it shows the rate limit error as it cannot retrieve tweets. 




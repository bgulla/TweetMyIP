import tweepy, sys

comsumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""





auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
print "Successfully logged in as " + api.me().name + "."
try:
 if len(sys.argv[1]) <= 140:
  api.update_status(sys.argv[1])
  print "Successfully tweeted: " + "'" + sys.argv[1] + "'!"
 else:
  raise IOError
except:
 print "Something went wrong: either your tweet was too long or you didn't pass in a string argument at launch."
finally:
 print "Shutting down script..."


# http://runnable.com/Us9rGCJY1zNWAAjr/how-to-use-tweepy-for-python

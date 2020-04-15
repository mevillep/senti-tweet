# handler.py

import numpy as np
from twitterscraper import query_tweets

def main(event, context):
    #a = np.arange(15).reshape(3, 5)

    print("Access twitter data")
    #print(a)
    list_of_tweets = query_tweets("Modi", 5)

    #print the retrieved tweets to the screen:
    for tweet in query_tweets("Modi", 5):
        print("**************************")
        print(tweet)

    # file = open("output.txt","w")
    # for tweet in query_tweets("Trump OR Clinton", 10):
    #     file.write(tweet.encode('utf-8'))
    # file.close()

if __name__ == "__main__":
    main('', '')

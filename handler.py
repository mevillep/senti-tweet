# handler.py

import numpy as np
from twitterscraper import query_tweets

def main(event, context):
    #a = np.arange(15).reshape(3, 5)

    print("Access twitter data")
    #print(a)
    list_of_tweets = query_tweets("Trump OR Clinton", 10)

    #print the retrieved tweets to the screen:
    for tweet in query_tweets("Trump OR Clinton", 10):
        print(tweet)


if __name__ == "__main__":
    main('', '')

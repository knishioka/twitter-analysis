import itertools

import matplotlib.pyplot as plt
import tweepy
from wordcloud import WordCloud

from twitter_analysis.tokenizer import extract_list_of_words
from twitter_analysis.twitter import twitter_api


def main():
    api = twitter_api()
    tweets = [
        tweet.full_text for tweet in tweepy.Cursor(api.search, q="朝活", tweet_mode="extended", lang="ja").items(100)
    ]
    nouns = list(itertools.chain.from_iterable(map(extract_list_of_words, tweets)))
    fpath = "~/Library/Fonts/ipaexg.ttf"
    stop_words = ["https"]
    wordcloud = WordCloud(
        font_path=fpath, background_color="white", width=900, height=500, stopwords=stop_words
    ).generate(" ".join(nouns))

    plt.figure(figsize=(15, 12))
    plt.imshow(wordcloud)
    plt.save("wordcloud.png")
    plt.close


if __name__ == "__main__":
    main()

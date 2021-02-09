import itertools

import matplotlib.pyplot as plt
import MeCab
from wordcloud import WordCloud

from twitter_analysis.twitter import twitter_api


def main():
    results = twitter_api().search(q="朝活")
    tweets = [r.text for r in results]
    m = MeCab.Tagger("-Ochasen")
    nouns = list(
        itertools.chain.from_iterable(
            [[line.split()[0] for line in m.parse(t).splitlines() if "名詞" in line.split()[-1]] for t in tweets]
        )
    )
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

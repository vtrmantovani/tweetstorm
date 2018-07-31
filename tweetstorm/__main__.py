import getopt
import sys

from tweetstorm import Tweetstorm


def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "h:t:", ["text="])
    except getopt.GetoptError:
        print('tweetstorm -t <text>')
        sys.exit()

    for opt, arg in opts:
        if opt == '-h':
            print('tweetstorm -t <text>')
            sys.exit()
        elif opt in ("-t", "--text"):
            t = Tweetstorm(arg)
            tweets = t.generate()
            for tweet in tweets:
                print(tweet)

            sys.exit()

    print('tweetstorm -t <text>')
    sys.exit()


if __name__ == "__main__":
    main()

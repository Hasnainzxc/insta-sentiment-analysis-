    from textblob import TextBlob
    import requests
    from bs4 import BeautifulSoup

    # Function to fetch comments from Instagram post URL
    def fetch_comments(post_url):
        try:
            response = requests.get(post_url)
            response.raise_for_status()  # Check for HTTP errors
            soup = BeautifulSoup(response.text, 'html.parser')
            comments = []
            comment_tags = soup.find_all('div', class_='C4VMK')
            for comment_tag in comment_tags:
                comment = comment_tag.find('span').text
                comments.append(comment)
            return comments
        except requests.RequestException as e:
            print(f"Error fetching comments: {e}")
            return None

    # Function to perform sentiment analysis
    def analyze_sentiment(comments):
        positive = 0
        neutral = 0
        negative = 0
        total = len(comments)

        for comment in comments:
            analysis = TextBlob(comment)
            if analysis.sentiment.polarity > 0:
                positive += 1
            elif analysis.sentiment.polarity == 0:
                neutral += 1
            else:
                negative += 1

        print("Sentiment Analysis Results:")
        print("Positive Comments:", positive)
        print("Neutral Comments:", neutral)
        print("Negative Comments:", negative)
        print("Total Comments:", total)

    # Main function
    def main():
        post_url = input("https://www.instagram.com/p/C6w-EiNrfIU/?utm_source=ig_web_copy_link ")
        comments = fetch_comments(post_url)
        if comments:
            analyze_sentiment(comments)

    if __name__ == "__main__":
        main()

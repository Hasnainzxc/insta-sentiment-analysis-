from textblob import TextBlob
import requests
import json

# Function to fetch comments from Instagram post
def fetch_comments(post_url):
    api_url = f"{post_url}?__a=1"
    response = requests.get(api_url)
    if response.status_code == 200:
        data = json.loads(response.text)
        comments = []
        for comment in data['graphql']['shortcode_media']['edge_media_to_parent_comment']['edges']:
            comments.append(comment['node']['text'])
        return comments
    else:
        print("Error fetching comments")
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
    post_url = input("Enter the URL of the Instagram post: ")
    comments = fetch_comments(post_url)
    if comments:
        analyze_sentiment(comments)

if __name__ == "__main__":
    main()

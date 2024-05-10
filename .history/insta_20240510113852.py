from textblob import TextBlob

# Sample comments for demonstration
sample_comments = [
    "Great post! Love your content.",
    "This is amazing!",
    "Not bad, but could be better.",
    "I don't like it.",
    "Neutral comment here.",
    "Wow, this is terrible."
]

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
    analyze_sentiment(sample_comments)

if __name__ == "__main__":
    main()

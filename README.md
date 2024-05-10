# Instagram Sentiment Analysis Script

This Python script allows you to perform sentiment analysis on comments from an Instagram post. It fetches comments from an Instagram post URL and analyzes the sentiment of those comments using the TextBlob library.

## Installation

1. Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

2. Clone this repository or download the `instagram_sentiment_analysis.py` file.

3. Install the required dependencies using pip:

pip install -r requirements.txt

bash
Copy code

## Usage

1. Run the script by executing the following command in your terminal or command prompt:

python instagram_sentiment_analysis.py

vbnet
Copy code

2. You will be prompted to enter the URL of the Instagram post you want to analyze.

3. Copy the URL of the Instagram post you want to analyze and paste it into the terminal.

4. Press Enter, and the script will fetch the comments from the provided Instagram post URL and perform sentiment analysis on them.

5. The sentiment analysis results will be displayed, showing the number of positive, neutral, and negative comments.

## Example

Enter the URL of the Instagram post: https://www.instagram.com/p/C6wLaVvL-hp/?utm_source=ig_web_copy_link

Sentiment Analysis Results:
Positive Comments: 10
Neutral Comments: 5
Negative Comments: 3
Total Comments: 18

vbnet
Copy code

## Notes

- The script uses BeautifulSoup for web scraping. Keep in mind that web scraping might violate Instagram's terms of service, so use this script responsibly and consider alternative methods if you plan to use it for production or commercial purposes.

- If Instagram's HTML structure changes, the script may break. In such cases, you may need to update the script accordingly.

- This script is provided as-is and may require modifications to suit your specific needs.

## License

This project is licensed under the [MIT License](LICENSE).

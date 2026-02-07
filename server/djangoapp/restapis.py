import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

backend_url = os.getenv(
    'backend_url', default="http://localhost:3030")
sentiment_analyzer_url = os.getenv(
    'sentiment_analyzer_url',
    default="http://localhost:5050/")

# Create a `get_request` to make HTTP GET requests
def get_request(endpoint, **kwargs):
    """
    Make HTTP GET request to backend
    """
    params = ""
    if kwargs:
        for key, value in kwargs.items():
            params = params + key + "=" + str(value) + "&"
    
    request_url = backend_url + endpoint + "?" + params
    print("GET from {} ".format(request_url))
    
    try:
        # Call get method of requests library with URL and parameters
        response = requests.get(request_url)
        return response.json()
    except Exception as e:
        # If any error occurs
        print("Network exception occurred:", e)
        return None

# Create a `post_request` to make HTTP POST requests
def post_request(endpoint, json_payload, **kwargs):
    """
    Make HTTP POST request to backend
    """
    params = ""
    if kwargs:
        for key, value in kwargs.items():
            params = params + key + "=" + str(value) + "&"
    
    request_url = backend_url + endpoint + "?" + params
    print("POST to {} ".format(request_url))
    
    try:
        response = requests.post(request_url, json=json_payload)
        return response.json()
    except Exception as e:
        print("Network exception occurred:", e)
        return {"error": str(e)}

# Create an `analyze_review_sentiments` method to call Watson NLU and analyze text
def analyze_review_sentiments(text):
    """
    Analyze text sentiment using sentiment analyzer service
    """
    if not text:
        return {"sentiment": "neutral"}
    
    # Remove any trailing slash from URL
    base_url = sentiment_analyzer_url.rstrip('/')
    request_url = base_url + "analyze/" + text
    print("GET from {} ".format(request_url))
    
    try:
        # Call get method of requests library with URL
        response = requests.get(request_url)
        
        if response.status_code == 200:
            result = response.json()
            # Extract sentiment from response
            sentiment = result.get('sentiment', {}).get('label', 'neutral')
            return {"sentiment": sentiment}
        else:
            print(f"Sentiment analyzer returned status: {response.status_code}")
            return {"sentiment": "neutral"}
    except Exception as e:
        print("Network exception occurred during sentiment analysis:", e)
        return {"sentiment": "neutral"}

# Create post_review method to post a review - EXACTLY AS COURSERA SHOWS
def post_review(data_dict):
    """
    Post a review to the backend - EXACT COURSERA CODE
    """
    request_url = backend_url + "/insert_review"
    try:
        response = requests.post(request_url, json=data_dict)
        print(response.json())
        return response.json()
    except:
        print("Network exception occurred")
        return {"error": "Network exception occurred"}
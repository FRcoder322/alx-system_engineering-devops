import requests

def number_of_subscribers(subreddit):
    # Set a custom User-Agent header to avoid issues with the Reddit API
    headers = {'User-Agent': 'CustomUserAgent'}

    # Construct the API URL for the subreddit
    url = f'https://www.reddit.com/r/{subreddit}/about.json'

    # Make the API request
    response = requests.get(url, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response and return the number of subscribers
        subreddit_info = response.json().get('data', {}).get('subscribers', 0)
        return subreddit_info
    elif response.status_code == 404:
        # Return 0 for invalid subreddits
        return 0
    else:
        # Handle other potential errors
        print(f"Error: {response.status_code}")
        return 0

# Example usage
subreddit_name = 'python'
subscribers_count = number_of_subscribers(subreddit_name)

if subscribers_count:
    print(f'The subreddit "{subreddit_name}" has {subscribers_count} subscribers.')
else:
    print(f'The subreddit "{subreddit_name}" is invalid or inaccessible.')


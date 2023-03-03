import googleapiclient.discovery
import googleapiclient.errors

# Replace with your API key
api_key = "YOUR_API_KEY_HERE"

# Build the YouTube API client
youtube = googleapiclient.discovery.build("youtube", "v3", developerKey=api_key)

# Define the search query
query = "cat videos"

# Make the API request to search for videos
try:
    request = youtube.search().list(
        part="id,snippet",
        q=query,
        type="video",
        maxResults=10
    )
    response = request.execute()

    # Print the results
    for item in response["items"]:
        print(item["snippet"]["title"])
except googleapiclient.errors.HttpError as e:
    print("An error occurred: %s" % e)

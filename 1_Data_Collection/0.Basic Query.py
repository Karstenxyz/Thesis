import requests

# The URL of the Snapshot Hub GraphQL API endpoint
url = "https://hub.snapshot.org/graphql"

# Your GraphQL query
query = """
{
  proposals {
    id
    title
    body
    start
    end
    state
    author
  }
}
"""

# Make a POST request to the endpoint with the query
response = requests.post(url, json={'query': query})

# Check if the request was successful
if response.status_code == 200:
    # Extract the data from the response
    data = response.json()
    print(data)
else:
    print("Failed to fetch data:", response.status_code)
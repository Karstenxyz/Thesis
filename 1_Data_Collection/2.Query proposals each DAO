import requests
from datetime import datetime

# The URL of the Snapshot Hub GraphQL API endpoint
url = "https://hub.snapshot.org/graphql"

# The updated GraphQL query
query = """
query Proposals {
  proposals(
    first: 700,
    skip: 0,
    where: {
      space_in: ["ferrum-network.eth"],
      state: "closed"
    }
  ) {
    id
    title
    body
    choices
    start
    end
    snapshot
    state
    author
    scores
    votes
    scores_total
    strategies {
      network
      params
    }
  }
}
"""

# Prepare the headers
headers = {
    "Content-Type": "application/json",
}

# Make a POST request to the endpoint with the query and headers
response = requests.post(url, json={'query': query}, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # Extract the data from the response
    data = response.json()
    print(data)
else:
    print("Failed to fetch data:", response.status_code)
    print(response.text)  # This will print the full error message from the API

# export the data into an xlsx

import pandas as pd

# Assuming 'data' is your JSON object that you've fetched
# and it contains the proposals in a list under ['data']['proposals']
proposals = data['data']['proposals']

# Convert the proposals list into a DataFrame
df = pd.DataFrame(proposals)

# Selecting which columns to export, adjust as needed
columns_to_export = ['id', 'title', 'body', 'choices', 'start', 'end', 'snapshot', 'state', 'author', 'scores', 'votes', 'scores_total', 'strategies']
df_export = df[columns_to_export]

# Save to XLSX
filename = "/Users/Karsten/Desktop/ferrum-network.eth.xlsx"
df_export.to_excel(filename, index=False)

print(f"File saved as {filename}")

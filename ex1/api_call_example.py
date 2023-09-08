import requests

url = 'http://localhost:4000/graphql'


query = """
query {
  artists(where: { name: "Red Hot Chili Peppers" }) {
	albums {
  	title
	}
  }
}
"""

headers = {
    'Authorization': 'Bearer YourAccessToken',
    'Content-Type': 'application/json',
}

response = requests.post(url, json={'query': query}, headers=headers)
if response.status_code == 200:
    data = response.json()
    print("GraphQL Response:")
    print(data)
else:
    print(f"Error: {response.status_code}")
    print(response.text)  # Print the response content for error diagnosis

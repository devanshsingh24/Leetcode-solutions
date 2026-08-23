import requests
import json

username = "your_leetcode_username"
url = f"https://leetcode.com/graphql"

query = {
    "query": """
    query recentSubmissions($username: String!) {
      recentSubmissionList(username: $username) {
        title
        titleSlug
        statusDisplay
        lang
        timestamp
      }
    }
    """,
    "variables": {"username": username}
}

res = requests.post(url, json=query)
data = res.json()

with open("submissions.json", "w") as f:
    json.dump(data, f, indent=2)

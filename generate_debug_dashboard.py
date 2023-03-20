import requests
import json

# Define your Grafana API endpoint, API key, and InfluixDB datasource URL
GRAFANA_API_URL = 'http://localhost:3000/api/dashboards/db'
GRAFANA_API_KEY = 'eyJrIjoieTZCQTdtNzhRMEdpUDFpdWJ5d2JHSEU1ckRYY0FsbnoiLCJuIjoidGVzdGtleSIsImlkIjoxfQ=='

# Define the panels
PANELS = [
    {
    }
]

# Define the dashboard JSON structure
dashboard= {
    'title': 'Debug Dashboard',
    'panels': [],
    'editable': True,
    'hideControls': False,
    'timezone': 'browser',
    'time': {
	'from': 'now-6h',
	'to': 'now'
    }
}

# Add each panel to the dashboard

# Define the payload to send to the Grafana API
payload = {
    'dashboard': dashboard,
    'overwrite': True,
}

# Send the request to the Grafana API
response = requests.post(
    GRAFANA_API_URL,
    headers={
    	'Authorization': f'Bearer {GRAFANA_API_KEY}',
	'COntent-Type': 'application/json',
    },
    json=payload,
)

# Print the response from the Grafana API
print(response.text)

import requests
import json

# Define your Grafana API endpoint, API key, and InfluixDB datasource URL
GRAFANA_API_URL = 'http://localhost:3000/api/dashboards/db'
GRAFANA_API_KEY = 'eyJrIjoiRElVSE85WjBqbnFvNUE3ZjhoVnNOdEJsa1FBQ0ZwVEIiLCJuIjoidGVzdGtleXphbnppYmFyIiwiaWQiOjF9'

# Define the panels
PANELS = [
    {
	'title':'Temperature',
	'type':'timeseries',
	'query':'''from(bucket: "sis")
  |> range(start: -30d)
  |> filter(fn: (r) => r["_measurement"] =="gateway_debugging")
  |> filter(fn: (r) => r["_field"]=="temperature")
  |> aggregateWindow(every: 5m, fn: mean, createEmpty: false)
  |> yield(name: "mean")''',
	'w':8,
	'x':0,
	'y':0,
"fieldConfig": {
    "defaults": {
      "custom": {
        "drawStyle": "line",
        "lineInterpolation": "smooth",
        "barAlignment": 0,
        "lineWidth": 1,
        "fillOpacity": 10,
        "gradientMode": "none",
        "spanNulls": False,
        "showPoints": "auto",
        "pointSize": 5,
        "stacking": {
          "mode": "none",
          "group": "A"
        },
        "axisPlacement": "auto",
        "axisLabel": "",
        "axisColorMode": "text",
        "scaleDistribution": {
          "type": "linear"
        },
        "axisCenteredZero": False,
        "hideFrom": {
          "tooltip": False,
          "viz": False,
          "legend": False
        },
        "thresholdsStyle": {
          "mode": "off"
        }
      },
      "color": {
        "mode": "palette-classic"
      },
      "mappings": [],
      "thresholds": {
        "mode": "absolute",
        "steps": [
          {
            "color": "green",
            "value": None
          },
          {
            "color": "red",
            "value": 80
          }
        ]
      },
      "unit": "celsius",
      "displayName": "${__field.labels.host}"
    },
    "overrides": []
  },
    },
    {
	'title':'Voltage',
	'type':'timeseries',
	'query':'''from(bucket: "sis")
  |> range(start: -30d)
  |> filter(fn: (r) => r["_measurement"] =="gateway_debugging")
  |> filter(fn: (r) => r["_field"]=="bus_voltage")
  |> aggregateWindow(every: 5m, fn: mean, createEmpty: false)
  |> yield(name: "mean")''',
	'w':8,
	'x':8,
	'y':0,
"fieldConfig": {
    "defaults": {
      "custom": {
        "drawStyle": "line",
        "lineInterpolation": "smooth",
        "barAlignment": 0,
        "lineWidth": 1,
        "fillOpacity": 10,
        "gradientMode": "none",
        "spanNulls": False,
        "showPoints": "auto",
        "pointSize": 5,
        "stacking": {
          "mode": "none",
          "group": "A"
        },
        "axisPlacement": "auto",
        "axisLabel": "",
        "axisColorMode": "text",
        "scaleDistribution": {
          "type": "linear"
        },
        "axisCenteredZero": False,
        "hideFrom": {
          "tooltip": False,
          "viz": False,
          "legend": False
        },
        "thresholdsStyle": {
          "mode": "off"
        }
      },
      "color": {
        "mode": "palette-classic"
      },
      "mappings": [],
      "thresholds": {
        "mode": "absolute",
        "steps": [
          {
            "color": "green",
            "value": None
          },
          {
            "color": "red",
            "value": 80
          }
        ]
      },
      "unit": "volt",
      "displayName": "${__field.labels.host}"
    },
    "overrides": []
  },
    },
    {
	'title':'Current',
	'type':'timeseries',
	'query':'''from(bucket: "sis")
  |> range(start: -30d)
  |> filter(fn: (r) => r["_measurement"] =="gateway_debugging")
  |> filter(fn: (r) => r["_field"]=="current")
  |> aggregateWindow(every: 5m, fn: mean, createEmpty: false)
  |> yield(name: "mean")''',
	'w':8,
	'x':0,
	'y':8,
"fieldConfig": {
    "defaults": {
      "custom": {
        "drawStyle": "line",
        "lineInterpolation": "smooth",
        "barAlignment": 0,
        "lineWidth": 1,
        "fillOpacity": 10,
        "gradientMode": "none",
        "spanNulls": False,
        "showPoints": "auto",
        "pointSize": 5,
        "stacking": {
          "mode": "none",
          "group": "A"
        },
        "axisPlacement": "auto",
        "axisLabel": "",
        "axisColorMode": "text",
        "scaleDistribution": {
          "type": "linear"
        },
        "axisCenteredZero": False,
        "hideFrom": {
          "tooltip": False,
          "viz": False,
          "legend": False
        },
        "thresholdsStyle": {
          "mode": "off"
        }
      },
      "color": {
        "mode": "palette-classic"
      },
      "mappings": [],
      "thresholds": {
        "mode": "absolute",
        "steps": [
          {
            "color": "dark-red",
            "value": None
          },
          {
            "color": "semi-dark-green",
            "value": 0
          }
        ]
      },
      "unit": "amp",
      "displayName": "${__field.labels.host}"
    },
    "overrides": []
  },
  },
    },
    {
	'title':'Power',
	'type':'timeseries',
	'query':'''from(bucket: "sis")
  |> range(start: -30d)
  |> filter(fn: (r) => r["_measurement"] =="gateway_debugging")
  |> filter(fn: (r) => r["_field"]=="power")
  |> aggregateWindow(every: 5m, fn: mean, createEmpty: false)
  |> yield(name: "mean")''',
	'w':8,
	'x':8,
	'y':8,
"fieldConfig": {
    "defaults": {
      "custom": {
        "drawStyle": "line",
        "lineInterpolation": "smooth",
        "barAlignment": 0,
        "lineWidth": 1,
        "fillOpacity": 10,
        "gradientMode": "none",
        "spanNulls": False,
        "showPoints": "auto",
        "pointSize": 5,
        "stacking": {
          "mode": "none",
          "group": "A"
        },
        "axisPlacement": "auto",
        "axisLabel": "",
        "axisColorMode": "text",
        "scaleDistribution": {
          "type": "linear"
        },
        "axisCenteredZero": False,
        "hideFrom": {
          "tooltip": False,
          "viz": False,
          "legend": False
        },
        "thresholdsStyle": {
          "mode": "off"
        }
      },
      "color": {
        "mode": "palette-classic"
      },
      "mappings": [],
      "thresholds": {
        "mode": "absolute",
        "steps": [
          {
            "color": "green",
            "value": None
          },
          {
            "color": "red",
            "value": 80
          }
        ]
      },
      "unit": "watt",
      "displayName": "${__field.labels.host}"
    },
    "overrides": []
  },
    },
    {
	'title':'Percentage',
	'type':'stat',
	'query':'''from(bucket: "sis")
  |> range(start: -30d)
  |> filter(fn: (r) => r["_measurement"] =="gateway_debugging")
  |> filter(fn: (r) => r["_field"]=="p")
  |> aggregateWindow(every: 5m, fn: mean, createEmpty: false)
  |> yield(name: "mean")''',
	'w':8,
	'x':16,
	'y':8,
"fieldConfig": {
    "defaults": {
      "mappings": [],
      "thresholds": {
        "mode": "absolute",
        "steps": [
          {
            "color": "green",
            "value": None
          },
          {
            "color": "red",
            "value": 80
          }
        ]
      },
      "color": {
        "mode": "thresholds"
      },
      "unit": "%",
      "displayName": "${__field.labels.host}"
    },
    "overrides": []
  },
    }
]

# Define the dashboard JSON structure
dashboard= {
    'title': 'Debug Dashboard',
    'panels': [],
    'editable': False,
    'hideControls': False,
    'timezone': 'browser',
    'time': {
	'from': 'now-6h',
	'to': 'now'
    }
}

# Add each panel to the dashboard
for panel in PANELS:
    panel_data = {
	'title': panel['title'],
	'type': panel['type'],
	'datasource':'InfluxDB_v2_Flux',
	'gridPos':
	    {
		'h': 8,
		'w': panel['w'],
		'x': panel['x'],
		'y': panel['y'],
            },
	'fieldConfig': panel['fieldConfig'],
	'targets':[
	    {
		'query': panel['query'],
		'refId':'A',
		'hide:':False,
		'type': panel['type']
	    },
	]
    }

    dashboard['panels'].append(panel_data)
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

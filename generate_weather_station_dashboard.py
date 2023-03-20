import requests
import json

# Define your Grafana API endpoint, API key, and InfluxDB datasource URL
GRAFANA_API_URL = 'http://localhost:3000/api/dashboards/db'
GRAFANA_API_KEY = 'eyJrIjoieTZCQTdtNzhRMEdpUDFpdWJ5d2JHSEU1ckRYY0FsbnoiLCJuIjoidGVzdGtleSIsImlkIjoxfQ=='

# Define the panels to include in the dashboard
#TODO UPDATE GEOMAP QUERY
PANELS = [
    {
	'title': 'Weather Station Location',
	'type': 'geomap',
	'query': '''from(bucket: "TestDataBucket2")
  |> range(start: -10y)
  |> filter(fn: (r) => r["_measurement"] == "TestMeasurement")
  |> filter(fn: (r) => r["_field"] == "longitude" or r["_field"] == "latitude")
  |> filter(fn: (r) => r["id"] == "0")
  |> aggregateWindow(every: v.windowPeriod, fn: mean, createEmpty: false)
  |> yield(name: "mean")''',
	'w': 5,
	'x': 0,
	'y': 0,
"fieldConfig": {
    "defaults": {
      "custom": {
        "hideFrom": {
          "tooltip": False,
          "viz": False,
          "legend": False
        }
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
      "color": {
        "mode": "thresholds"
      }
    },
    "overrides": []
  },
    },
    {
	'title': 'Weather Stations',
	'type': 'table',
	'query': '''from(bucket: "TestDataBucket2")
  |> range(start: -1y)
  |> filter(fn: (r) => r["_measurement"] == "TestMeasurement")
  |> filter(fn: (r) => r["_field"]=="name")
  |> group(columns: ["name"])
  |> keep(columns: ["id", "_value"])
  |> rename(columns: {_value: "Name","id": "Id"})
''',
	'w':19,
	'x':5,
	'y':0,
"fieldConfig": {
    "defaults": {
      "custom": {
        "align": "auto",
        "displayMode": "auto",
        "inspect": False,
        "filterable": False
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
      "color": {
        "mode": "thresholds"
      }
    },
    "overrides": []
  },
    },
    {
        'title': 'Temperature',
	'type': 'timeseries',
        'query':'''from(bucket: "TestDataBucket2")
  |> range(start: -50d)
  |> filter(fn: (r) => r["_measurement"] == "TestMeasurement")
  |> filter(fn: (r) => r["_field"] == "temp")
  |> aggregateWindow(every: v.windowPeriod, fn: mean, createEmpty: false)
  |> yield(name: "mean")''',
        'y_axis_label': 'Temperature (C)',
	'w': 8,
	'x': 0,
	'y': 8,
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
        "mode": "palette-classic",
        "fixedColor": "light-yellow"
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
      "displayName": "Weather Station ${__field.labels.source}",
      "unit": "celsius"
    },
    "overrides": []
  },
    },
    {
	'title': 'Average Temperatures (past 24h)',
	'type': 'gauge',
	'query': '''from(bucket: "TestDataBucket2")
  |> range(start: -1d)
  |> filter(fn: (r) => r["_measurement"] == "TestMeasurement")
  |> filter(fn: (r) => r["_field"] == "temp")
  |> aggregateWindow(every: v.windowPeriod, fn: mean, createEmpty: false)
  |> yield(name: "mean")
''',
	'w': 16,
	'x': 8,
	'y': 8,
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
            "color": "#EAB839",
            "value": 26.5
          },
          {
            "color": "red",
            "value": 28
          }
        ]
      },
      "color": {
        "mode": "thresholds"
      },
      "displayName": "Weather Station ${__field.labels.source}",
      "max": 30,
      "min": 20,
      "unit": "celsius"
    },
    "overrides": []
  },
    },
    {
        'title': 'Rain',
	'type': 'timeseries',
        'query': '''from(bucket: "TestDataBucket2")
  |> range(start: -50d)
  |> filter(fn: (r) => r["_measurement"] == "TestMeasurement")
  |> filter(fn: (r) => r["_field"] == "rain")
  |> aggregateWindow(every: v.windowPeriod, fn: mean, createEmpty: false)
  |> yield(name: "mean")''',
        'y_axis_label': 'Rain (mm)',
	'w': 8,
	'x': 0,
        'y': 16,
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
        "mode": "palette-classic",
        "fixedColor": "blue"
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
      "displayName": "Weather Station ${__field.labels.source}",
      "unit": "lengthmm"
    },
    "overrides": []
  },
    },
    {
	'title': 'Average Rainfall (past 24h)',
        'type': 'gauge',
	'query':'''from(bucket: "TestDataBucket2")
  |> range(start: -1d)
  |> filter(fn: (r) => r["_measurement"] == "TestMeasurement")
  |> filter(fn: (r) => r["_field"] == "rain")
  |> aggregateWindow(every: v.windowPeriod, fn: mean, createEmpty: false)
  |> yield(name: "mean")''',
	'w': 16,
	'x': 8,
	'y': 16,
"fieldConfig": {
    "defaults": {
      "mappings": [],
      "thresholds": {
        "mode": "absolute",
        "steps": [
          {
            "color": "dark-blue",
            "value": None
          }
        ]
      },
      "color": {
        "mode": "thresholds"
      },
      "displayName": "Weather Station ${__field.labels.source}",
      "max": 110,
      "min": 40,
      "unit": "lengthmm"
    },
    "overrides": []
  },
    },
    {
        'title': 'Humidity',
	'type': 'timeseries',
        'query': '''from(bucket: "TestDataBucket2")
  |> range(start: -50d)
  |> filter(fn: (r) => r["_measurement"] == "TestMeasurement")
  |> filter(fn: (r) => r["_field"] == "humidity")
  |> aggregateWindow(every: v.windowPeriod, fn: mean, createEmpty: false)
  |> yield(name: "mean")''',
        'y_axis_label': 'Humidity (%)',
	'w': 8,
	'x': 0,
        'y': 24,
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
        "mode": "palette-classic",
        "fixedColor": "light-green"
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
      "displayName": "Weather Station ${__field.labels.source}",
      "unit": "humidity"
    },
    "overrides": []
  },
    },
    {
	'title': 'Average Humidity (past 24h)',
	'type': 'gauge',
	'query':'''from(bucket: "TestDataBucket2")
  |> range(start: -1d)
  |> filter(fn: (r) => r["_measurement"] == "TestMeasurement")
  |> filter(fn: (r) => r["_field"] == "humidity")
  |> aggregateWindow(every: v.windowPeriod, fn: mean, createEmpty: false)
  |> yield(name: "mean")''',
	'w': 16,
	'x': 8,
	'y': 24,
"fieldConfig": {
    "defaults": {
      "mappings": [],
      "thresholds": {
        "mode": "absolute",
        "steps": [
          {
            "color": "light-blue",
            "value": None
          }
        ]
      },
      "color": {
        "mode": "thresholds"
      },
      "unit": "humidity",
      "displayName": "Weather Station ${__field.labels.source}",
    },
    "overrides": []
  },
    },
    {
        'title': 'Wind Direction',
	'type': 'timeseries',
        'query': '''from(bucket: "TestDataBucket2")
  |> range(start: -50d)
  |> filter(fn: (r) => r["_measurement"] == "TestMeasurement")
  |> filter(fn: (r) => r["_field"] == "wind_direction")
  |> aggregateWindow(every: v.windowPeriod, fn: mean, createEmpty: false)
  |> yield(name: "mean")''',
        'y_axis_label': 'Wind Direction (degrees)',
	'w': 8,
	'x': 0,
        'y': 32,
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
        "mode": "palette-classic",
        "fixedColor": "green"
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
      "displayName": "Weather Station ${__field.labels.source}",
      "unit": "degree"
    },
    "overrides": []
  },
    },
    {
        'title': 'Wind Speed',
	'type': 'timeseries',
        'query': '''from(bucket: "TestDataBucket2")
  |> range(start: -50d)
  |> filter(fn: (r) => r["_measurement"] == "TestMeasurement")
  |> filter(fn: (r) => r["_field"] == "wind_speed")
  |> aggregateWindow(every: v.windowPeriod, fn: mean, createEmpty: false)
  |> yield(name: "mean")''',
        'y_axis_label': 'Wind Speed (m/s)',
	'w': 8,
	'x': 8,
        'y': 32,
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
        "mode": "palette-classic",
        "fixedColor": "light-blue"
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
      "displayName": "Weather Station ${__field.labels.source}",
      "unit": "velocityms"
    },
    "overrides": []
  },
    },
    {
        'title': 'Wind Gust',
	'type': 'timeseries',
        'query': '''from(bucket: "TestDataBucket2")
  |> range(start: -50d)
  |> filter(fn: (r) => r["_measurement"] == "TestMeasurement")
  |> filter(fn: (r) => r["_field"] == "wind_gust")
  |> aggregateWindow(every: v.windowPeriod, fn: mean, createEmpty: false)
  |> yield(name: "mean")''',
	'y_axis_label': 'Wind Gust (m/s)',
	'w': 8,
	'x': 16,
        'y': 32,
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
        "mode": "palette-classic",
        "fixedColor": "super-light-blue"
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
      "displayName": "Weather Station ${__field.labels.source}",
      "unit": "velocityms"
    },
    "overrides": []
  },
    }
    ,
]

# Define the dashboard JSON structure
dashboard = {
    'title': 'Weather Station Dashboard',
    'panels': [],
    'editable': True,
    'hideControls': False,
    'timezone': 'browser',
}

# Add each panel to the dashboard
for panel in PANELS:
    panel_data = {
        'title': panel['title'],
        'type': panel['type'],
        'datasource': 'InfluxDB',
	'gridPos': 
	    {
		'h': 8,
		'w': panel['w'],
		'x': panel['x'],
		'y': panel['y']
	    }
	,
	'fieldConfig': panel['fieldConfig'],
        'targets':[
            {
                'query': panel['query'],
                'refId': 'A',
                'hide': False,
                'type': panel['type'],
            },
	]
    }
    if panel['type'] == 'timeseries':
        panel_data['yaxes'] = [{
	    'label': panel['y_axis_label'],
            'format': 'short',
            'show': True
        }, {
            'format': 'short',
            'show': True
        }]
        panel_data['x_axis'] = {'show': True}

    dashboard['panels'].append(panel_data)

# Add the rows to the dashboard
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
        'Content-Type': 'application/json',
    },
    json=payload,
)

# Print the response from the Grafana API
print(response.text)

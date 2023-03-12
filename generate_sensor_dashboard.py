import requests
import json

# Define your Grafana API endpoint, API key, and InfluixDB datasource URL
GRAFANA_API_URL = 'http://localhost:3000/api/dashboards/db'
GRAFANA_API_KEY = 'eyJrIjoieTZCQTdtNzhRMEdpUDFpdWJ5d2JHSEU1ckRYY0FsbnoiLCJuIjoidGVzdGtleSIsImlkIjoxfQ=='
INFLUXDB_URL = 'http://localhost:8086'
INFLUXDB_BUCKET = 'TestDataSensor'
INFLUXDB_MEASUREMENT = 'TestMeasurementSensor'
# Define the time range for the data

#Define  the panels to incluse in the dashboard

PANELS = [
    {
	'title': 'Sensor Board Location',
	'type': 'geomap',
	'query':'',
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
	'title': 'Sensor Board',
	'type': 'table',
	'query':'',
	'w': 19,
	'x': 5,
	'y': 0,
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
	'title':'Temperature (BME280)',
	'type':'timeseries',
	'query':'''from(bucket: "TestDataSensor")
  |> range(start: -1y, stop: v.timeRangeStop)
  |> filter(fn: (r) => r["_measurement"] == "TestMeasurementSensor")
  |> filter(fn: (r) => r["_field"] == "temp")
  |> aggregateWindow(every: v.windowPeriod, fn: mean, createEmpty: false)
  |> yield(name: "mean")''',
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
      "displayName": "Board ${__field.labels.id}",
      "unit": "celsius"
    },
    "overrides": []
  },
    },
    {
	'title':'Air Pressure (BME280)',
	'type':'timeseries',
	'query':'''from(bucket: "TestDataSensor")
  |> range(start: -1y, stop: v.timeRangeStop)
  |> filter(fn: (r) => r["_measurement"] == "TestMeasurementSensor")
  |> filter(fn: (r) => r["_field"] == "air_pressure")
  |> aggregateWindow(every: v.windowPeriod, fn: mean, createEmpty: false)
  |> yield(name: "mean")''',
	'w': 8,
	'x': 8,
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
      "displayName": "Board ${__field.labels.id}",
      "unit": "pressurehpa"
    },
    "overrides": []
  },
    },
    {
        'title':'Humidity (BME280)',
        'type':'timeseries',
        'query':'''from(bucket: "TestDataSensor")
  |> range(start: -1y, stop: v.timeRangeStop)
  |> filter(fn: (r) => r["_measurement"] == "TestMeasurementSensor")
  |> filter(fn: (r) => r["_field"] == "humidity")
  |> aggregateWindow(every: v.windowPeriod, fn: mean, createEmpty: false)
  |> yield(name: "mean")''',
        'w': 8,
        'x': 16,
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
      "displayName": "Board ${__field.labels.id}",
      "unit": "humidity"
    },
    "overrides": []
  },
    },
    {
        'title':'Particles (SPS30)',
        'type':'timeseries',
        'query':'''from(bucket: "TestDataSensor")
  |> range(start: -1y, stop: v.timeRangeStop)
  |> filter(fn: (r) => r["_measurement"] == "TestMeasurementSensor")
  |> filter(fn: (r) => r["_field"] == "particles")
  |> aggregateWindow(every: v.windowPeriod, fn: mean, createEmpty: false)
  |> yield(name: "mean")''',
        'w': 8,
        'x': 8,
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
      "displayName": "Board ${__field.labels.id}",
      "unit": "µg/m³"
    },
    "overrides": []
  },
    },
    {
        'title':'Ppm (SGP41)',
        'type':'timeseries',
        'query':'''from(bucket: "TestDataSensor")
  |> range(start: -1y, stop: v.timeRangeStop)
  |> filter(fn: (r) => r["_measurement"] == "TestMeasurementSensor")
  |> filter(fn: (r) => r["_field"] == "PPM")
  |> aggregateWindow(every: v.windowPeriod, fn: mean, createEmpty: false)
  |> yield(name: "mean")''',
        'w': 8,
        'x': 8,
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
      "displayName": "Board ${__field.labels.id}",
      "unit": "ppm"
    },
    "overrides": []
  },
    },
    {
        'title':'CO2 (SCD41)',
        'type':'timeseries',
        'query':'''from(bucket: "TestDataSensor")
  |> range(start: -1y, stop: v.timeRangeStop)
  |> filter(fn: (r) => r["_measurement"] == "TestMeasurementSensor")
  |> filter(fn: (r) => r["_field"] == "CO2")
  |> aggregateWindow(every: v.windowPeriod, fn: mean, createEmpty: false)
  |> yield(name: "mean")''',
        'w': 8,
        'x': 16,
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
      "displayName": "Board ${__field.labels.id}",
      "unit": "ppm"
    },
    "overrides": []
  },
    },
    {
        'title':'VOC (SGP41)',
        'type':'timeseries',
        'query':'''from(bucket: "TestDataSensor")
  |> range(start: -1y, stop: v.timeRangeStop)
  |> filter(fn: (r) => r["_measurement"] == "TestMeasurementSensor")
  |> filter(fn: (r) => r["_field"] == "VOC")
  |> aggregateWindow(every: v.windowPeriod, fn: mean, createEmpty: false)
  |> yield(name: "mean")''',
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
      "displayName": "Board ${__field.labels.id}"
    },
    "overrides": []
  },
    },
    {
        'title':'NOx (SGP41)',
        'type':'timeseries',
        'query':'''from(bucket: "TestDataSensor")
  |> range(start: -1y, stop: v.timeRangeStop)
  |> filter(fn: (r) => r["_measurement"] == "TestMeasurementSensor")
  |> filter(fn: (r) => r["_field"] == "NOx")
  |> aggregateWindow(every: v.windowPeriod, fn: mean, createEmpty: false)
  |> yield(name: "mean")''',
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
      "displayName": "Board ${__field.labels.id}"
    },
    "overrides": []
  },
    },
]

# Define the dashboard JSON structure
dashboard = {
    'title': 'Test Dashboard Sensor',
    'panels': [],
    'editable': True,
    'hideControls': False,
    'timezone': 'browser',
    'time': {
	'from':'now-24h',
	'to':'now'
    }
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
#    if panel['type'] == 'timeseries':
#        panel_data['yaxes'] = [{
#            'label': panel['y_axis_label'],
#            'format': 'short',
#            'show': True
#        }, {
#            'format': 'short',
#            'show': True
#        }]
#        panel_data['x_axis'] = {'show': True}

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
        'Content-Type': 'application/json',
    },
    json=payload,
)

# Print the response from the Grafana API
print(response.text)

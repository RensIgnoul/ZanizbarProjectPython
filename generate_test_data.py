import random
import influxdb_client
from influxdb_client.client.write_api import SYNCHRONOUS

from datetime import datetime, timedelta

bucket = "TestOptimization"
org = "APSoftwareProject"
measurement_name = "testMeasurement"
token = "NqUvjEV6LbcA0qgUJ9wA7xjikfZ_7KKz64Bx_vwK_HCVjTaV_iy7TkTb71pLua3CktIpsN4S-dyQ91MyQ-wPDg=="
url="http://localhost:8086"

client = influxdb_client.InfluxDBClient(
    url=url,
    token=token,
    org=org
)
write_api = client.write_api(write_options=SYNCHRONOUS)


for i in range(5):
    for j in range(1000):
        temp = round(random.uniform(24, 28), 1)
        humidity = random.randint(75, 83)
        wind_speed = round(random.uniform(1, 4), 1)
        wind_gusts = round(random.uniform(3, 8), 1)
        wind_direction = random.randint(50, 100)
        rain = round(random.uniform(50, 100), 1)
        sourceNr = random.randint(0,4)

        currentTime = datetime.now()
        prevTime = currentTime - timedelta(seconds=(3600*j))
        epochSeconds = prevTime.timestamp()
        timestamp = str(int(epochSeconds)) + "000000000"

        line = f"TestMeasurement,source={i} temp={temp},humidity={humidity},wind_speed={wind_speed},wind_gust={wind_gusts},wind_direction={wind_direction},rain={rain} {timestamp}"
        write_api.write(bucket=bucket, org=org, record=line)


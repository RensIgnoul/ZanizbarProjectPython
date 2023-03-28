import random
from datetime import datetime, timedelta
import influxdb_client
from influxdb_client.client.write_api import SYNCHRONOUS


#filename = "testdata_sensor.csv"

bucket = "TestDataSensor"
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


#file = open(filename, "w")
sb = ""

for i in range(5):
    for j in range(1000):
        voc = random.randint(0,500)
        nox = random.randint(0,500)
        ppm = round(random.uniform(0,1000),2)
        co2 = round(random.uniform(400,5000),2)
        air_pressure = round(random.uniform(300,1100),2)
        temp = round(random.uniform(-40,85),2)
        humidity = round(random.uniform(0,100),2)
        particles = round(random.uniform(0,1000),2)
        idNr = random.randint(0,4) 

        currentTime = datetime.now()
        prevTime = currentTime - timedelta(seconds=(3600*j))
        epochSeconds = prevTime.timestamp()
        timestamp = str(int(epochSeconds)) + "000000000"

        line = f"TestMeasurementSensor,id={i} VOC={voc},NOx={nox},PPM={ppm},CO2={co2},air_pressure={air_pressure},temp={temp},humidity={humidity},particles={particles} {timestamp}"
        write_api.write(bucket=bucket, org=org, record=line)
       # sb += line

#file.write(sb)

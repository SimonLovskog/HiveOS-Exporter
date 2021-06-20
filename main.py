from prometheus_client import start_http_server, Summary
import time
import os
import aiohttp
import asyncio

from lib.prometheus import hashrates, temperature, algoHashrates, invalidShares

apiUrl = "https://api2.hiveos.farm/api/v2"

async def getData(farmID, workersID, APIKey):
    session = aiohttp.ClientSession(headers={"Authorization": "Bearer %s" % APIKey})

    for workerID in workersID:
        data = await session.get("{}/farms/{}/workers/{}".format(apiUrl, farmID, workerID))
        data = await data.json()
        workerName = data['name']

        for stat in data['miners_summary']['hashrates']:
            algoHashrates.labels("{}_{}".format(workerName, stat['algo'])).set(stat['hash'])
            invalidShares.labels("{}_{}".format(workerName, stat['algo'])).set(stat['shares']['ratio'])

        for stat in data['gpu_stats']:
            hashrates.labels("{}_{}".format(workerName, stat['bus_id'])).set(stat['hash'])
            temperature.labels("{}_{}".format(workerName, stat['bus_id'])).set(stat['temp'])
    
    await session.close()

if __name__ == '__main__':
    start_http_server(8000)
    farmID = os.getenv("FARMID")
    workersID = os.getenv("WORKERSID")
    APIKey = os.getenv("APIKEY")

    workersID = workersID.split(",")

    while True:
        asyncio.run(getData(farmID, workersID, APIKey))
        time.sleep(30000)

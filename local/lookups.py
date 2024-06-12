import asyncio
import time

import aiohttp
import requests
urls = ["https://raw.githubusercontent.com/epshteinmatthew/cesiumscalabilitytest/main/" + item[1] for item in
            requests.get(
                "https://raw.githubusercontent.com/epshteinmatthew/cesiumscalabilitytest/main/metadata.json").json().items()
        if int(item[0]) <= 10000 and int(item[0]) >= 10]
async def get(url, session):
    try:
        async with session.get(url=url) as response:
            resp = await response.read()
            print("Successfully got url {} with resp of length {}.".format(url, len(resp)))
    except Exception as e:
        print("Unable to get url {} due to {}.".format(url, e.__class__))


async def main(urls):
    async with aiohttp.ClientSession() as session:
        ret = await asyncio.gather(*(get(url, session) for url in urls))
    print("Finalized all. Return is a list of len {} outputs.".format(len(ret)))

start = time.time()
asyncio.run(main(urls))
end = time.time()

print("Took {} seconds to pull {} websites.".format(end - start, len(urls)))

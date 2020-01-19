""" This is a test of the FlightAirMap feed """
import asyncio
from aiohttp import ClientSession
from aio_geojson_flightairmap import FlightAirMapFeed
async def main() -> None:
    """ Main function """
    async with ClientSession() as websession:
        # Home Coordinates: Latitude: -33.0, Longitude: 150.0
        # Filter radius: 50 km
        feed = FlightAirMapFeed(websession,
                                (-33.0, 150.0),
                                "http://192.168.0.200/FlightAirMap/live/geojson",
                                filter_radius=20000)
        status, entries = await feed.update()
        print(status)
        print(entries)
        for entry in entries:
            print(entry.publication_date)
            print(entry.coordinates)
            print(entry.flight_num)
asyncio.get_event_loop().run_until_complete(main())

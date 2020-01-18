import asyncio
from aiohttp import ClientSession
from aio_geojson_flightairmap import FlightAirMapFeed
async def main() -> None:
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
        for e in entries:
            print(e.publication_date)
            print(e.coordinates)
            print(e.flight_num)
asyncio.get_event_loop().run_until_complete(main())
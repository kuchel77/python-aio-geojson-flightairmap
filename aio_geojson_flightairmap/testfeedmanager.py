""" Test Feed Manager """
import asyncio
from aiohttp import ClientSession
from aio_geojson_flightairmap import FlightAirMapFeedManager


 
async def _generate_entity(self, external_id):
        """Generate new entity."""
        new_entity = FlightAirMapLocationEvent(self, external_id)
        # Add new entities to HA.
        self._async_add_entities([new_entity], True)

async def _update_entity(self, external_id):
        """Update entity."""
        async_dispatcher_send(self._hass, SIGNAL_UPDATE_ENTITY.format(external_id))

async def _remove_entity(self, external_id):
        """Remove entity."""
        async_dispatcher_send(self._hass, SIGNAL_DELETE_ENTITY.format(external_id))

async def main() -> None:
    """ Main function """
    async with ClientSession() as websession:
        # Home Coordinates: Latitude: -33.0, Longitude: 150.0
        # Filter radius: 50 km

        _feed_manager = FlightAirMapFeedManager(
            websession,
            _generate_entity,
            _update_entity,
            _remove_entity,
            (-33.0, 150.0),
            filter_radius=20000)

        status, entries = await _feed_manager._feed.update()
        print(status)
        print(entries)
        for entry in entries:
            print(entry.publication_date)
            print(entry.coordinates)
            print(entry.flight_num)
            print(entry.aircraft_registration)

asyncio.get_event_loop().run_until_complete(main())

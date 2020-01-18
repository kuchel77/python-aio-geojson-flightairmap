"""Test for the Flight Air Map GeoJSON feed manager."""
import datetime

import aiohttp
import pytest

from aio_geojson_flightairmap.feed_manager import \
    FlightAirMapFeedManager
from tests.utils import load_fixture


@pytest.mark.asyncio
async def test_feed_manager(aresponses, event_loop):
    """Test the feed manager."""
    home_coordinates = (-31.0, 151.0)
    aresponses.add(
        '192.160.0.200',
        '/FlightAirMap/live/geojson',
        'get',
        aresponses.Response(text=load_fixture('flights-1.json'),
                            status=200),
        match_querystring=True,
    )

    async with aiohttp.ClientSession(loop=event_loop) as websession:

        # This will just record calls and keep track of external ids.
        generated_entity_external_ids = []
        updated_entity_external_ids = []
        removed_entity_external_ids = []

        async def _generate_entity(external_id):
            """Generate new entity."""
            generated_entity_external_ids.append(external_id)

        async def _update_entity(external_id):
            """Update entity."""
            updated_entity_external_ids.append(external_id)

        async def _remove_entity(external_id):
            """Remove entity."""
            removed_entity_external_ids.append(external_id)

        feed_manager = FlightAirMapFeedManager(
            websession, _generate_entity, _update_entity, _remove_entity,
            home_coordinates, None)
        assert repr(feed_manager) == "<FlightAirMap" \
                                     "FeedManager(" \
                                     "feed=<FlightAirMapFeed" \
                                     "home=(-31.0, 151.0), url=http://" \
                                     "192.160.0.200" \
                                     "/FlightAirMap/live/geojson, " \
                                     "radius=None)>)>"
        await feed_manager.update()
        entries = feed_manager.feed_entries
        assert entries is not None
        assert len(entries) == 3
        assert len(generated_entity_external_ids) == 3
        assert len(updated_entity_external_ids) == 0
        assert len(removed_entity_external_ids) == 0

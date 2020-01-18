"""Test for the Flight Air Map GeoJSON feed."""
import datetime

import aiohttp
import pytest

from aio_geojson_client.consts import UPDATE_OK

from aio_geojson_flightairmap.consts import ATTRIBUTION
from aio_geojson_flightairmap.feed import FlightAirMapFeed
from tests.utils import load_fixture


@pytest.mark.asyncio
async def test_update_ok(aresponses, event_loop):
    """Test updating feed is ok."""
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

        feed = FlightAirMapFeed(websession, home_coordinates)
        assert repr(feed) == "<FlightAirMapFeed" \
                             "home=(-31.0, 151.0), url=http://" \
                             "192.160.0.200" \
                             "/FlightAirMap/live/geojson, " \
                             "radius=None)>)>"
        status, entries = await feed.update()
        assert status == UPDATE_OK
        assert entries is not None
        assert len(entries) == 3


@pytest.mark.asyncio
async def test_empty_feed(aresponses, event_loop):
    """Test updating feed is ok when feed does not contain any entries."""
    home_coordinates = (-41.2, 174.7)
    aresponses.add(
        '192.168.0.200',
        '/FlightAirMap/live/geojson',
        'get',
        aresponses.Response(text=load_fixture('flights-2.json'),
                            status=200),
        match_querystring=True,
    )

    async with aiohttp.ClientSession(loop=event_loop) as websession:

        feed = FlightAirMapFeed(websession, home_coordinates)
        assert repr(feed) == "<FlightAirMapFeed(" \
                             "home=(-41.2, 174.7), " \
                             "url=http://192.168.0.200" \
                             "/live/geojson, " \
                             "radius=None)>"
        status, entries = await feed.update()
        assert status == UPDATE_OK
        assert entries is not None
        assert len(entries) == 0
        assert feed.last_timestamp is None

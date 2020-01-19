"""Feed Manager for Flight Air Map Incidents feed."""
from aio_geojson_client.feed_manager import FeedManagerBase
from aiohttp import ClientSession

from .feed import FlightAirMapFeed

class FlightAirMapFeedManager(FeedManagerBase):
    """Feed Manager for Flight Air Map feed."""

    def __init__(self,
                 websession: ClientSession,
                 generate_callback,
                 update_callback,
                 remove_callback,
                 coordinates=None,
                 feed_url=None,
                 filter_radius=None):
        """Initialize the Flight Air Map Manager."""
        feed = FlightAirMapFeed(
            websession,
            coordinates,
            feed_url,
            filter_radius)
        super().__init__(feed,
                         generate_callback,
                         update_callback,
                         remove_callback)

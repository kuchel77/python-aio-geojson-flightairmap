"""Flight Air Map feed."""
import logging
from typing import Optional

from aio_geojson_client.feed import GeoJsonFeed
from aiohttp import ClientSession

from aio_geojson_flightairmap.feed_entry import FlightAirMapFeedEntry

_LOGGER = logging.getLogger(__name__)


class FlightAirMapFeed(GeoJsonFeed):
    """Flight Air Map feed."""

    def __init__(self,
                 websession: ClientSession,
                 coordinates,
                 url,
                 filter_radius=None):
        """Initialise this service."""
        super().__init__(websession,                         
                         coordinates,
                         url=url,
                         filter_radius=filter_radius)

    def __repr__(self):
        """Return string representation of this feed."""
        return '<{}(home={}, url={}, radius={})>'.format(
            self.__class__.__name__, self._home_coordinates, self._url,
            self._filter_radius)

    def _new_entry(self, home_coordinates, feature, global_data):
        """Generate a new entry."""
        return FlightAirMapFeedEntry(home_coordinates, feature)

    def _filter_entries(self, entries):
        """Filter the provided entries."""
        filtered_entries = super()._filter_entries(entries)
        return filtered_entries

    def _extract_last_timestamp(self, feed_entries):
        """Determine latest (newest) entry from the filtered feed."""
        if feed_entries:
            dates = sorted(filter(
                None, [entry.publication_date for entry in feed_entries]),
                           reverse=True)
            if dates is not None:
                return dates[0]
        return None

    def _extract_from_feed(self, feed) -> Optional:
        """Extract global metadata from feed."""
        return None

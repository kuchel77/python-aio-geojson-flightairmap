"""Flight Air Map feed entry."""
import pytz
import calendar
from datetime import datetime
from time import strptime

import logging
import re
from typing import Optional
from aio_geojson_client.feed_entry import FeedEntry

import aio_geojson_flightairmap.consts

_LOGGER = logging.getLogger(__name__)

class FlightAirMapFeedEntry(FeedEntry):
    """Flight Air Map Incidents feed entry."""

    def __init__(self, home_coordinates, feature):
        """Initialise this service."""
        super().__init__(home_coordinates, feature)

    @property
    def title(self) -> str:
        """Return the title of this entry."""
        return self._search_in_properties(ATTR_FLIGHT_CODE)

    @property
    def external_id(self) -> str:
        """Return the title of this entry."""
        return self._search_in_properties(ATTR_ID)
  
    @property
    def flight_num(self) -> str:
        """Return the title of this entry."""
        return self._search_in_properties(ATTR_FLIGHT_CODE )

    @property
    def aircraft_registration(self) -> str:
        """Return the y of this entry."""
        return self._search_in_properties(ATTR_AIRCRAFT_REGISTRATION)

    @property
    def aircraft_type(self) -> str:
        """Return the location of this entry."""
        return self._search_in_description(ATTR_AIRCRAFT_TYPE)

    @property
    def departure_airport(self) -> str:
        """Return the y of this entry."""
        return self._search_in_properties(ATTR_DEPARTURE_AIRPORT)

    @property
    def arrival_airport(self) -> str:
        """Return the location of this entry."""
        return self._search_in_description(ATTR_ARRIVAL_AIRPORT)       

    @property
    def publication_date(self) -> datetime:
        """Return the publication date of this entry."""
        current_time = datetime.now().strftime("%d/%m/%Y %I:%M:%S %p")
        date_struct = strptime(current_time, "%d/%m/%Y %I:%M:%S %p")
        publication_date = datetime.fromtimestamp(calendar.timegm(date_struct), tz=pytz.utc)
        return publication_date
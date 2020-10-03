"""Flight Air Map feed entry."""
from datetime import datetime

import logging
import pytz

from aio_geojson_client.feed_entry import FeedEntry

_LOGGER = logging.getLogger(__name__)

class FlightAirMapFeedEntry(FeedEntry):
    """Flight Air Map Incidents feed entry."""

    def __init__(self, home_coordinates, feature):
        """Initialise this service."""
        super().__init__(home_coordinates, feature)

    @property
    def title(self) -> str:
        """Return the title of this entry."""
        return self._search_in_properties("c")

    @property
    def external_id(self) -> str:
        """Return the title of this entry."""
        return self._search_in_properties("fi")

    @property
    def flight_num(self) -> str:
        """Return the title of this entry."""
        return self._search_in_properties("c")

    @property
    def aircraft_registration(self) -> str:
        """Return the y of this entry."""
        return self._search_in_properties("reg")

    @property
    def aircraft_icao(self) -> str:
        """Return the y of this entry."""
        return self._search_in_properties("aircraft_icao")

    @property
    def aircraft_type(self) -> str:
        """Return the location of this entry."""
        return self._search_in_properties("ai")

    @property
    def departure_airport(self) -> str:
        """Return the y of this entry."""
        return self._search_in_properties("dac")

    @property
    def arrival_airport(self) -> str:
        """Return the location of this entry."""
        arrival_airport = self._search_in_properties("aac")
        return arrival_airport
    
    @property
    def altitude(self) -> str:
        """Return the location of this entry."""
        if self._search_in_properties("a") is not None:
            altitude = float(self._search_in_properties("a"))*100
        else:
            altitude = 0
        return altitude

    @property
    def squawk(self) -> str:
        """Return the location of this entry."""
        squawk = self._search_in_properties("sq")
        return squawk
   
    @property
    def heading(self) -> str:
        """Return the location of this entry."""
        heading = self._search_in_properties("h")
        if heading is not None:
            return heading
        return None

    @property
    def publication_date(self) -> datetime:
        """Return the publication date of this entry."""
        last_update = self._search_in_properties("lu")
        if last_update is not None:
            publication_date = datetime.fromtimestamp(int(last_update), tz=pytz.utc)
            return publication_date 
        return None

import re
from datetime import datetime
from typing import Optional

import requests

from requests import Response

from api.api_endpoint import ApiEndpoint
from api.crunchy_obj.account import Account
from api.crunchy_obj.episode import Episode
from api.crunchy_obj.season import Season
from api.request_type import RequestType


class CrunchyApi:
    """
    The API allows to search for series, seasons, episodes, and more.
    """

    def __init__(
            self,
            basic_token: str,
            username: str,
            password: str,
            locale: str = "fr-FR"
    ) -> None:
        self.basic_token = basic_token
        self.username = username
        self.password = password
        self.locale = locale
        self.http = requests.Session()
        self.account = Account(dict())

    def login(self) -> Account:
        """Start a new session with the API"""

        return self._create_session()

    def _create_session(self, refresh: bool = False) -> Account:
        """Initiate a new session or refresh the session with the API"""

        if not refresh:
            data = {
                "username": self.username,
                "password": self.password,
                "grant_type": "password",
                "scope": "offline_access",
            }
        else:
            data = {
                "refresh_token": self.account.refresh_token,
                "grant_type": "refresh_token",
                "scope": "offline_access",
            }

        headers = {
            'Authorization': '{type} {key}'.format(type='Basic', key=self.basic_token),
        }

        # It's necessary to make a manual request to prevent recursive requests
        r = self.http.request(
            method=RequestType.POST,
            url=ApiEndpoint.TOKEN,
            headers=headers,
            data=data
        )
        json = self._check_request(r)
        self.account.load_data_source(json)

        json = self._make_request(RequestType.GET, ApiEndpoint.INDEX)
        self.account.load_data_source(json)

        json = self._make_request(RequestType.GET, ApiEndpoint.PROFILE)
        self.account.load_data_source(json)

        return self.account

    def _make_request(
            self,
            method: RequestType,
            url: str,
            data: Optional[dict] = None,
            params: Optional[dict] = None
    ) -> dict:
        """Generic method to make a request to the API"""

        if self.account and self.account.expires_in <= datetime.utcnow():
            self._create_session(refresh=True)

        authorization_data = {
            RequestType.GET: {"type": 'Bearer', "key": self.account.access_token},
            RequestType.POST: {"type": 'Basic', "key": self.basic_token},
        }
        authorization = authorization_data.get(method)

        headers = {
            'Authorization': '{type} {key}'.format(type=authorization.get("type"), key=authorization.get("key")),
        }

        r = self.http.request(
            method=str(method),
            url=str(url),
            headers=headers,
            data=data,
            params=params
        )

        return self._check_request(r)

    @staticmethod
    def _check_request(r: Response) -> dict:
        """Check if the request was successful"""

        code: int = r.status_code
        json: [dict] = r.json()

        if "error" in json:
            error_type = json.get("error")
            if error_type == "invalid_grant":
                raise Exception("Error {code}: Fail to login".format(code=code))
        elif "message" in json and "code" in json:
            raise Exception("Error {code}: {message}".format(code=code, message=json.get("message")))
        if code != 200:
            raise Exception("Unknown Error {code}: {message}".format(code=code, message=r.text))

        return json

    @staticmethod
    def is_series_link(url: str) -> bool:
        pattern = r"https?:\/\/(www\.)?beta\.crunchyroll\.com\/[a-zA-Z]{2}\/series\/\w+(\/\w+)?"
        return True if re.match(pattern, url) else False

    @staticmethod
    def is_episode_link(url: str) -> bool:
        pattern = r"https?:\/\/(www\.)?beta\.crunchyroll\.com\/[a-zA-Z]{2}\/watch\/\w+(\/\w+)?"
        return True if re.match(pattern, url) else False

    def get_seasons_from_series_id(self, series_id: str) -> [Season]:
        """Get all seasons from a series"""

        params = {
            "series_id": series_id,
            "locale": self.locale,
            "Policy": self.account.cms.policy,
            "Signature": self.account.cms.signature,
            "Key-Pair-Id": self.account.cms.key_pair_id,
        }

        json = self._make_request(
            RequestType.GET,
            ApiEndpoint.SEASONS.format(bucket=self.account.cms.bucket),
            params=params
        )

        return [Season(item) for item in json.get("items")]

    def get_episodes_from_season_id(self, season_id: str) -> [Episode]:
        """Get all episodes from a season"""

        params = {
            "season_id": season_id,
            "locale": self.locale,
            "Policy": self.account.cms.policy,
            "Signature": self.account.cms.signature,
            "Key-Pair-Id": self.account.cms.key_pair_id,
        }

        json = self._make_request(
            RequestType.GET,
            ApiEndpoint.EPISODES.format(bucket=self.account.cms.bucket),
            params=params
        )

        return [Episode(item) for item in json.get("Items")]

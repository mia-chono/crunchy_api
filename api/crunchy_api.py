import re
import urllib.parse
from datetime import datetime
from typing import Any, Optional

import requests

from requests import Response

from api.api_endpoint import ApiEndpoint
from api.crunchy_obj.account import Account
from api.crunchy_obj.season import Season
from api.request_type import RequestType


class CrunchyApi:
    """
        TODO mini description
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
        return self._create_session()

    def _create_session(self, refresh: bool = False) -> Account:
        if not refresh:
            data = {
                "username": self.username,
                "password": self.password,
                "grant_type": "password",
                "scope": "offline_access",
            }
        elif refresh:
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
        json = self._check_request_error(r)
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

        return self._check_request_error(r)

    @staticmethod
    def _check_request_error(r: Response) -> dict:
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

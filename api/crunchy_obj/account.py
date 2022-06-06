import json
from datetime import datetime, timedelta
from json import dumps
from typing import Optional

from api.crunchy_obj.base_crunchyroll_object_interface import BaseCrunchyrollObjectInterface
from api.crunchy_obj.cms import CMS


class Account(BaseCrunchyrollObjectInterface):
    def __init__(self, data: Optional[dict] = {}):
        self.access_token: Optional[str] = data.get("access_token")
        self.refresh_token: Optional[str] = data.get("refresh_token")
        self.expires_in: datetime = datetime.utcnow() + timedelta(seconds=data.get("expires_in") or 0)
        self.token_type: Optional[str] = data.get("token_type")
        self.scope: Optional[str] = data.get("scope")
        self.country: Optional[str] = data.get("country")
        self.account_id: Optional[str] = data.get("account_id")

        self.cms: CMS = CMS(data.get("cms", {}))

        self.avatar: Optional[str] = data.get("avatar")
        self.has_beta: Optional[bool] = data.get("cr_beta_opt_in")
        self.email_verified: Optional[bool] = data.get("crleg_email_verified")
        self.email: Optional[str] = data.get("email")
        self.maturity_rating: Optional[str] = data.get("maturity_rating")
        self.account_language: Optional[str] = data.get("preferred_communication_language")
        self.subtitles_language: Optional[str] = data.get("preferred_communication_language")
        self.username: Optional[str] = data.get("username")

    def load_data_source(self, data_source: dict):
        self.access_token = data_source.get("access_token") or self.access_token
        self.refresh_token = data_source.get("refresh_token") or self.refresh_token

        if data_source.get("expires_in"):
            self.expires_in = datetime.utcnow() + timedelta(seconds=data_source.get("expires_in"))

        self.token_type = data_source.get("token_type") or self.token_type
        self.scope = data_source.get("scope") or self.scope
        self.country = data_source.get("country") or self.country
        self.account_id = data_source.get("account_id") or self.account_id

        if data_source.get("cms"):
            self.cms.load_data_source(data_source.get("cms"))

        self.avatar = data_source.get("avatar") or self.avatar
        self.has_beta = data_source.get("cr_beta_opt_in") or self.has_beta
        self.email_verified = data_source.get("crleg_email_verified") or self.email_verified
        self.email = data_source.get("email") or self.email
        self.maturity_rating = data_source.get("maturity_rating") or self.maturity_rating
        self.account_language = data_source.get("preferred_communication_language") or self.account_language
        self.subtitles_language = data_source.get("preferred_communication_language") or self.subtitles_language
        self.username = data_source.get("username") or self.username

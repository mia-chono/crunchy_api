from typing import Optional

from crunchy_api.crunchy_api.crunchy_obj.base_crunchyroll_object_interface import BaseCrunchyrollObjectInterface


class CMS(BaseCrunchyrollObjectInterface):
    def __init__(self, data_source: Optional[dict] = {}):
        self.bucket: Optional[str] = data_source.get("bucket")
        self.policy: Optional[str] = data_source.get("policy")
        self.signature: Optional[str] = data_source.get("signature")
        self.key_pair_id: Optional[str] = data_source.get("key_pair_id")
        self.expires: Optional[str] = data_source.get("expires")

    def load_data_source(self, data_source: dict):
        self.bucket = data_source.get("bucket") or self.bucket
        self.policy = data_source.get("policy") or self.policy
        self.signature = data_source.get("signature") or self.signature
        self.key_pair_id = data_source.get("key_pair_id") or self.key_pair_id
        self.expires = data_source.get("expires") or self.expires

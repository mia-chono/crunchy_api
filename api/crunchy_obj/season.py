from typing import Optional

from api.crunchy_obj.base_crunchyroll_object_interface import BaseCrunchyrollObjectInterface


class Season(BaseCrunchyrollObjectInterface):
    def __init__(self, data_source: Optional[dict] = {}):
        self.id: Optional[str] = data_source.get("id")
        self.channel_id: Optional[str] = data_source.get("channel_id")
        self.title: Optional[str] = data_source.get("title")
        self.slug_title: Optional[str] = data_source.get("slug_title")
        self.series_id: Optional[str] = data_source.get("series_id")
        self.season_number: Optional[int] = data_source.get("season_number")
        self.is_complete: Optional[bool] = data_source.get("is_complete")
        self.description: Optional[str] = data_source.get("description")
        self.keywords: list[str] = data_source.get("keywords", [])
        self.season_tags: list[str] = data_source.get("season_tags", [])
        self.images: dict = data_source.get("images", {})
        self.is_mature: Optional[bool] = data_source.get("is_mature")
        self.mature_blocked: Optional[bool] = data_source.get("mature_blocked")
        self.is_subbed: Optional[bool] = data_source.get("is_subbed")
        self.is_dubbed: Optional[bool] = data_source.get("is_dubbed")
        self.is_simulcast: Optional[bool] = data_source.get("is_simulcast")
        self.seo_title: Optional[str] = data_source.get("seo_title")
        self.seo_description: Optional[str] = data_source.get("seo_description")
        self.availability_notes: Optional[str] = data_source.get("availability_notes")

    def load_data_source(self, data_source: dict):
        self.id = data_source.get("id") or self.id
        self.channel_id = data_source.get("channel_id") or self.channel_id
        self.title = data_source.get("title") or self.title
        self.slug_title = data_source.get("slug_title") or self.slug_title
        self.series_id = data_source.get("series_id") or self.series_id
        self.season_number = data_source.get("season_number") or self.season_number
        self.is_complete = data_source.get("is_complete") or self.is_complete
        self.description = data_source.get("description") or self.description
        self.keywords = data_source.get("keywords", []) or self.keywords
        self.season_tags = data_source.get("season_tags", []) or self.season_tags
        self.images = data_source.get("images", {}) or self.images
        self.is_mature = data_source.get("is_mature") or self.is_mature
        self.mature_blocked = data_source.get("mature_blocked") or self.mature_blocked
        self.is_subbed = data_source.get("is_subbed") or self.is_subbed
        self.is_dubbed = data_source.get("is_dubbed") or self.is_dubbed
        self.is_simulcast = data_source.get("is_simulcast") or self.is_simulcast
        self.seo_title = data_source.get("seo_title") or self.seo_title
        self.seo_description = data_source.get("seo_description") or self.seo_description
        self.availability_notes = data_source.get("availability_notes") or self.availability_notes

from typing import Optional

from crunchy_api.crunchy_api.crunchy_obj.base_crunchyroll_object_interface import BaseCrunchyrollObjectInterface
from crunchy_api.crunchy_api.crunchy_obj.episode_links import EpisodeLinks
from crunchy_api.crunchy_api.crunchy_obj.images import Images


class Episode(BaseCrunchyrollObjectInterface):
    def __init__(self, data_source: Optional[dict]):
        self.links: EpisodeLinks = EpisodeLinks(data_source.get("__links__", {}))
        self.id: Optional[str] = data_source.get("id")
        self.channel_id: Optional[str] = data_source.get("channel_id")
        self.series_id: Optional[str] = data_source.get("series_id")
        self.series_title: Optional[str] = data_source.get("series_title")
        self.series_slug_title: Optional[str] = data_source.get("series_slug_title")
        self.season_id: Optional[str] = data_source.get("season_id")
        self.season_title: Optional[str] = data_source.get("season_title")
        self.season_slug_title: Optional[str] = data_source.get("season_slug_title")
        self.season_number: Optional[int] = data_source.get("season_number")
        self.episode: Optional[str] = data_source.get("episode")
        self.episode_number: Optional[int] = data_source.get("episode_number")
        self.sequence_number: Optional[int] = data_source.get("sequence_number")
        self.production_episode_id: Optional[str] = data_source.get("production_episode_id")
        self.title: Optional[str] = data_source.get("title")
        self.slug_title: Optional[str] = data_source.get("slug_title")
        self.description: Optional[str] = data_source.get("description")
        self.next_episode_id: Optional[str] = data_source.get("next_episode_id")
        self.next_episode_title: Optional[str] = data_source.get("next_episode_title")
        self.hd_flag: Optional[bool] = data_source.get("hd_flag")
        self.is_mature: Optional[bool] = data_source.get("is_mature")
        self.mature_blocked: Optional[bool] = data_source.get("mature_blocked")
        self.episode_air_date: Optional[str] = data_source.get("episode_air_date")
        self.is_subbed: Optional[bool] = data_source.get("is_subbed")
        self.is_dubbed: Optional[bool] = data_source.get("is_dubbed")
        self.is_clip: Optional[bool] = data_source.get("is_clip")
        self.seo_title: Optional[str] = data_source.get("seo_title")
        self.seo_description: Optional[str] = data_source.get("seo_description")
        self.season_tags: list[str] = data_source.get("season_tags", [])
        self.available_offline: Optional[bool] = data_source.get("available_offline")
        self.media_type: Optional[str] = data_source.get("media_type")
        self.slug: Optional[str] = data_source.get("slug")
        self.images: Images = Images(data_source.get("images", {}))
        self.duration_ms: Optional[int] = data_source.get("duration_ms")
        self.is_premium_only: Optional[bool] = data_source.get("is_premium_only")
        self.listing_id: Optional[str] = data_source.get("listing_id")
        self.subtitle_locales: list[str] = data_source.get("subtitle_locales", [])
        self.playback: Optional[str] = data_source.get("playback")
        self.availability_notes: Optional[str] = data_source.get("availability_notes")

    def load_data_source(self, data_source: dict):
        if data_source.get("__links__"):
            self.links = EpisodeLinks(data_source.get("__links__", {}))
        self.id = data_source.get("id") or self.id
        self.channel_id = data_source.get("channel_id") or self.channel_id
        self.series_id = data_source.get("series_id") or self.series_id
        self.series_title = data_source.get("series_title") or self.series_title
        self.series_slug_title = data_source.get("series_slug_title") or self.series_slug_title
        self.season_id = data_source.get("season_id") or self.season_id
        self.season_title = data_source.get("season_title") or self.season_title
        self.season_slug_title = data_source.get("season_slug_title", []) or self.season_slug_title
        self.season_number = data_source.get("season_number") or self.season_number
        self.episode = data_source.get("episode") or self.episode
        self.episode_number = data_source.get("episode_number") or self.episode_number
        self.sequence_number = data_source.get("sequence_number") or self.sequence_number
        self.production_episode_id = data_source.get("production_episode_id") or self.production_episode_id
        self.title = data_source.get("title") or self.title
        self.slug_title = data_source.get("slug_title") or self.slug_title
        self.description = data_source.get("description") or self.description
        self.next_episode_id = data_source.get("next_episode_id") or self.next_episode_id
        self.next_episode_title = data_source.get("next_episode_title") or self.next_episode_title
        self.hd_flag = data_source.get("hd_flag") or self.hd_flag
        self.is_mature = data_source.get("is_mature") or self.is_mature
        self.mature_blocked = data_source.get("mature_blocked") or self.mature_blocked
        self.episode_air_date = data_source.get("episode_air_date") or self.episode_air_date
        self.is_subbed = data_source.get("is_subbed") or self.is_subbed
        self.is_dubbed = data_source.get("is_dubbed") or self.is_dubbed
        self.is_clip = data_source.get("is_clip") or self.is_clip
        self.seo_title = data_source.get("seo_title") or self.seo_title
        self.seo_description = data_source.get("seo_description") or self.seo_description
        self.season_tags = data_source.get("season_tags", []) or self.season_tags
        self.available_offline = data_source.get("available_offline") or self.available_offline
        self.media_type = data_source.get("media_type") or self.media_type
        self.slug = data_source.get("slug") or self.slug
        self.images = Images(data_source.get("images", {})) or self.images
        self.duration_ms = data_source.get("duration_ms") or self.duration_ms
        self.is_premium_only = data_source.get("is_premium_only") or self.is_premium_only
        self.listing_id = data_source.get("listing_id") or self.listing_id
        self.subtitle_locales = data_source.get("subtitle_locales", []) or self.subtitle_locales
        self.playback = data_source.get("playback") or self.playback
        self.availability_notes = data_source.get("availability_notes") or self.availability_notes

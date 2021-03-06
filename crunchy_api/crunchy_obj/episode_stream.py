from typing import Optional

from .base_crunchyroll_object_interface import BaseCrunchyrollObjectInterface
from .streams import Streams
from .subtitles import Subtitle


class EpisodeStream(BaseCrunchyrollObjectInterface):
    def __init__(self, data_source: Optional[dict] = {}):
        self.audio_locale: Optional[str] = data_source.get("audio_locale")
        self.subtitles: dict[str, Subtitle] = {key: Subtitle(value) for key, value in data_source.get("subtitles", {}).items()}
        self.streams: Streams = Streams(data_source.get("streams", {}))
        self.bifs: list[str] = data_source.get("bifs", [])

    def load_data_source(self, data_source: dict):
        self.audio_locale = data_source.get("audio_locale") or self.audio_locale
        self.subtitles = {key: Subtitle(value) for key, value in data_source.get("subtitles", {}).items()}
        self.streams.load_data_source(data_source.get("streams", {}))
        self.bifs = data_source.get("bifs", []) or self.bifs

from typing import Optional

from crunchy_api.crunchy_obj.base_crunchyroll_object_interface import BaseCrunchyrollObjectInterface
from crunchy_api.crunchy_obj.stream import Stream


class Streams(BaseCrunchyrollObjectInterface):
    def __init__(self, data_source: Optional[dict] = {}):
        self.adaptive_dash: dict[str, Stream] = {key: Stream(value) for key, value in data_source.get("adaptive_dash", {}).items()}
        self.adaptive_hls: dict[str, Stream] = {key: Stream(value) for key, value in data_source.get("adaptive_hls", {}).items()}
        self.download_hls: dict[str, Stream] = {key: Stream(value) for key, value in data_source.get("download_hls", {}).items()}
        self.drm_adaptive_dash: dict[str, Stream] = {key: Stream(value) for key, value in data_source.get("drm_adaptive_dash", {}).items()}
        self.drm_adaptive_hls: dict[str, Stream] = {key: Stream(value) for key, value in data_source.get("drm_adaptive_hls", {}).items()}
        self.drm_download_hls: dict[str, Stream] = {key: Stream(value) for key, value in data_source.get("drm_download_hls", {}).items()}
        self.trailer_dash: dict[str, Stream] = {key: Stream(value) for key, value in data_source.get("trailer_dash", {}).items()}
        self.trailer_hls: dict[str, Stream] = {key: Stream(value) for key, value in data_source.get("trailer_hls", {}).items()}
        self.vo_adaptive_dash: dict[str, Stream] = {key: Stream(value) for key, value in data_source.get("vo_adaptive_dash", {}).items()}
        self.vo_adaptive_hls: dict[str, Stream] = {key: Stream(value) for key, value in data_source.get("vo_adaptive_hls", {}).items()}
        self.vo_drm_adaptive_dash: dict[str, Stream] = {key: Stream(value) for key, value in data_source.get("vo_drm_adaptive_dash", {}).items()}
        self.vo_drm_adaptive_hls: dict[str, Stream] = {key: Stream(value) for key, value in data_source.get("vo_drm_adaptive_hls", {}).items()}

    def load_data_source(self, data_source: dict):
        self.adaptive_dash = {key: Stream(value) for key, value in data_source.get("adaptive_dash", {}).items()}
        self.adaptive_hls = {key: Stream(value) for key, value in data_source.get("adaptive_hls", {}).items()}
        self.download_hls = {key: Stream(value) for key, value in data_source.get("download_hls", {}).items()}
        self.drm_adaptive_dash = {key: Stream(value) for key, value in data_source.get("drm_adaptive_dash", {}).items()}
        self.drm_adaptive_hls = {key: Stream(value) for key, value in data_source.get("drm_adaptive_hls", {}).items()}
        self.drm_download_hls = {key: Stream(value) for key, value in data_source.get("drm_download_hls", {}).items()}
        self.trailer_dash = {key: Stream(value) for key, value in data_source.get("trailer_dash", {}).items()}
        self.trailer_hls = {key: Stream(value) for key, value in data_source.get("trailer_hls", {}).items()}
        self.vo_adaptive_dash = {key: Stream(value) for key, value in data_source.get("vo_adaptive_dash", {}).items()}
        self.vo_adaptive_hls = {key: Stream(value) for key, value in data_source.get("vo_adaptive_hls", {}).items()}
        self.vo_drm_adaptive_dash = {key: Stream(value) for key, value in data_source.get("vo_drm_adaptive_dash", {}).items()}
        self.vo_drm_adaptive_hls = {key: Stream(value) for key, value in data_source.get("vo_drm_adaptive_hls", {}).items()}

from typing import Optional


class EpisodeLinks:
    def __init__(self, data_source: Optional[dict]):
        self.channel: Link = Link(data_source.get("episode/channel", {}))
        self.next_episode: Link = Link(data_source.get("episode/next_episode", {}))
        self.season: Link = Link(data_source.get("episode/season", {}))
        self.series: Link = Link(data_source.get("episode/series", {}))
        self.streams: Link = Link(data_source.get("streams", {}))


class Link:
    def __init__(self, data_source: dict):
        self.href: Optional[str] = data_source.get("href")

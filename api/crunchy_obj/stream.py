class Stream:
    def __init__(self, data_source: dict):
        self.hardsub_locale: str = data_source.get("hardsub_locale")
        self.url: str = data_source.get("url")
        self.vcodec: str = data_source.get("vcodec")

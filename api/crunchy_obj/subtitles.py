class Subtitle:
    def __init__(self, data_source: dict):
        self.locale: str = data_source.get("locale")
        self.url: str = data_source.get("url")
        self.format: str = data_source.get("format")

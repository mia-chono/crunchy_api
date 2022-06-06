class Image:
    def __init__(self, data_source: dict):
        self.width: int = data_source.get("width")
        self.height: int = data_source.get("height")
        self.type: str = data_source.get("type")
        self.source: str = data_source.get("source")

from .image import Image


class Images:
    def __init__(self, data_source: dict):
        self.poster_tall: list[Image] = [Image(item) for item in data_source.get("poster_tall", [[]])[0]]
        self.poster_wide: list[Image] = [Image(item) for item in data_source.get("poster_wide", [[]])[0]]
        self.thumbnail: list[Image] = [Image(item) for item in data_source.get("thumbnail", [[]])[0]]

from dataclasses import dataclass


@dataclass
class Asset:
    name: str


class Portfolio:
    def __init__(self) -> None:
        self._assets = []

    def add(self, name: str) -> Asset:
        asset = Asset(name)
        self._assets.append(asset)
        return asset

"""
data classes
"""
from dataclasses import dataclass


@dataclass
class Anime:
    """
data class for anime search returns

    title- str
    url- str
    episode_list-list
    episodes_url_list- dict
    """
    title: str
    url: str
    anime_image: str
    episode_list: list = None
    episodes_url_list: dict = None


@dataclass
class DownloadOrder:
    """
download url listing

    stream_sb_high- str
    dodostream- str
    stream_sb_normal- str
    stream_sb_low- str
    """
    stream_sb_high: str
    dodostream: str
    stream_sb_normal: str
    stream_sb_low: str


@dataclass
class Episode:
    """
data class for anime episode ids

    episode_number- int
    episode_ids- DownloadOrder
    episode_urls- DownloadOrder
    """
    episode_number: int
    episode_ids: DownloadOrder
    episode_urls: DownloadOrder


if __name__ == "__main__":
    pass

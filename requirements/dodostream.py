"""
scrape from dodostream
"""
import os
import keyboard
from requirements import config
from requirements.get_episodes_list import get_episodes_list_and_urls as \
    get_episodes_list_and_urls
from requirements.search_gogo_anime_term import search_ as search_
from requirements.get_video_ids import get_video_ids as get_video_ids
from requirements.page_load_return import page_process
import win32clipboard


def setClipboardData(data):
    """
set clipboard data
    :param data:
    """
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardText(data)
    win32clipboard.CloseClipboard()


def dodostream(anime_objet):
    """
scrape from dodostream and return dodostream_final
    :return:
    """
    episodes = anime_objet[list(anime_objet.keys())[0]]["episode urls"]
    episodes_list = list(episodes.keys())
    for key in episodes_list:
        try:
            print("episode:", key)
            key = str(key)
            link = episodes.get(key).get("dodostream")
            if link is None:
                print(anime_objet)
                input("please find url as an error will occur")
            else:
                print(link)
            try:
                page = page_process(episodes.get(key).get("dodostream"))
            except Exception as e:
                if e != e:
                    print(e)
                page = episodes.get(key).get("dodostream")
            page = str(page)
            page = page.split("\n")
            download_page_url = None
            for line in page:
                if "href=\"/download/" in line:
                    line = line.split("\"")[-2]
                    download_page_url = config.dodostream_url + line
                    episodes[key]["dodo download page"] = download_page_url
            if download_page_url is None:
                episodes[key]["dodo download page"] = episodes.get(key).get("dodostream")

            os.system("cls")
            print("dodostream loading episode:", key)
            print("dodostream page url:", episodes.get(key).get("dodostream"))
            print("download page:", episodes[key]["dodo download page"])
            setClipboardData(episodes[key]["dodo download page"])
            keyboard.wait("ctrl+v")
            print("paste success")
        except Exception as e:
            print(e)

    anime_objet[list(anime_objet.keys())[0]]["episode urls"] = episodes
    return anime_objet


if __name__ == "__main__":
    print(dodostream(get_video_ids(get_episodes_list_and_urls(search_(input("name : "))))))

"""
stream sb
"""
import time
from requirements.get_episodes_list import get_episodes_list_and_urls as \
    get_episodes_list_and_urls
from requirements.get_video_ids import get_video_ids as get_video_ids
from requirements.page_load_return import page_process
from requirements.search_gogo_anime_term import search_ as search_
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


def load_download_link(key, episodes):
    """load link"""
    # print(episodes.get(key).get("sbplay_normal_page"))
    # sb_download_page = None
    # try:
    #     sb_download_page = (episodes.get(key)).get("sbplay_high_page")
    #     if sb_download_page is None:
    #         raise KeyError
    # except KeyError:
    try:
        sb_download_page = (episodes.get(key)).get("sbplay_normal_page")
        if sb_download_page is None:
            raise KeyError
    except KeyError:
        sb_download_page = (episodes.get(key)).get("sbplay_low_page")
        if sb_download_page is None:
            return episodes, False
    # print(episodes)
    if sb_download_page is None:
        download_ = False
    else:
        download_ = None
    while download_ is None:
        print("waiting 10 seconds")
        time.sleep(10)
        print("searching")
        page = page_process(sb_download_page)
        episodes[key]["sbplay_download_page"] = sb_download_page
        print(episodes[key]["sbplay_download_page"])
        text = str(page).split("\n")
        for line in text:
            # print(line)
            if "Direct Download Link" in line:
                download_ = line.split("\"")[1]
                episodes[key]["sbplay_download"] = download_
                try:
                    episodes[key]["downloadable"].append(download_)
                except Exception as e:
                    if e != e:
                        pass
                    episodes[key]["downloadable"] = [download_]
                # print(download_)
        if download_ is None:
            print("please check site press enter to copy url")
            setClipboardData(sb_download_page)
            input("press enter upon visiting site and clicking button")
    return episodes, download_


def stream_sb(anime_objet):
    """
func
    :return:
    """
    episodes = anime_objet[list(anime_objet.keys())[0]]["episode urls"]
    episodes_list = list(episodes.keys())
    for key in episodes_list:
        # print(key)
        key = str(key)
        page = page_process(episodes.get(key).get("sbplay"))
        text = str(page).split("\n")
        for line in text:
            # print(line)
            if "Normal quality" in line:
                line = line.split("(")[1].split(")")[0].replace("'", "").replace(",", " ").split(" ")
                link_normal = f"https://sbplay.one/dl?op=download_orig&id={line[0]}&mode={line[1]}&hash={line[2]}"
                episodes[key]["sbplay_normal_page"] = link_normal
            # if "High quality" in line:
            #     line = line.split("(")[1].split(")")[0].replace("'", "").replace(",", " ").split(" ")
            #     link_high = f"https://sbplay.one/dl?op=download_orig&id={line[0]}&mode={line[1]}&hash={line[2]}"
            #     episodes[key]["sbplay_high_page"] = link_high
            if "Low quality" in line:
                line = line.split("(")[1].split(")")[0].replace("'", "").replace(",", " ").split(" ")
                link_low = f"https://sbplay.one/dl?op=download_orig&id={line[0]}&mode={line[1]}&hash={line[2]}"
                episodes[key]["sbplay_low_page"] = link_low
        # try:
        #     episodes.get(key).get("sbplay_low_page")
        # except Exception as e:
        #     if e != e:
        #         pass
        #     episodes[key]["sbplay_low_page"] = None
        # try:
        #     episodes.get(key).get("sbplay_high_page")
        # except Exception as e:
        #     if e != e:
        #         pass
        #     episodes[key]["sbplay_high_page"] = None
        # try:
        #     episodes.get(key).get("sbplay_normal_page")
        # except Exception as e:
        #     if e != e:
        #         pass
        #     episodes[key]["sbplay_normal_page"] = None
        print(key)
        loaded_link = False
        a = 1
        while not loaded_link:
            print("loading link")
            episodes, loaded_link = load_download_link(key, episodes)
            if loaded_link is False:
                print("link loading error")
            else:
                print(f"download link is {loaded_link}")
            a += 1
            if a == 10:
                break

    anime_objet[list(anime_objet.keys())[0]]["episode urls"] = episodes
    return anime_objet


if __name__ == "__main__":
    print(stream_sb(get_video_ids(get_episodes_list_and_urls(search_(str(input("name : ")).replace(" ", "%20"))))))

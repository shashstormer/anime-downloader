"""
scrape from goload
"""
from requirements.get_episodes_list import get_episodes_list_and_urls as \
    get_episodes_list_and_urls
from requirements.get_video_ids import get_video_ids as get_video_ids
from requirements.page_load_return import page_process
from requirements.search_gogo_anime_term import search_ as search_


def goload(anime_objet):
    """
func
    :return:
    """
    episodes = anime_objet[list(anime_objet.keys())[0]]["episode urls"]
    episodes_list = list(episodes.keys())
    for key in episodes_list:
        # print(key)
        key = str(key)
        page = page_process(episodes.get(key).get("goload"))
        text = str(page).split("\n")
        for line in text:
            if "storage.googleapis.com" in line:
                line = line.replace("<div class=\"dowload\"><a download=\"\" href=\"",  "")
                line = line.split("\"")[0]
                # print(line)
                if "720.mp4" in line:
                    episodes[key]["goload_720_download_url"] = line
                    episodes[key]["downloadable"].append(line)
                # if "1080.mp4" in line:
                #     episodes[key]["goload_1080_download_url"] = line
                #     episodes[key]["downloadable"].append(line)
                if "-sd.mp4" in line:
                    episodes[key]["goload_sd_download_url"] = line
                    episodes[key]["downloadable"].append(line)
    anime_objet[list(anime_objet.keys())[0]]["episode urls"] = episodes
    return anime_objet


if __name__ == "__main__":
    print(goload(get_video_ids(get_episodes_list_and_urls(search_(input("name : "))))))

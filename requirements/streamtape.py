"""
scrape streamtape
"""
from requirements.get_episodes_list import get_episodes_list_and_urls as \
    get_episodes_list_and_urls
from requirements.search_gogo_anime_term import search_ as search_
from requirements.get_video_ids import get_video_ids as get_video_ids
from requirements.page_load_return import page_process


def streamtape(anime_objet):
    """
scrape from dodostream and return dodostream_final
    :return:
    """
    episodes = anime_objet[list(anime_objet.keys())[0]]["episode urls"]
    episodes_list = list(episodes.keys())
    for key in episodes_list:
        print(key)
        key = str(key)
        page = page_process(episodes.get(key).get("streamtape"))
        page = str(page)
        page = page.split("\n")
        for line in page:
            # print(line)
            if "https:\/\/thumb.tapecontent.net\/remotecaption\/" in line:
                line = line.split("https:\/\/thumb.tapecontent.net\/remotecaption\/")[1]
                line = line.split("\"")[0]
                streamtape_id = episodes.get(key).get("streamtape").split("v/")[1]

                line = f"https://streamtape.com/get_video?id={streamtape_id}&{line}&stream=1"
                episodes[key]["streamtape_download"] = line
                episodes[key]["downloadable"].append(line)

    anime_objet[list(anime_objet.keys())[0]]["episode urls"] = episodes
    return anime_objet


if __name__ == "__main__":
    print(streamtape(get_video_ids(get_episodes_list_and_urls(search_(input("name : "))))))

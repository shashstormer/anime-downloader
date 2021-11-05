"""
get video ids for the videos on gogoanime.vc
"""
from requirements.get_episodes_list import get_episodes_list_and_urls
from requirements.search_gogo_anime_term import search_
from requirements.page_load_return import page_process


def get_video_ids(anime_objet):
    """
function to get video ids from a gogoanime page
:var anime_objet: the object that contains the anime details
    :return:
    """

    episodes = anime_objet[list(anime_objet.keys())[0]]["episode urls"]
    episodes_list = list(episodes.keys())
    for key in episodes_list:
        print(f"getting download links for episode {key}")
        ep_url = episodes[key].get("episode url")
        ep_page = page_process(ep_url)
        ep_page = str(ep_page)
        ep_page = ep_page.split("\n")
        for line in ep_page:
            if "https://gogoplay1.com/download?id=" in line:
                # print(line)
                line = line.split("href=\"")[1].split("\"")[0]
                line = episodes[key]["goload"] = f"{line}"
                print(f"{line}")

            if "<a data-video=\"https://" in line:
                line = line.split("\"")[1]
                if "streamtape.com/e" in line:
                    line = line.split("streamtape.com/e/")[1]
                    line = line.split("/")[0]
                    line = episodes[key]["streamtape"] = f"https://streamtape.com/v/{line}"
                if "sbplay" in line:
                    # print(line)
                    line = line.split(".html")[0]
                    line = line.split("e/")[1]
                    line = episodes[key]["sbplay"] = f"https://tubesb.com/d/{line}"
                if "dood.la/" in line:
                    line = line.replace("/e/", "/d/")
                    line = episodes[key]["dodostream"] = f"{line}"
                if "embedsito" in line:
                    line = line.replace("/v/", "/f/")
                    line = episodes[key]["xstream"] = f"{line}"
                if "dood.la/" in line:
                    print(line)
    anime_objet[list(anime_objet.keys())[0]]["episode urls"] = episodes
    return anime_objet


if __name__ == "__main__":
    print(get_video_ids(get_episodes_list_and_urls(search_("mairimashita"))))

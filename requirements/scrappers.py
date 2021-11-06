"""
call all scrappers
"""
from requirements.streamsb import stream_sb as stream_sb
from requirements.get_episodes_list import get_episodes_list_and_urls as \
    get_episodes_list_and_urls
from requirements.search_gogo_anime_term import search_ as search_
from requirements.get_video_ids import get_video_ids as get_video_ids
# from requirements.goload import goload as goload
# from requirements.streamtape import streamtape as streamtape


def scrape(anime_object):
    """

    :param anime_object:
    """

    for key in anime_object[list(anime_object.keys())[0]]["episode urls"]:
        anime_object[list(anime_object.keys())[0]]["episode urls"][key]["downloadable"] = []
    anime_objet = anime_object
    try:
        anime_object = stream_sb(anime_object)
        anime_objet = anime_object
    except Exception as e:
        if e != e:
            print(e)
        anime_object = anime_objet
    return anime_object


if __name__ == "__main__":
    print(scrape(get_video_ids(get_episodes_list_and_urls(search_(input("name : "))))))

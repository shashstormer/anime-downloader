"""
call all scrappers
"""
# from requirements.streamsb import stream_sb as stream_sb
from requirements.get_episodes_list import get_episodes_list_and_urls as \
    get_episodes_list_and_urls
from requirements.search_gogo_anime_term import search_ as search_
from requirements.get_video_ids import get_video_ids as get_video_ids
from requirements.dodostream import dodostream as dodostream
# from requirements.streamtape import streamtape as streamtape


def loading_error(anime_object, episode, loader):
    """
    add errored episodes to anime_object
    """
    try:
        previous_errors = anime_object[list(anime_object.keys())[0]].get("error episodes")
        if previous_errors:
            previous_errors.append(episode)
        anime_object[list(anime_object.keys())[0]]["error episodes"] = previous_errors
        previous_errors_details = anime_object[list(anime_object.keys())[0]].get("error details")
        if previous_errors_details:
            previous_errors_details.append({f"{episode}": loader})
    except Exception as e:
        if e != e:
            print(e)
        anime_object[list(anime_object.keys())[0]]["error episodes"] = [episode]
        anime_object[list(anime_object.keys())[0]]["error details"] = [{f"{episode}": loader}]


def scrape(anime_object):
    """

    :param anime_object:
    """

    for key in anime_object[list(anime_object.keys())[0]]["episode urls"]:
        anime_object[list(anime_object.keys())[0]]["episode urls"][key]["downloadable"] = []
    anime_objet = anime_object
    try:
        anime_object = dodostream(anime_object)
        anime_objet = anime_object
    except Exception as e:
        key = 1
        if e != e:
            pass
        print(e)
        anime_object = anime_objet
        loading_error(anime_object, key, "dodostream")
        input("error while loading dodostream")
    return anime_object


if __name__ == "__main__":
    print(scrape(get_video_ids(get_episodes_list_and_urls(search_(input("name : "))))))

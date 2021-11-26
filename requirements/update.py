"""
downloads latest episode of ongoing animes
"""
import json
import os
from requirements.config import anime_folder
from requirements.download import download
from requirements.inner_main import other
from requirements.page_load_return import page_process
from requirements.scrappers import scrape


def get_episodes_list(anime_objet):
    """
    get episode list
    """
    url = anime_objet.get(list(anime_objet.keys())[0]).get("anime details page")
    # print(url)
    data = str(page_process(url))
    # print(data)
    data = data.split("\n")
    # ep_start, ep_end = 0, 0
    genres = []
    for line in data:
        # print(line)
        if "ep_start" and "ep_end" and "<a class=\"active\"" in line:
            # print(line)
            line = line.split(">")[1]
            line = line.replace("</a", "")
            # if int(ep_start) == 0:
            #     ep_start = 1
            ep_end = line.split("-")[1]
            anime_objet.get(list(anime_objet.keys())[0])["total episodes"] = ep_end
    try:
        folder_name = list(anime_objet.keys())[0].replace("-", " ")
        folder_name = folder_name.replace("-", " ")
        folder_name = folder_name.replace("\\", " ")
        folder_name = folder_name.replace("/", " ")
        folder_name = folder_name.replace("?", " ")
        folder_name = folder_name.replace("*", " ")
        folder_name = folder_name.replace("<", " ")
        folder_name = folder_name.replace("<", " ")
        folder_name = folder_name.replace("|", " ")
        folder_name = folder_name.replace("\"", " ")
        folder_name.strip(" ")
        folder_name.strip("\n")
        stat_fold = anime_objet.get(list(anime_objet.keys())[0]).get("status")
        try:
            os.mkdir(f"{anime_folder}/{stat_fold}/{folder_name}")
        except Exception as e:
            if e:
                pass
            if folder_name.endswith(" "):
                folder_name = folder_name[0:-1]
            folder_name += "/file_data.json"
            with open(f"{anime_folder}/{stat_fold}/{folder_name}") as file:
                json_load = json.load(file)
                # anime_objet.get(list(anime_objet.keys())[0]).get("status")
                last_downloaded = json_load.get(list(json_load.keys())[0]).get("last downloaded")
    except Exception as e:
        if e:
            pass
        last_downloaded = 0
    ep_end = int(anime_objet.get(list(anime_objet.keys())[0])["total episodes"])
    # ep_start = int(last_downloaded)
    # last_downloaded = int(last_downloaded)
    # print(f"there are {ep_end} episodes in {list(anime_objet.keys())[0]}")
    # print(f"you have last downloaded episode \"{last_downloaded}\"")
    # print(int(ep_end))
    # print(int(last_downloaded))
    # os.system("pause")
    if int(ep_end) == int(last_downloaded):
        print("latest downloaded already")
        raise Exception("already downloaded")
    else:
        ep_start = last_downloaded + 1
        ep_end = ep_end
        if ep_end < ep_start:
            ep_end = ep_start
        print("downloading latest")
        anime_objet.get(list(anime_objet.keys())[0])["last downloaded"] = ep_end
        ep_link = anime_objet.get(list(anime_objet.keys())[0]).get("anime details page")
        ep_link = ep_link.replace("category/", "")
        ep_link = f"{ep_link}-episode-"
        ep_links = {}
        anime_objet.get(list(anime_objet.keys())[0])["genres"] = genres
        for num in range(int(ep_start), int(ep_end) + 1):
            ep_links[f"{num}"] = {"episode url": ep_link + f"{num}"}
        anime_objet[list(anime_objet.keys())[0]]["episode urls"] = ep_links
        # print(anime_objet)
        return anime_objet


def get_video_ids(anime_objet):
    """
function to get video ids from a gogoanime page
:var anime_objet: the object that contains the anime details
    :return:
    """

    episodes = anime_objet[list(anime_objet.keys())[0]]["episode urls"]
    episodes_list = list(episodes.keys())
    for key in episodes_list:
        print(f"scrapping links for episode {key}")
        ep_url = episodes[key].get("episode url")
        ep_page = page_process(ep_url)
        ep_page = str(ep_page)
        ep_page = ep_page.split("\n")
        for line in ep_page:
            if "data-video=\"//goload.one/streaming.php?" in line:
                # print(line)
                line = line.split("data-video=\"")[1].split("\"")[0].replace("streaming.php", "download")
                # print(line)
                line = episodes[key]["goload"] = f"https:{line}"
                # print(f"{line}")

            if "<a data-video=\"https://" in line:
                line = line.split("\"")[1]
                if "streamtape.com/e" in line:
                    line = line.split("streamtape.com/e/")[1]
                    line = line.split("/")[0]
                    line = episodes[key]["streamtape"] = f"https://streamtape.com/v/{line}"
                if "sbplay" in line:
                    print(line)
                    line = line.split(".html")[0]
                    line = line.split("e/")[1]
                    line = episodes[key]["sbplay"] = f"https://tubesb.com/d/{line}"
                if "dood.la/" in line:
                    line = line.replace("/e/", "/d/")
                    line = episodes[key]["dodostream"] = f"{line}"
                if "embedsito" in line:
                    line = line.replace("/v/", "/f/")
                    line = episodes[key]["xstream"] = f"{line}"
                print(line)
    anime_objet[list(anime_objet.keys())[0]]["episode urls"] = episodes
    return anime_objet


def function():
    """
    main function
    """
    ongoing_anime_folders = []
    for main, animes, files in os.walk(anime_folder + "/Ongoing"):
        if main == anime_folder + "/Ongoing":
            for anime in animes:
                # print(anime_folder + "/Ongoing/" + anime + "/file_data.json")
                ongoing_anime_folders.append(anime_folder + "/Ongoing/" + anime + "/file_data.json")
    # print(ongoing_anime_folders)
    for file in ongoing_anime_folders:
        with open(file) as file_read:
            file_data: dict = json.load(file_read)
        ep_difference = int((file_data.get(list(file_data.keys())[0])).get("total episodes")) - int(
            (file_data.get(list(file_data.keys())[0])).get("last downloaded"))
        print("\n\n\n")
        try:
            os.system("cls")
            if ep_difference < 30:
                print("name : ", list(file_data.keys())[0])
                print("\n\n\n")
                data = get_episodes_list(file_data)
                data = get_video_ids(data)
                data = scrape(data)
                old(data)
            else:
                print("skipped", list(file_data.keys())[0])
        except Exception as e:
            print(e)


def old(anime_object: dict = None):
    """
    pass
    """
    data = anime_object
    # print(data)
    folder_name = list(data.keys())[0].replace("-", " ")
    folder_name = folder_name.replace("-", " ")
    folder_name = folder_name.replace("\\", " ")
    folder_name = folder_name.replace("/", " ")
    folder_name = folder_name.replace("?", " ")
    folder_name = folder_name.replace("*", " ")
    folder_name = folder_name.replace("<", " ")
    folder_name = folder_name.replace("<", " ")
    folder_name = folder_name.replace("|", " ")
    folder_name = folder_name.replace("\"", " ")
    folder_name.strip(" ")
    folder_name.strip("\n")
    stat_fold = data.get(list(data.keys())[0]).get("status")
    try:
        os.mkdir(f"{anime_folder}/{stat_fold}/{folder_name}")
    except Exception as e:
        if e:
            pass
    if folder_name.endswith(" "):
        folder_name = folder_name[0:-1]
    other.json_writer(f"{anime_folder}/{stat_fold}/{folder_name}", data)
    data = download(anime_object)
    return data


if __name__ == "__main__":
    function()

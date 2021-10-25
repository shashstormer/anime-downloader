"""
get episodes list from gogoanime
"""
import json
import os

from requirements.config import anime_folder
from requirements.page_load_return import page_process
from requirements.search_gogo_anime_term import search_


def get_episodes_list_and_urls(anime_objet):
    """
    gets the episodes list for the anime
    :return:
    """
    url = anime_objet.get(list(anime_objet.keys())[0]).get("anime details page")
    # print(url)
    data = str(page_process(url)).split("\n")
    ep_start, ep_end = 0, 0
    genres = []
    next_line_read = False
    status = False
    Type = False
    for line in data:
        # print(line)
        # if "" in line:
        #     line = line.split("")

        if next_line_read:
            # print(line)
            line = line.split(">")[1].split("<")[0]
            # print(line)
            if status:
                anime_objet.get(list(anime_objet.keys())[0])["status"] = line
            elif Type:
                anime_objet.get(list(anime_objet.keys())[0])["release time"] = line
            next_line_read = False

        if "<p class=\"type\"><span>Type: </span>" in line:
            next_line_read = True
            Type = True

        if "<p class=\"type\"><span>Other name: </span>" in line:
            line = line.split(">")[1].split("<")[0].split(",")
            anime_objet.get(list(anime_objet.keys())[0])["other names"] = line

        if "<p class=\"type\"><span>Status: </span>" in line:
            next_line_read = True
            status = True

        if "https://gogoanime.vc/genre/" in line:
            line = line.split("\"")
            for genre in line:
                if "https://gogoanime.vc/genre/" in genre:
                    genre = genre.split("/")[-1]
                    genres.append(genre)
        if "<p class=\"type\"><span>Plot Summary:" in line:
            line = line.split("</span>")[1]
            line = line.split(".\r")

            # line.replace(".\r", "")
            line_ = line[0].split(" ")
            line__ = ""
            word_number = 0
            # print(line)
            # print(line_)
            for word in line_:
                # print(word)
                line__ += word + " "
                word_number += 1
                if word_number == 10:
                    line__ += "\n"
                    word_number = 0

            print(line__)
            anime_objet.get(list(anime_objet.keys())[0])["description"] = line__

        last_downloaded = 0
        if "ep_start" and "ep_end" and "<a class=\"active\"" in line:
            # print(line)
            line = line.split(">")[1]
            line = line.replace("</a", "")
            # print(line)
            # ep_start = line.split("-")[0]
            if int(ep_start) == 0:
                ep_start = 1
            try:
                ep_end = line.split("-")[1]
            except IndexError:
                ep_end = line.split("-")[0]
            anime_objet.get(list(anime_objet.keys())[0])["total episodes"] = ep_end
            anime_objet.get(list(anime_objet.keys())[0])["last downloaded"] = "unknown"
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
                print(e)
                if e:
                    pass
                last_downloaded = 0

            print(f"there are {ep_end} episodes in {list(anime_objet.keys())[0]}")
            print(f"you have last downloaded episode \"{last_downloaded}\"")

            # todo: to show last downloaded episode
            if int(ep_end) > 0:
                ep_start = int(input("start: "))
                ep_end = int(input("end: "))
                if ep_end < ep_start:
                    ep_end = ep_start
            anime_objet.get(list(anime_objet.keys())[0])["last downloaded"] = ep_end
            os.system("cls")
            # print(ep_end)
            # print(ep_start)
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


if __name__ == "__main__":
    search = search_("overlord")
    # print(search)
    search = get_episodes_list_and_urls(search)
    print(search)

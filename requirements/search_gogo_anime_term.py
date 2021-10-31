"""
search gogoanime for a keyword
"""
import os

from requirements.page_load_return import page_process
from requirements.config import anime_folder


def search_(term):
    """
search gogoanime for term
    :param term:
    :return: {anime_name: {title: str, image cover: UrlImg, anime details page: url,
                              release date: int}}
    """
    url = f"https://gogoanime.pe//search.html?keyword={term}"
    # page_process(url).findAll('div', {'class': 'main_body'})
    search = page_process(url).findAll('div', {'class': 'last_episodes'})
    # print(len(search))
    search = search[0]
    # print(search)
    animes = {}
    search = str(search).split("</li>")
    for anime in search:
        try:
            anime = (anime.split("<div class=\"img\">"))[1].split("\n")
            anime.pop(3)
            # anime.pop()
            anime_details = []
            anime_name = None
            for ani in anime:
                if ani == anime[1]:
                    ani = ani.replace("<a href=\"/category/", "").split("\"")[0]
                    anime[1] = ani
                    anime_name = ani
                    # print(ani)
                if ani == anime[2]:
                    ani = ani.split("=")[2]
                    ani = ani.replace("\"", "")
                    # ani = ani.replace("/", "")
                    ani = ani.replace(">", "")
                    ani = ani[0:-1]
                    anime[2] = ani
                    # print(ani)
                if "<p class=\"name\"><a href=\"" in ani:
                    ani = ani.replace("<p class=\"name\"><a href=\"", "")
                    ani = ani.split("\"")[0]
                    ani = "https://gogoanime.pe" + ani
                if " Released:" in ani:
                    ani = ani.replace(" ", "")
                    ani = ani.split(":")[1]
                    ani = ani.replace("</p>", "")
                if "</div>" in ani:
                    pass
                elif "<p class=\"released\">" == ani:
                    pass
                else:
                    if ani:
                        anime_details.append(ani)
                    # print(ani)
                    if anime_name is not None:
                        animes[anime_name] = anime_details
        except Exception as e:
            print(e)

    for AnimeNames in animes:
        details = animes.get(AnimeNames)
        animes[AnimeNames] = {"title": details[0], "image cover": details[1], "anime details page": details[2],
                              "release date": details[3]}
    for anime_names in animes:
        # print(anime_names, end=" ")
        # print(_search_.get(anime_names).get("release date"))
        if animes.get(anime_names).get("release date") == "                                                      " \
                                                          "     " \
                                                          "                          ":
            animes[anime_names]["release date"] = "upcoming"
        # print(animes.get(anime_names).get("release date"))
    anime_number = 1
    key_ = list(animes.keys())
    for anime in key_:
        print(anime_number, end=" ")
        anime_number += 1
        details_anime = (animes.get(anime))
        print(details_anime.get("title") + "   " + details_anime.get("release date"))
    select_number = int(input("please select : ")) - 1
    anime_selected = {key_[select_number]: animes.get(key_[select_number])}
    data = anime_selected
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
    files_check = []
    for MainFolder, SubFolder, files in os.walk(anime_folder):
        for Sub in SubFolder:
            # print([MainFolder, SubFolder, Sub])
            # if inp.replace("-", " ").lower() in Sub.replace("-", " ").lower():
            # print(SubFolder)
            Sub_orignal = Sub
            Sub = Sub.replace("-", " ")
            if Sub == folder_name:
                files_check.append(fr"{MainFolder}\{Sub_orignal}")
    a = 1
    print("existing folders are :")
    for file in files_check:
        print(a, ". ", file)
        a += 1
    inp = input("press enter to continue...(type exit to stop)")
    if inp == "exit":
        os.kill(os.getpid(), 9)
    # print(anime_selected)
    # print(animes)
    return anime_selected


if __name__ == "__main__":
    _search_ = search_(input("name: "))

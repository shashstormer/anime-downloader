"""
package for dwlder_23_9_21
"""
from requirements.scrappers import *
from requirements.search_gogo_anime_term import search_ as search_
from requirements.get_video_ids import get_video_ids as get_video_ids
from requirements.program_name_start import program_name
from requirements.download import *
import json
from requirements.config import anime_folder


class other:
    """
other functions not basic to program
    """

    def __init__(self, programs_name="downloader"):
        self.program_name = programs_name

    def name(self):
        """
        prints name of program in a beautiful manner
        """
        program_name(self.program_name).__print__()

    @staticmethod
    def json_writer(location, anime_objects):
        """
writes the details to a json file
        :param anime_objects: final order return
        :param location: folder of anime
        :return:
        """
        final_data = anime_objects
        try:
            with open(f"{location}/file_data.json", "rt") as file:
                file.close()
        except Exception as e:
            print(e)
            open(f"{location}/file_data.json", "wt")
        try:
            with open(f"{location}/file_data.json", "rt") as file:
                # file = file.read()
                final_data = json.load(file)
            old_episodes_list = list((final_data[list(final_data.keys())[0]]["episode urls"]).keys())
        except Exception as e:
            old_episodes_list = []
            if e != e:
                print(e)
        episodes = anime_objects[list(anime_objects.keys())[0]]["episode urls"]
        episodes_list = list(episodes.keys())
        for episode in episodes_list:
            if episode not in old_episodes_list:
                final_data[list(anime_objects.keys())[0]]["episode urls"][episode] = episodes.get(episode)
            else:
                pass
        final_data[list(anime_objects.keys())[0]]["total episodes"] = \
            anime_objects[list(anime_objects.keys())[0]]["total episodes"]
        final_data[list(anime_objects.keys())[0]]["last downloaded"] = \
            anime_objects[list(anime_objects.keys())[0]]["last downloaded"]
        final_data[list(anime_objects.keys())[0]]["status"] = \
            anime_objects[list(anime_objects.keys())[0]]["status"]

        with open(f"{location}/file_data.json", "w") as file:
            json.dump(final_data, file, indent=4)


class main:
    """
main functions
    """

    @staticmethod
    def search(term):
        """
    order 1
search gogoanime for term
:param term: anime name
        :return: order 1
        """
        term = term.replace(" ", "%20")
        return search_(term)

    @staticmethod
    def video_ids_load(anime_object):
        """
        order 3
        :param anime_object: order 2 return
        :return: order 3
        """
        return get_video_ids(anime_object)

    @staticmethod
    def video_urls_load(anime_object):
        """
        order 2
        :param anime_object: order 1 return
        :return: order 2 return
        """
        return get_episodes_list_and_urls(anime_object)

    @staticmethod
    def download_links_scrape(anime_object):
        """
        order 4
        :param anime_object: order 3 return
        :return: order 4 OR final order
        """
        return scrape(anime_object)

    @staticmethod
    def download_files(anime_object):
        """
        downloads videos
        :param anime_object: final order return
        :return: None
        """
        return download(anime_object)

    def full_function(self, term):
        """
        order 0
        :param term: name of anime
        :return: final order and complete downloads
        """
        data = self.download_links_scrape(self.video_ids_load(self.video_urls_load
                                                              (self.search(term)
                                                               )))
        print(data)
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
            print(e)
        if folder_name.endswith(" "):
            folder_name = folder_name[0:-1]
        other.json_writer(f"{anime_folder}/{stat_fold}/{folder_name}", data)
        data = self.download_files(data)
        return data


if __name__ == "__main__":
    other()
    print("\n")
    print(main().full_function(input("name : ")))

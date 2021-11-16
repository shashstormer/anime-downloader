"""
download video url
"""
import os
import win32clipboard
from requirements.config import anime_folder as dl_folder


def setClipboardData(data):
    """
set clipboard data
    :param data:
    """
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardText(data)
    win32clipboard.CloseClipboard()


class dwlder:
    """
class for download functions
    """

    def __init__(self, anime_object=None):
        self.anime_object = anime_object
        self.details = {}

    def anime_object_separator(self):
        """

        :return:
        """
        anime_episodes = self.anime_object.get(list(self.anime_object.keys())[0]).get("episode urls")
        for episode in anime_episodes:
            # print(episode)
            details = anime_episodes.get(episode)
            details_ = [(str(list(self.anime_object.keys())[0]).strip(" ")), episode,
                        details.get("downloadable")]
            self.details[str(episode)] = details_
            # print(details_)

    def anime_object_download_link_get_and_download(self):
        """

        :return:
        """
        anime_episodes = self.anime_object.get(list(self.anime_object.keys())[0]).get("episode urls")
        if anime_episodes == anime_episodes:
            pass
        for details in self.details:
            details = self.details.get(details)
            folder_name, episode_number, download_link = details
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
            download_main_folder = dl_folder + "/" + self.anime_object.get(list(self.anime_object.keys())[0]).get("status")
            try:
                os.mkdir(fr"{download_main_folder}\\{folder_name}")
            except Exception as e:
                if e != e:
                    pass
            print("name : " + (list(self.anime_object.keys())[0]).replace("-", " "))
            print("total episodes :   " + self.anime_object.get(list(self.anime_object.keys())[0])["total episodes"])
            print(fr"episodes to download remaining : " + str(
                int(self.anime_object.get(list(self.anime_object.keys())[0])["last downloaded"]) - int(episode_number)))
            print("downloading episode : ", episode_number)
            if f"{episode_number}.mp4" in os.walk(
                    fr"{download_main_folder}\{folder_name}") and f"{episode_number}.mp4.aria2" not in \
                    os.walk(
                    fr"{download_main_folder}\{folder_name}"):
                break

            for download_ in download_link:
                file = []
                for main_folder, sub_folder, file in os.walk(fr"{download_main_folder}\{folder_name}"):
                    pass
                if (f"{episode_number}.mp4" in file) and (f"{episode_number}.mp4.aria2" not in file):
                    break
                if f"{episode_number}.mp4.crdownload" in file:
                    break
                # if f"{episode_number}.mp4.crdownload" in file:
                #     break
                try:
                    options = f'-x 10 --max-tries=5 --retry-wait=10 --check-certificate=false -d ' \
                              fr'"{download_main_folder}\{folder_name}" -o "{episode_number}.mp4" '
                    cmd = f'aria2c "{download_}" {options}'
                    os.system(cmd)
                    if f"{episode_number}.mp4" in file and f"{episode_number}.mp4.aria2" in file:
                        raise FutureWarning

                except Exception as e:
                    print(e)
                    link_choice = 0
                    try:
                        if not download_link:
                            pass
                        else:
                            links_number = len(download_link)
                            if links_number >= 2:
                                link_choice = 1
                        download_ = download_link[link_choice]
                        options = f'-x 10 --max-tries=5 --retry-wait=10 --check-certificate=false -d ' \
                                  fr'"{download_main_folder}\{folder_name}" -o "{episode_number}.mp4" '
                        cmd = f'aria2c "{download_}" {options}'
                        os.system(cmd)
                        if f"{episode_number}.mp4" in file and f"{episode_number}.mp4.aria2" in file:
                            raise FutureWarning
                    except Exception as err:
                        print(err)
                        print("manual trial")
                        print("url is")
                        download_ = download_link[link_choice]
                        print(download_)
                        input("press enter to set to clipboard")
                        setClipboardData(download_)
                        try:
                            os.remove(fr"{download_main_folder}\{folder_name}\{episode_number}.aria2")
                        except FileNotFoundError:
                            pass
                        if input("press enter to continue downloading...") == "open":
                            os.startfile(fr"{download_main_folder}\{folder_name}")

        return self.anime_object

    def auto_download(self):
        """

        :return:
        """
        self.anime_object_separator()
        return self.anime_object_download_link_get_and_download()


def download(anime_object):
    """
downloads the anime object files if non existent
    """
    return dwlder(anime_object).auto_download()


if __name__ == "__main__":
    import requirements.inner_main as main
    download(main.main().full_function(input("name : ")))

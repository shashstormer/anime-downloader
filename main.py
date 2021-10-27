"""
downloader made on 23-9-21
"""
import os

from requirements import inner_main, config

if config.anime_folder == "c:/users/user/downloads/anime":
    print("please set the variable anime_folder in config.py file located in requirements folder")
    input("press enter to exit...")
else:
    inner_main.other(config.program_name).name()
    try:
        try:
            os.mkdir(f"{config.anime_folder}/Completed")
        except FileExistsError:
            pass
        try:
            os.mkdir(f"{config.anime_folder}/Ongoing")
        except FileExistsError:
            pass
        try:
            os.mkdir(f"{config.anime_folder}/Upcoming")
        except FileExistsError:
            pass
        # print("\n")
        anime = input("enter anime name : ")
        if anime == "update":
            import requirements.update
            requirements.update.function()
        else:
            inner_main.main().full_function(anime)
    except Exception as e:
        print(e)

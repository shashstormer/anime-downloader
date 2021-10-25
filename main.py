"""
downloader made on 23-9-21
"""
from requirements import inner_main, config

if config.anime_folder == "c:/users/user/downloads/anime":
    print("please set the variable anime_folder in config.py file located in requirements folder")
    input("press enter to exit...")
else:
    inner_main.other(config.program_name).name()
    try:
        inner_main.main().full_function(input("enter anime name : "))
    except Exception as e:
        print(e)

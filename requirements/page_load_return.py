"""
load website and return beautiful soup thing
"""
from bs4 import BeautifulSoup
import urllib.request
import urllib3
import urllib3.request


def page_process(url: str):
    """
    :return soup data html parser
    :var url url of the page to be loaded
load page and return the beautiful soup processed data
    """
    print(url)
    user_agent = 'Chrome/92.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7)'
    headers = {'User-Agent': user_agent, 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
               'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
               'Accept-Encoding': 'none',
               'Accept-Language': 'en-US,en;q=0.8',
               'Connection': 'keep-alive'}
    request = urllib.request.Request(url=url, headers=headers)
    response = urllib.request.urlopen(request)
    data = response.read()
    soup = BeautifulSoup(data, "html.parser")
    return soup


def page_process_2():
    """
made using urllib3
    :return:
    """
    user_agent = 'Chrome/92.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7)'
    headers = {'User-Agent': user_agent, 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
               'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
               'Accept-Encoding': 'none',
               'Accept-Language': 'en-US,en;q=0.8',
               'Connection': 'keep-alive'}
    request = urllib3.request.RequestMethods(headers).request(None, None)
    if __name__ == "":
        request()
#     this part is not finished

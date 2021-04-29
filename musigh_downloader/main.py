import os
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from .musigh_downloader.spiders.musigh import MusighSpider


def get_download_path():
    if os.name == 'nt':
        import winreg
        sub_key = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders'
        downloads_guid = '{374DE290-123F-4565-9164-39C4925E467B}'
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, sub_key) as key:
            location = winreg.QueryValueEx(key, downloads_guid)[0]
        return location
    else:
        return os.path.join(os.path.expanduser('~'), 'downloads')


def main():
    download_folder = os.path.join(get_download_path(), 'musigh')
    settings = get_project_settings()
    settings.set('FILES_STORE', download_folder)
    process = CrawlerProcess(settings)
    process.crawl(MusighSpider)
    process.start()

# pyinstaller --onefile main.py --name MusighScraper.exe --icon musigh.ico
# python -m nuitka --onefile --plugin-enable=pylint-warnings --windows-onefile-tempdir main.py
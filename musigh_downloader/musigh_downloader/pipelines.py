# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import os
from urllib.parse import urlparse

from scrapy.pipelines.files import FilesPipeline
from scrapy.pipelines.images import ImagesPipeline


class MusighDownloaderPipeline(FilesPipeline):
    def file_path(self, request, response=None, info=None, *, item=None):
        file_name: str = request.url.split("/")[-3] + '/' + request.url.split("/")[-2] + '/' + request.url.split("/")[-1]
        return file_name

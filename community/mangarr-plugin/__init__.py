from plugins.base import MangaPluginBase


class TemplatePlugin(MangaPluginBase):
    languages = []

    def search_manga(self, query:str, language:str=None) -> dict:
        return {}

    def get_manga(self, arguments:dict) -> dict:
        return {}
    
    def get_chapter(self, arguments:dict) -> dict:
        return {}
    
    def get_chapters(self, arguments:dict) -> list[dict]:
        return []
    
    def get_pages(self, arguments:dict) -> list[dict]:
        return []
from BuildingModel import BuildingModel
from BuildingRepository import BuildingRepository
from bs4 import BeautifulSoup
from typing import Tuple
import requests

class BuildingScrapingRepository(BuildingRepository):
    url: str = 'https://www.idealista.com/en/venta-viviendas/alcala-de-henares/ensanche/'

    def find_buildings(self) -> Tuple[BuildingModel]:
        html = requests.get(self.url).text
        soup = BeautifulSoup(html, 'html.parser')
        print(soup)

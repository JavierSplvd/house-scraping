from abc import ABC, abstractmethod
from typing import Tuple
from BuildingModel import BuildingModel

class BuildingRepository(ABC):
    @abstractmethod
    def find_buildings(self) -> Tuple[BuildingModel]:
        pass
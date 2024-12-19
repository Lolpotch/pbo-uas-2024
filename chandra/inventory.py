from abc import ABC, abstractmethod

class Inventory(ABC):
    @abstractmethod
    def add_data(self):
        pass

    @abstractmethod
    def edit_data(self):
        pass

    @abstractmethod
    def delete_data(self):
        pass

    @abstractmethod
    def search_data(self):
        pass
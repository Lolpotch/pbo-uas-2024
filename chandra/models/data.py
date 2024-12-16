from abc import ABC, abstractmethod

class Data(ABC):
    @abstractmethod
    def TambahData(self):
        """Method to add data."""
        pass

    @abstractmethod
    def EditData(self):
        """Method to edit data."""
        pass

    @abstractmethod
    def HapusData(self):
        """Method to delete data."""
        pass

    @abstractmethod
    def CariData(self):
        """Method to search for data."""
        pass
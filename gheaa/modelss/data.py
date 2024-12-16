from abc import ABC, abstractmethod

class Data(ABC):
    @abstractmethod
    def tambah_data(self):
        pass

    @abstractmethod
    def edit_data(self):
        pass

    @abstractmethod
    def hapus_data(self):
        pass

    @abstractmethod
    def cari_data(self):
        pass
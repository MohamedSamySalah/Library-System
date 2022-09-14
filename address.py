class Address():
    def __init__(self,city,sate,country):
        self.__city = city
        self.__sate = sate
        self.__country = country
    @property
    def get_city(self):
        return self.__city
    @property
    def get_state(self):
        return self.__sate
    @property
    def get_country(self):
        return self.__country
    
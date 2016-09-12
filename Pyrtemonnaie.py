#!/usr/bin/env python3

from Datapoint import Datapoint

class Pyrtemonnaie:
    def __init__(self, path=""):
        self.__Path = path
        self.__Datapoints = []

    def get_path(self):
        pass

    def set_path(self, path):
        pass

    def get_datapoints(self):
        pass

    def count_datapoints(self):
        return len(self.__Datapoints)

    def sort_by_date(self):
        self.__Datapoints.sort(key= lambda d: d.Date)
        return

    Path = property(get_path, set_path)
    Datapoints = property(get_datapoints)
    Count = property(count_datapoints)
    
    def add_datapoint(self, datapoint):
        if type(datapoint) == str:
            d = Datapoint()
            d.parse(datapoint)
        elif type(datapoint) == Datapoint:
            self.__Datapoints.append(datapoint)

    def delete_datapoint(self, datapoint):
        pass

    def clear_pyrtemonnaie(self):
        pass
from statistics import mean
from collections import defaultdict

class UndergroundSystem:

    def __init__(self):
        # key = current cutomer id, value = tuple(station_name, t)
        self.checkins = dict()
        self.completed = dict()
    
    def _setDirectionValue(self, startStation: str, endStation: str, t: int) -> None:
        key = (startStation, endStation)
        if key not in self.completed:
            self.completed[key] = (t, 1)
        else:
            v, c = self.completed[key]
            self.completed[key] = (v + ((t - v)/(c + 1)), c + 1)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkins[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        checkinStation, checkinTime = self.checkins[id]
        self._setDirectionValue(checkinStation, stationName, t - checkinTime)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.completed[(startStation, endStation)][0]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
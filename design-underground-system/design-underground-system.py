from statistics import mean

class UndergroundSystem:

    def __init__(self):
        # key = current cutomer id, value = tuple(station_name, t)
        self.checkins = dict()
        # key = station_name, value = dict where key = station_name, value = list of travel times
        self.completed = dict()
    
    def _getOrCreateDirection(self, station_a: str, station_b: str) -> List[int]:
        if station_a not in self.completed:
            self.completed[station_a] = dict()
        
        if station_b not in self.completed[station_a]:
            self.completed[station_a][station_b] = list()
            # self.completed[station_b][station_a] = self.completed[station_a][station_b]
        
        return self.completed[station_a][station_b]

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkins[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        checkinStation, checkinTime = self.checkins[id]
        direction = self._getOrCreateDirection(checkinStation, stationName)
        direction.append(t - checkinTime)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        direction = self._getOrCreateDirection(startStation, endStation)
        return mean(direction)


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
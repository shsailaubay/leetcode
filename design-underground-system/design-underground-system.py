from collections import defaultdict

class UndergroundSystem:

    def __init__(self):
        # key = current cutomer id, value = tuple(station_name, t)
        self.checkins = dict()
        self.completed = defaultdict(lambda: [0, 0])

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkins[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        checkinStation, checkinTime = self.checkins.pop(id)
        self.completed[(checkinStation, stationName)][0] += t - checkinTime
        self.completed[(checkinStation, stationName)][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.completed[(startStation, endStation)][0] / self.completed[(startStation, endStation)][1]
 
# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
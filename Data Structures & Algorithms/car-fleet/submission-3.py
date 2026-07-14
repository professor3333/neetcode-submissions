class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse = True)
        fleet_time = []
        for pos, spd in cars:
            time = (target - pos)/spd
            fleet_time.append(time)
            if len(fleet_time) >= 2 and fleet_time[-1] <= fleet_time[-2]:
                fleet_time.pop()
        return len(fleet_time)
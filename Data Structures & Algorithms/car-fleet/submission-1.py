class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse = True)
        fleet_times = []
        for pos, spd in cars:
            time_to_finish = (target - pos)/spd
            fleet_times.append(time_to_finish)
            if len(fleet_times) >= 2 and fleet_times[-1] <= fleet_times[-2]:
                fleet_times.pop()
        return len(fleet_times)
"""
Where you input region control methods
"""

"""
Main Method - Do Not Edit Headers

Returns dict with cycle times
Keys - Road Name
Value - Cycle Time
{'RoadNameN_S': 5, 'RoadNameE_W': 5}
"""
def congestion(lane):
    cars = 0
    if len(lane) != 0:
        for x in lane:
            if x != 0:
                cars+=1
        return cars/len(lane)
def run(time, intersection):
    # mRoads = intersection.roads
    # compare = {}
    # for x in mRoads:
    #     sum = 0
    #     for y in mRoads[x]['enter']:
    #         for i in y.queue:
    #             sum+=congestion(i)
    #             #print(y, congestion(i))
    #     for z in mRoads[x]['exit']:
    #         for i in z.queue:
    #             sum+=congestion(i)
    #             #print(z, congestion(i))
    #     compare[x] = sum
    # list = []
    # for x in mRoads:
    #     list.append(x)
    # x, y = list[0], list[1]
    # arr = {}
    # #print(compare[x], compare[y])
    # if compare[x] > compare[y]:
    #     arr[x] = intersection.cycle_times[x] + 1
    #     arr[y] = intersection.cycle_times[y] - 1
    # if compare[y] > compare[x]:
    #     arr[x] = intersection.cycle_times[x] - 1
    #     arr[y] = intersection.cycle_times[y] + 1
    # if compare[y] is compare[x]:
    #     if compare[y] >= 1.5:
    #         arr[x] = intersection.cycle_times[x] + 1
    #         arr[y] = intersection.cycle_times[y] + 1
    #     else:
    #         if intersection.cycle_times[x] > 45:
    #             arr[x] = intersection.cycle_times[x] - 1
    #         if intersection.cycle_times[y] > 45:
    #             arr[y] = intersection.cycle_times[y] - 1
    # print(intersection.cycle_times, compare[x], compare[y], arr)
    # return arr
    return None

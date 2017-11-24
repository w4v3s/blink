"""
Intersection Object

"""
from dependencies import *
from input_objects import intersection_control

class Intersection(threading.Thread):
    def __init__(self, tick, name, region, region_com, directions = 4):
        threading.Thread.__init__(self)

        self.id = uuid.uuid4()
        self.name = name
        self.region = region
        self.region_com = region_com
        self.directions = directions

        self.tick = tick
        self.com = queue.Queue()
        self.input_road = [0 for d in range(directions)]
        self.exit = [0 for d in range(directions)]

        self.lights = ["red" for d in range(directions)]
        self.cycleTimes = [10,10,10,10]
        self.effCycleTimes = [sum(self.cycleTimes[0,x+1]) for x in range(len(self.cycleTimes))]
    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    """
    Attaching Roads
    Attempts to find a road in the opposite direction thats already been attached
    If not, then attaches to the end of the array
    """
    def search(self, road, road_list):
        ind = False
        for r in range(len(road_list)):
            if road_list[r] and road.name == road_list[r].name:
                ind = r
                print("\tFOUND")
        return ind
    def attach_input_road(self,road):
        if road in self.input_road:
            cprint("WARNING: Attempted to add preexisting input road to intersection.",'yellow')
            return

        dir = self.search(road, self.exit)
        if dir:
            temp = None

            if dir < len(self.input_road):
                temp = self.input_road.pop(dir)
                self.input_road.append(temp)

            self.input_road.insert(dir, road)
        else:
            for d in range(len(self.exit)):
                if self.input_road[d] == 0:
                    self.input_road[d] = road
                    break

    def attach_exit(self, road):
        if road in self.exit:
            cprint("WARNING: Attempted to add preexisting exit road to intersection.",'yellow')
            return

        dir = self.search(road, self.input_road)
        if dir:

            temp = None
            if dir < len(self.exit):
                temp = self.exit.pop(dir)
                self.exit.append(temp)

            self.exit.insert(dir, road)
        else:
            for d in range(len(self.exit)):
                if self.exit[d] == 0:
                    self.exit[d] = road
                    break
        """
        Light management
        """
        def updateCycles(self, tick):
            currentCycle = tick%sum(self.cycleTimes)
            for x in range(self.effCycleTimes):
                if(currentCycle<self.effCycleTimes[x]):
                    currentGreenLight = self.lights[x]
            return currentGreenLight

        def changeCycleTimes(self, newLights):
            self.cycleTimes = newLights
            self.effCycleTimes = [sum(self.cycleTimes[0,x+1]) for x in range(len(self.cycleTimes))]]

        def createLightMap(self, road_network):
            print(road_network)
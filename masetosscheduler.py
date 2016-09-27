from copy import copy
from math import ceil
from random import choice, sample


class Day:
    
    def __init__(self, Name):
        self.Name = Name
        self.AMSandwichMaker = None
        self.AMGrill = None
        self.AMHelper = None
        self.AMServers = None
        self.PMSandwichMaker = None
        self.PMGrill = None
        self.PMHelper = None
        self.PMServers = None
        self.PMDinners = None
        
    def return_busy_persons(self):  # Want a better name
        '''Return Person Objects who are already scheduled in the Day object.'''
        BusyPersons = set()
        positions = [self.AMSandwichMaker, self.AMGrill, self.AMHelper,
                     self.AMSevers, self.PMSandwichMaker, self.PMGrill,
                     self.PMHelper, self.PMServers, self.PMDinners]
        positions = [item for item in positions if item != None]
        for position in positions:
            if type(position) == list:
                for server in position:
                    BusyPersons.add(server)
            else:
                BusyPersons.add(position)
        return BusyPersons
                    
                    
    def GenerateAndSetServers(self, AMServerList, PMServerList, Total):
        PMServerList = copy(PMServerList)
        AMTotal = max(int(Total / 2), 2)
        PMTotal = ceil(Total / 2) # Handles odd number of input servers
        self.AMServers = sample(AMServerList, AMTotal)
        if Total > 2: # This handles Monday and Tuesday.
            for server in self.AMServers:
                if server in PMServerList:
                    PMServerList.remove(server)
            self.PMServers = sample(PMServerList, PMTotal)
        
    def GenerateAndSetKitchen(self, SandwichMakerList, GrillerList, HelperList, DinnerList):
        # Make Shallow Copies of Data
        SandwichMakerList = copy(SandwichMakerList)
        GrillerList = copy(GrillerList)
        HelperList = copy(HelperList)
        DinnerList = copy(DinnerList)
    
        # Set SandwichMakers
        if self.AMSandwichMaker != Lisa:
            self.AMSandwichMaker, self.PMSandwichMaker = sample(SandwichMakerList, 2)
        else:
            self.PMSandwichMaker = choice(SandwichMakerList)
        
        # Set Grillers
        for sandwichmaker in [self.AMSandwichMaker, self.PMSandwichMaker]:
            if sandwichmaker in GrillerList:
                GrillerList.remove(sandwichmaker)
        if self.AMGrill != Tim:
            self.AMGrill, self.PMGrill = sample(GrillerList, 2)
        else:    
            self.PMGrill = choice(GrillerList)
        
        #Set Helpers
        for person in [self.AMSandwichMaker, self.AMGrill, self.PMSandwichMaker, self.PMGrill]:
            if person in HelperList:
                HelperList.remove(person)
        self.AMHelper, self.PMHelper = sample(HelperList, 2)
        
        #Set Dinners
        for person in [self.PMSandwichMaker, self.PMGrill, self.AMHelper, self.PMHelper]:
            if person in DinnerList:
                DinnerList.remove(person)
        if DinnerList == []:
            self.PMDinners = EMPTY
        else:
            self.PMDinners = choice(DinnerList)
   

class Person:

    def __init__(self, Name):
        self.Name = Name
        self.CanDoSandwiches = None
        self.CanDoGrill = None
        self.CanDoHelper = None
        self.CanDoDinners = None
        
        
def printout_test():
    for day in Week:
        print('--', day.Name,' Staff --')
        print('AMSandwichMaker: ', day.AMSandwichMaker.Name)
        print('AMGrill: ', day.AMGrill.Name)
        print('AMHelper: ', day.AMHelper.Name)
        for server in day.AMServers:
            print('AMServer: ', server.Name)
        if day in [Wednesday, Thursday, Friday, Saturday]:
            print('PMSandwichMaker: ', day.PMSandwichMaker.Name)
            print('PMGrill: ', day.PMGrill.Name)
            print('PMHelper: ', day.PMHelper.Name)
            print('PMDinners: ', day.PMDinners.Name)
            for server in day.PMServers:
                print('PMServer: ', server.Name)
        print('\n')
            
def set_schedule(WeekList):
    for day in WeekList:
        if day in [Monday, Tuesday]:
            day.AMSandwichMaker = Lisa
            day.AMGrill = Tim
            day.AMHelper = choice(Helpers)
            day.GenerateAndSetServers(AMServers, PMServers, 2)
        if day in [Wednesday, Thursday]:
            day.AMSandwichMaker = Lisa
            day.AMGrill = Tim
            day.GenerateAndSetKitchen(SandwichMakers, Grillers, Helpers, Dinners)
            day.GenerateAndSetServers(AMServers, PMServers, 4)
            day.PMDinners = EMPTY
        if day == Friday:
            day.AMSandwichMaker = Lisa
            day.AMGrill = Tim
            day.GenerateAndSetKitchen(SandwichMakers, Grillers, Helpers, Dinners)
            day.GenerateAndSetServers(AMServers, PMServers, 6)
        if day == Saturday:
            day.GenerateAndSetKitchen(SandwichMakers, Grillers, Helpers, Dinners)
            day.GenerateAndSetServers(AMServers, PMServers, 4)
            day.PMDinners = EMPTY
        
Monday = Day('Monday')
Tuesday = Day('Tuesday')
Wednesday = Day('Wednesday')
Thursday = Day('Thursday')
Friday = Day('Friday')
Saturday = Day('Saturday')
Week = [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday]

Tammy = Person('Tammy')
Lisa = Person('Lisa')
Sherie = Person('Sherie')
Tim = Person('Tim')
Peggy = Person('Peggy')
Katie = Person('Katie')
Alex = Person('Alex')
Jamie = Person('Jamie')
Rhiannon = Person('Rhiannon')
Kara = Person('Kara')
Nathan = Person('Nathan')
Johnny = Person('Johnny')
Joe = Person('Joe')
Sara = Person('Sara')
EMPTY = Person('-EMPTY-') 

SandwichMakers = [Katie, Rhiannon, Joe]
Grillers = [Katie, Alex, Rhiannon, Nathan, Johnny, Joe]
Helpers = [Katie, Alex, Rhiannon, Kara, Nathan, Johnny, Joe]
AMServers = [Tammy, Sherie, Peggy, Jamie, Sara]
PMServers = [Jamie, Rhiannon, Kara, Nathan, Sara]
Dinners = [Alex, Rhiannon, Kara, Nathan, Johnny, Joe, Katie]

for sandwichMaker in SandwichMakers:
    sandwichMaker.CanDoSandwiches = True
for griller in Grillers:
    griller.CanDoGrill = True
for helper in Helpers:
    helper.CanDoHelper = True
for dinner in Dinners:
    dinner.CanDoDinner = True
    
   
set_schedule(Week)        
printout_test()

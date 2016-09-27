from copy import copy
from random import choice

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
        self.positions_not_filled = 0
        
    def busy_persons(self):
        '''Return Person Objects who are already scheduled in the Day object.'''
        BusyPersons = set()
        positions = [self.AMSandwichMaker, self.AMGrill, self.AMHelper,
                     self.AMServers, self.PMSandwichMaker, self.PMGrill,
                     self.PMHelper, self.PMServers, self.PMDinners]
        positions = [item for item in positions if item != None]
        for position in positions:
            if type(position) == list:
                for server in position:
                    BusyPersons.add(server)
            else:
                BusyPersons.add(position)
        return BusyPersons
        
    def set_position(self, position_list):
        position_list = copy(position_list)
        for person in self.busy_persons():
            if person in position_list:
                position_list.remove(person)
                
        try:
            return choice(position_list)
        except(IndexError):
            self.positions_not_filled += 1
            print('A position was not succesfully filled.')
            return EMPTY 
            
    def GenerateAndSetServers(self, AMTotal, PMTotal):
        self.AMServers = []
        self.PMServers = []
        for server in range(AMTotal):
            self.AMServers.append(self.set_position(AMServers))
        for server in range(PMTotal):
            self.PMServers.append(self.set_position(PMServers))
        
    def GenerateAndSetKitchen(self):
        if self.AMSandwichMaker == None:
            self.AMSandwichMaker = self.set_position(SandwichMakers)
        self.PMSandwichMaker = self.set_position(SandwichMakers)
        if self.AMGrill == None:
            self.AMGrill = self.set_position(Grillers)
        self.PMGrill = self.set_position(Grillers)
        self.AMHelper = self.set_position(Helpers)
        self.PMHelper = self.set_position(Helpers)
 

class Person:

    def __init__(self, Name):
        self.Name = Name

        
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
            try:
                print('PMDinners: ', day.PMDinners.Name)
            except(AttributeError):
                pass
            for server in day.PMServers:
                print('PMServer: ', server.Name)
        print('Positions not filled: ', day.positions_not_filled)
        print('\n')
            
def set_schedule(WeekList):
    for day in WeekList:
        if day in [Monday, Tuesday]:
            day.AMSandwichMaker = Lisa
            day.AMGrill = Tim
            day.AMHelper = day.set_position(Helpers)
            day.GenerateAndSetServers(AMTotal=2, PMTotal=0)
        if day in [Wednesday, Thursday]:
            day.AMSandwichMaker = Lisa
            day.AMGrill = Tim
            day.GenerateAndSetKitchen()
            day.GenerateAndSetServers(AMTotal=2, PMTotal=2)
        if day == Friday:
            day.AMSandwichMaker = Lisa
            day.AMGrill = Tim
            day.GenerateAndSetKitchen()
            day.GenerateAndSetServers(AMTotal=3, PMTotal=3)
            day.PMDinners = day.set_position(Dinners)
        if day == Saturday:
            day.GenerateAndSetKitchen()
            day.GenerateAndSetServers(AMTotal=2, PMTotal=2)
        
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

set_schedule(Week)
printout_test()

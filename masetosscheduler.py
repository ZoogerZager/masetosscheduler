from copy import copy
from random import choice

class Day:
    
    def __init__(self, Name):
        self.Name = Name
        self.AMSandwichMaker = None
        self.AMGrill = None
        self.AMHelper = None
        self.AMServers = []
        self.PMSandwichMaker = None
        self.PMGrill = None
        self.PMHelper = None
        self.PMServers = []
        self.PMDinners = None
        self.BusyPersons = set()
        self.positions_not_filled = 0
        
    def set_position_manually(self, person):
        self.BusyPersons.add(person)
        return person
        
    def set_position(self, position_list):
        position_list = copy(position_list)
        for person in self.BusyPersons:
            if person in position_list:
                position_list.remove(person)
        try:
            chosen = choice(position_list)
            self.BusyPersons.add(chosen)
            return chosen
        except(IndexError):
            self.positions_not_filled += 1
            return EMPTY 
            
    def GenerateAndSetServers(self, AMTotal, PMTotal):
        AMTotal = AMTotal - len(self.AMServers) # subtract servers set manually.
        PMTotal = PMTotal - len(self.PMServers)
        for server in range(AMTotal):
            self.AMServers.append(self.set_position(AMServers))
        for server in range(PMTotal):
            self.PMServers.append(self.set_position(PMServers))
    
    def GenerateAndSetKitchen(self):
        """This really sucks and there's probably a better way"""
        if self.AMSandwichMaker == None:
            self.AMSandwichMaker = self.set_position(SandwichMakers)
        if self.PMSandwichMaker == None:
            self.PMSandwichMaker = self.set_position(SandwichMakers)
        if self.AMGrill == None:
            self.AMGrill = self.set_position(Grillers)
        if self.PMGrill == None:
            self.PMGrill = self.set_position(Grillers)
        if self.AMHelper == None:
            self.AMHelper = self.set_position(Helpers)
        if self.PMHelper == None:
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
            day.AMSandwichMaker = day.set_position_manually(Lisa)
            day.AMGrill = day.set_position_manually(Tim)
            day.AMHelper = day.set_position(Helpers)
            day.GenerateAndSetServers(AMTotal=2, PMTotal=0)
        if day == Wednesday:
            day.AMSandwichMaker = day.set_position_manually(Lisa)
            day.AMGrill = day.set_position_manually(Tim)
            day.AMServers.append(day.set_position_manually(Sherie))
            day.GenerateAndSetKitchen()
            day.GenerateAndSetServers(AMTotal=2, PMTotal=2)
        if day == Thursday:
            day.AMSandwichMaker = day.set_position_manually(Lisa)
            day.AMGrill = day.set_position_manually(Tim)
            day.GenerateAndSetKitchen()
            day.GenerateAndSetServers(AMTotal=2, PMTotal=2)
        if day == Friday:
            day.AMSandwichMaker = day.set_position_manually(Lisa)
            day.AMGrill = day.set_position_manually(Tim)
            day.AMServers.append(day.set_position_manually(Sherie))
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


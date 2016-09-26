import random

class Day():
    
    def __init__(self, Name):
        self.Name = Name
        self.AMSandwichMaker = ''
        self.AMGrill = ''
        self.AMHelper = ''
        self.AMServers = []
        self.PMSandwichMaker = ''
        self.PMGrill = ''
        self.PMHelper = ''
        self.PMServers = []
        self.PMDinners = ''
        self.trainees = []
        
    def GenerateAndSetServers(self, ServerList, Total):
        servers = random.sample(ServerList, Total)
        self.AMServers = servers[0:max(2, int((Total/2)))]
        self.PMServers = servers[int(Total/2):Total]
        
    def GenerateAndSetKitchen(self, SandwichMakerList, GrillerList, HelperList, DinnerList):
        # Set SandwichMaker
        self.PMSandwichMaker = random.choice(SandwichMakerList)
        
        # Set Griller
        if self.PMSandwichMaker in GrillerList:
            GrillerList.remove(self.PMSandwichMaker)            
        self.PMGrill = random.choice(GrillerList)
        
        #Set Helpers
        for person in [self.PMSandwichMaker, self.PMGrill]:
            if person in HelperList:
                HelperList.remove(person)
        self.AMHelper, self.PMHelper = random.sample(HelperList, 2)
        
        #Set Dinners
        for person in [self.PMSandwichMaker, self.PMGrill, self.AMHelper, self.PMHelper]:
            if person in DinnerList:
                DinnerList.remove(person)
        if DinnerList == []:
            self.PMDinners = EMPTY
        else:
            self.PMDinners = random.choice(DinnerList)
   

class Person():

    def __init__(self, Name):
        self.Name = Name
        self.CanDoSandwiches = None
        self.CanDoGrill = None
        self.CanDoHelper = None
        self.CanServe = None
        self.CanDoDinners = None
        
def PrintoutTest():
    for day in Week:
        try:
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
        except(AttributeError):
            print('A position was not succesfully filled')
        
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

# Leaving only People whose schedules are flexible.
# Consider dividing into PM and AM Servers / Grillers.
People = [Tammy, Lisa, Sherie, Tim, Peggy, Katie, Alex,
          Jamie, Rhiannon, Kara, Nathan, Johnny, Joe, Sara]
SandwichMakers = [Katie, Rhiannon, Joe]
Grillers = [Katie, Alex, Rhiannon, Nathan, Johnny, Joe]
Helpers = [Katie, Alex, Rhiannon, Kara, Nathan, Johnny, Joe]
Servers = [Tammy, Sherie, Peggy, Jamie, Rhiannon, Kara, Nathan, Sara]
Dinners = [Alex, Rhiannon, Kara, Nathan, Johnny, Joe, Katie]

for sandwichMaker in SandwichMakers:
    sandwichMaker.CanDoSandwiches = True
for griller in Grillers:
    griller.CanDoGrill = True
for helper in Helpers:
    helper.CanDoHelper = True
for server in Servers:
    server.CanServe = True
for dinner in Dinners:
    dinner.CanDoDinner = True
    
# Standard Schedule Setup. Being verbose with repetition rather than efficient.
for day in Week:
    if day in [Monday, Tuesday]
        day.AMSandwichMaker = Lisa
        day.AMGrill = Tim
        day.AMHelper = random.choice(Helpers)
        day.GenerateAndSetServers(Servers, 2)
    if day in [Wednesday, Thursday]:
        day.AMSandwichMaker = Lisa
        day.AMGrill = Tim
        day.GenerateAndSetKitchen(SandwichMakers, Grillers, Helpers, Dinners)
        day.GenerateAndSetServers(Servers, 4)
    if day == Friday:
        day.AMSandwichMaker = Lisa
        day.AMGrill = Tim
        day.GenerateAndSetKitchen(SandwichMakers, Grillers, Helpers, Dinners)
        day.GenerateAndSetServers(Servers, 6)
    if day == Saturday:
        day.AMSandwichMaker, day.PMSandwichMaker = random.sample(SandwichMakers, 2)
        AvailableGrillers = Grillers
        for SandwichMaker in [day.AMSandwichMaker, day.PMSandwichMaker]:
            if SandwichMaker in AvailableGrillers:
                AvailableGrillers.remove(SandwichMaker)
        day.AMGrill, day.PMGrill = random.sample(AvailableGrillers, 2) 
        AvailableHelpers = Helpers
        for person in [day.AMSandwichMaker, day.PMSandwichMaker, day.AMGrill, day.PMGrill]:
            if person in AvailableHelpers:
                AvailableHelpers.remove(person)
        day.AMHelper, day.PMHelper = random.sample(AvailableHelpers, 2)
        day.GenerateAndSetServers(Servers, 4)

PrintoutTest()
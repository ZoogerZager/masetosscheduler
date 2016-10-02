from copy import copy
from random import choice


class Day:
    def __init__(self, name):
        self.name = name
        self.AMSandwichMaker = None
        self.AMGrill = None
        self.AMHelper = None
        self.AMServers = []
        self.PMSandwichMaker = None
        self.PMGrill = None
        self.PMHelper = None
        self.PMServers = []
        self.PMDinners = None
		self.AMBusyPersons = set()
        self.PMBusyPersons = set()
        self.empty_positions = 0

	def build_availability(self, person_list):
		for person in person_list:
			if person.not_available['AM'] == self.name or person.not_available['AM'] == 'All':
				self.AMBusyPersons.add(person)
			if person.not_available['PM'] == self.name or person.not_available['PM'] == 'All':
				self.PMBusyPersons.add(person)
				
    def not_available(self, person):
        assert isinstance(person, Person), "%r is not a Person Object" % person
        self.BusyPersons.add(person)

    def set_position_manually(self, person):
        assert isinstance(person, Person), "%r is not a Person Object" % person
        self.BusyPersons.add(person)
        return person

    def get_free_employees(self, position_list):
        position_list = copy(position_list)
        for person in self.BusyPersons:
            if person in position_list:
                position_list.remove(person)
        return position_list

    def set_position(self, position_list):
        try:
            chosen = choice(self.get_free_employees(position_list))
            self.BusyPersons.add(chosen)
            return chosen
        except IndexError:
            self.empty_positions += 1
            return EMPTY

    def set_servers(self, am_total, pm_total):
        am_total -= len(self.AMServers)  # subtract servers set manually.
        pm_total -= len(self.PMServers)
        for server in range(am_total):
            self.AMServers.append(self.set_position(AMServers))
        for server in range(pm_total):
            self.PMServers.append(self.set_position(PMServers))

    def set_kitchen(self):
        if self.AMSandwichMaker is None:
            self.AMSandwichMaker = self.set_position(AMSandwichMakers)
        if self.PMSandwichMaker is None:
            self.PMSandwichMaker = self.set_position(PMSandwichMakers)
        if self.AMGrill is None:
            self.AMGrill = self.set_position(AMGrillers)
        if self.PMGrill is None:
            self.PMGrill = self.set_position(PMGrillers)
        if self.AMHelper is None:
            self.AMHelper = self.set_position(AMHelpers)
        if self.PMHelper is None:
            self.PMHelper = self.set_position(PMHelpers)


class Person:
    def __init__(self, name, positions, not_available):
        assert isinstance(positions, list), "%r is not a list" % positions
        assert isinstance(availability, dict), "%r is not a dict" % availability
        self.name = name
        self.positions = positions
        self.not_available = not_available

def set_schedule(week_list):
    total_empty_positions = 0
    for day in week_list:
        if day.name in ['Monday', 'Tuesday']:
            day.AMSandwichMaker = day.set_position_manually(Lisa)
            day.AMGrill = day.set_position_manually(Tim)
            day.AMHelper = day.set_position(AMHelpers)
            day.set_servers(am_total=2, pm_total=0)
        if day.name is 'Wednesday':
            day.AMSandwichMaker = day.set_position_manually(Lisa)
            day.AMGrill = day.set_position_manually(Tim)
            day.AMServers.append(day.set_position_manually(Sherie))
            day.set_kitchen()
            day.set_servers(am_total=2, pm_total=2)
        if day.name is 'Thursday':
            day.AMSandwichMaker = day.set_position_manually(Lisa)
            day.AMGrill = day.set_position_manually(Tim)
            day.set_kitchen()
            day.set_servers(am_total=2, pm_total=2)
        if day.name is 'Friday':
            day.AMSandwichMaker = day.set_position_manually(Lisa)
            day.AMGrill = day.set_position_manually(Tim)
            day.AMServers.append(day.set_position_manually(Sherie))
            day.set_kitchen()
            day.set_servers(am_total=3, pm_total=3)
            day.PMDinners = day.set_position(Dinners)
        if day.name is 'Saturday':
            day.set_kitchen()
            day.set_servers(am_total=2, pm_total=2)
        total_empty_positions += day.empty_positions
    if total_empty_positions == 0:  # Succesful
        return True
    if total_empty_positions > 0:  # Unsuccesful
        return False


def printout_test(week_list):
    for day in week_list:
        print('--', day.name, ' Staff --')
        print('AMSandwichMaker: ', day.AMSandwichMaker.name)
        print('AMGrill: ', day.AMGrill.name)
        print('AMHelper: ', day.AMHelper.name)
        for server in day.AMServers:
            print('AMServer: ', server.name)
        if day.name in ['Wednesday', 'Thursday', 'Friday', 'Saturday']:
            print('PMSandwichMaker: ', day.PMSandwichMaker.name)
            print('PMGrill: ', day.PMGrill.name)
            print('PMHelper: ', day.PMHelper.name)
            try:
                print('PMDinners: ', day.PMDinners.name)
            except AttributeError:
                pass
            for server in day.PMServers:
                print('PMServer: ', server.name)
        print('Empty Positions: ', day.empty_positions)
        print('\n')


def initialize_week():
    Monday = Day('Monday')
    Tuesday = Day('Tuesday')
    Wednesday = Day('Wednesday')
    Thursday = Day('Thursday')
    Friday = Day('Friday')
    Saturday = Day('Saturday')
    Week = [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday]
    return Week

Tammy = Person('Tammy', ['Server'], {'PM': 'All'})
Lisa = Person('Lisa', ['SandwichMaker'], {'AM': 'Saturday', 'PM': 'All'})
Sherie = Person('Sherie', ['Server'], {'PM': 'All'})
Tim = Person('Tim', ['Griller'], {'AM': 'Saturday','PM': 'All'})
Peggy = Person('Peggy', ['Server'], ['PM': 'All'])
Katie = Person('Katie', ['SandwichMaker', 'Griller', 'Helper', 'Dinners'],
                        {})
Alex = Person('Alex', ['Griller', 'Helper', 'Dinners'], {})
Jamie = Person('Jamie', ['Server'], {})
Rhiannon = Person('Rhiannon', ['SandwichMaker', 'Griller', 'Helper', 'Server',
                               'Dinners'], {})
Kara = Person('Kara', ['Helper', 'Server', 'Dinners'], {})
Nathan = Person('Nathan', ['Griller', 'Helper', 'Server', 'Dinners'], {'AM': 'All'})
Johnny = Person('Johnny', ['Griller', 'Helper'], {'AM': 'All'})
Joe = Person('Joe', ['SandwichMaker', 'Griller', 'Helper', 'Dinners'],
                    {})
Sara = Person('Sara', ['Server'], {})
EMPTY = Person('-EMPTY-', [], {})

People = [Tammy, Lisa, Sherie, Tim, Peggy, Katie, Alex, Jamie, Rhiannon, Kara,
          Nathan, Johnny, Joe, Sara]

#TODO This all needs reworked for the new not_available attribute
AMSandwichMakers = [p for p in People if 'SandwichMaker' in p.positions and 'AM' in p.availability]
PMSandwichMakers = [p for p in People if 'SandwichMaker' in p.positions and 'PM' in p.availability]
AMGrillers = [p for p in People if 'Griller' in p.positions and 'AM' in p.availability]
PMGrillers = [p for p in People if 'Griller' in p.positions and 'PM' in p.availability]
AMHelpers = [p for p in People if 'Helper' in p.positions and 'AM' in p.availability]
PMHelpers = [p for p in People if 'Helper' in p.positions and 'PM' in p.availability]
AMServers = [p for p in People if 'Server' in p.positions and 'AM' in p.availability]
PMServers = [p for p in People if 'Server' in p.positions and 'PM' in p.availability]
Dinners = [p for p in People if 'Dinners' in p.positions]


week = initialize_week()
schedule_completed = set_schedule(week)
while not schedule_completed:
    week = initialize_week()
    schedule_completed = set_schedule(week)
printout_test(week)

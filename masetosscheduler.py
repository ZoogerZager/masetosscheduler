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
            if person.not_available['AM'] == self.name:
                self.AMBusyPersons.add(person)
            if person.not_available['AM'] == 'All':
                self.AMBusyPersons.add(person)
            if person.not_available['PM'] == self.name:
                self.PMBusyPersons.add(person)
            if person.not_available['PM'] == 'All':
                self.PMBusyPersons.add(person)

    def not_available(self, person):
        assert isinstance(person, Person), "%r is not a Person Object" % person
        self.AMBusyPersons.add(person)
        self.PMBusyPersons.add(person)

    def set_position_manually(self, person):
        assert isinstance(person, Person), "%r is not a Person Object" % person
        self.AMBusyPersons.add(person)
        self.PMBusyPersons.add(person)
        return person

    def get_free_am_employees(self, position_list):    # Hackish
        position_list = copy(position_list)
        for person in self.AMBusyPersons:
            if person in position_list:
                position_list.remove(person)
        return position_list

    def get_free_pm_employees(self, position_list):
        position_list = copy(position_list)
        for person in self.PMBusyPersons:
            if person in position_list:
                position_list.remove(person)
        return position_list

    def set_position(self, position_list, shift):
        assert shift in ['AM', 'PM'], '%r shift should be "AM" or "PM"' % shift
        if shift is 'AM':
            try:
                chosen = choice(self.get_free_am_employees(position_list))
                self.AMBusyPersons.add(chosen)
                self.PMBusyPersons.add(chosen)
                return chosen
            except IndexError:
                self.empty_positions += 1
                return EMPTY
        if shift is 'PM':
            try:
                chosen = choice(self.get_free_pm_employees(position_list))
                self.AMBusyPersons.add(chosen)
                self.PMBusyPersons.add(chosen)
                return chosen
            except IndexError:
                self.empty_positions += 1
                return EMPTY

    def set_servers(self, am_total, pm_total):
        am_total -= len(self.AMServers)  # subtract servers set manually.
        pm_total -= len(self.PMServers)
        for server in range(am_total):
            self.AMServers.append(self.set_position(Servers, 'AM'))
        for server in range(pm_total):
            self.PMServers.append(self.set_position(Servers, 'PM'))

    def set_kitchen(self):
        if self.AMSandwichMaker is None:
            self.AMSandwichMaker = self.set_position(SandwichMakers, 'AM')
        if self.PMSandwichMaker is None:
            self.PMSandwichMaker = self.set_position(SandwichMakers, 'PM')
        if self.AMGrill is None:
            self.AMGrill = self.set_position(Grillers, 'AM')
        if self.PMGrill is None:
            self.PMGrill = self.set_position(Grillers, 'PM')
        if self.AMHelper is None:
            self.AMHelper = self.set_position(Helpers, 'AM')
        if self.PMHelper is None:
            self.PMHelper = self.set_position(Helpers, 'PM')


class Person:
    def __init__(self, name, positions, not_available):
        assert isinstance(positions, list), "%r is not a list" % positions
        assert isinstance(not_available, dict), "%r is not a dict" % not_available
        self.name = name
        self.positions = positions
        self.not_available = not_available


def set_schedule(week_list):
    total_empty_positions = 0
    for day in week_list:
        day.build_availability(People)
        if day.name in ['Monday', 'Tuesday']:
            day.AMSandwichMaker = day.set_position_manually(Lisa)
            day.AMGrill = day.set_position_manually(Tim)
            day.AMHelper = day.set_position(Helpers, 'AM')
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
            day.PMDinners = day.set_position(Dinners, 'PM')
        if day.name is 'Saturday':
            day.set_kitchen()
            day.set_servers(am_total=2, pm_total=2)
        total_empty_positions += day.empty_positions
    if total_empty_positions == 0:  # Successful
        return True
    if total_empty_positions > 0:  # Unsuccessful
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
    week = []
    for day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']:
        current_day = Day(day)
        week.append(current_day)
    return week


def run_once_and_print():
    week = initialize_week()
    set_schedule(week)
    printout_test(week)


def run_till_completed():
    week = initialize_week()
    schedule_completed = set_schedule(week)
    while not schedule_completed:
        week = initialize_week()
        schedule_completed = set_schedule(week)
    printout_test(week)

#TODO The Availability Dicts should have lists as values
Tammy = Person('Tammy', ['Server'], dict(AM=None, PM='All'))
Lisa = Person('Lisa', ['SandwichMaker'], dict(AM='Saturday', PM='All'))
Sherie = Person('Sherie', ['Server'], dict(AM=None, PM='All'))
Tim = Person('Tim', ['Griller'], dict(AM='Saturday', PM='All'))
Peggy = Person('Peggy', ['Server'], {'AM': None, 'PM': 'All'})
Katie = Person('Katie', ['SandwichMaker', 'Griller', 'Helper', 'Dinners'], dict(AM=None, PM=None))
Alex = Person('Alex', ['Griller', 'Helper', 'Dinners'], dict(AM=None, PM=None))
Jamie = Person('Jamie', ['Server'], dict(AM=None, PM=None))
Rhiannon = Person('Rhiannon', ['SandwichMaker', 'Griller', 'Helper', 'Server', 'Dinners'], dict(AM=None, PM=None))
Kara = Person('Kara', ['Helper', 'Server', 'Dinners'], dict(AM=None, PM=None))
Nathan = Person('Nathan', ['Griller', 'Helper', 'Server', 'Dinners'], dict(AM='All', PM=None))
Johnny = Person('Johnny', ['Griller', 'Helper'], dict(AM='All', PM=None))
Joe = Person('Joe', ['SandwichMaker', 'Griller', 'Helper', 'Dinners'], dict(AM=None, PM=None))
Sara = Person('Sara', ['Server'], dict(AM=None, PM=None))
EMPTY = Person('-EMPTY-', [], dict(AM='All', PM='All'))

People = [Tammy, Lisa, Sherie, Tim, Peggy, Katie, Alex, Jamie, Rhiannon, Kara,
          Nathan, Johnny, Joe, Sara]

SandwichMakers = [p for p in People if 'SandwichMaker' in p.positions]
Grillers = [p for p in People if 'Griller' in p.positions]
Helpers = [p for p in People if 'Helper' in p.positions]
Servers = [p for p in People if 'Server' in p.positions]
Dinners = [p for p in People if 'Dinners' in p.positions]

# run_once_and_print()
run_till_completed()

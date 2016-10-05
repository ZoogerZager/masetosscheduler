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

    def set_availability(self, person_list):
        for person in person_list:
            if self.name in person.not_available['AM']:
                self.AMBusyPersons.add(person)
            if 'All' in person.not_available['AM']:
                self.AMBusyPersons.add(person)
            if self.name in person.not_available['PM']:
                self.PMBusyPersons.add(person)
            if 'All' in person.not_available['PM']:
                self.PMBusyPersons.add(person)

    def set_busy(self, person):
        assert isinstance(person, Person), "%r is not a Person Object" % person
        self.AMBusyPersons.add(person)
        self.PMBusyPersons.add(person)

    def set_position_manually(self, person):
        assert isinstance(person, Person), "%r is not a Person Object" % person
        self.set_busy(person)
        return person

    def get_free_am_employees(self, position_list):
        return list(position_list - self.AMBusyPersons)

    def get_free_pm_employees(self, position_list):
        return list(position_list - self.PMBusyPersons)

    def set_position(self, position_list, shift):
        assert shift in ['AM', 'PM'], '%r shift should be "AM" or "PM"' % shift
        try:
            if shift is 'AM':
                chosen = choice(self.get_free_am_employees(position_list))
                self.set_busy(chosen)
                return chosen
            if shift is 'PM':
                chosen = choice(self.get_free_pm_employees(position_list))
                self.set_busy(chosen)
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

    def print(self):
        print('--', self.name, ' Staff --')
        print('AMSandwichMaker: ', self.AMSandwichMaker.name)
        print('AMGrill: ', self.AMGrill.name)
        print('AMHelper: ', self.AMHelper.name)
        for server in self.AMServers:
            print('AMServer: ', server.name)
        if self.name in ['Wednesday', 'Thursday', 'Friday', 'Saturday']:
            print('PMSandwichMaker: ', self.PMSandwichMaker.name)
            print('PMGrill: ', self.PMGrill.name)
            print('PMHelper: ', self.PMHelper.name)
            try:
                print('PMDinners: ', self.PMDinners.name)
            except AttributeError:
                pass
            for server in self.PMServers:
                print('PMServer: ', server.name)
        print('Empty Positions: ', self.empty_positions)
        print('\n')



class Monday(Day):
    def setup(self):
        self.set_availability(People)
        self.AMSandwichMaker = self.set_position_manually(Lisa)
        self.AMGrill = self.set_position_manually(Tim)
        self.AMHelper = self.set_position(Helpers, 'AM')
        self.set_servers(am_total=2, pm_total=0)


class Tuesday(Day):
    def setup(self):
        self.set_availability(People)
        self.AMSandwichMaker = self.set_position_manually(Lisa)
        self.AMGrill = self.set_position_manually(Tim)
        self.AMHelper = self.set_position(Helpers, 'AM')
        self.set_servers(am_total=2, pm_total=0)


class Wednesday(Day):
    def setup(self):
        self.set_availability(People)
        self.AMSandwichMaker = self.set_position_manually(Lisa)
        self.AMGrill = self.set_position_manually(Tim)
        self.AMServers.append(self.set_position_manually(Sherie))
        self.set_kitchen()
        self.set_servers(am_total=2, pm_total=2)


class Thursday(Day):
    def setup(self):
        self.set_availability(People)
        self.AMSandwichMaker = self.set_position_manually(Lisa)
        self.AMGrill = self.set_position_manually(Tim)
        self.AMServers.append(self.set_position_manually(Sherie))
        self.set_kitchen()
        self.set_servers(am_total=2, pm_total=2)


class Friday(Day):
    def setup(self):
        self.set_availability(People)
        self.AMSandwichMaker = self.set_position_manually(Lisa)
        self.AMGrill = self.set_position_manually(Tim)
        self.AMServers.append(self.set_position_manually(Sherie))
        self.set_kitchen()
        self.set_servers(am_total=3, pm_total=3)
        self.PMDinners = self.set_position(Dinners, 'PM')
        return self.empty_positions


class Saturday(Day):
    def setup(self):
        self.set_availability(People)
        self.set_kitchen()
        self.set_servers(am_total=2, pm_total=2)


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
        day.set_availability(People)
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
    if total_empty_positions > 0:   # Unsuccessful
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


Tammy = Person('Tammy', ['Server'], dict(AM=[], PM=['All']))
Lisa = Person('Lisa', ['SandwichMaker'], dict(AM=['Saturday'], PM=['All']))
Sherie = Person('Sherie', ['Server'], dict(AM=[], PM=['All']))
Tim = Person('Tim', ['Griller'], dict(AM=['Saturday'], PM=['All']))
Peggy = Person('Peggy', ['Server'], {'AM': [], 'PM': ['All']})
Katie = Person('Katie', ['SandwichMaker', 'Griller', 'Helper', 'Dinners'], dict(AM=[], PM=[]))
Alex = Person('Alex', ['Griller', 'Helper', 'Dinners'], dict(AM=[], PM=[]))
Jamie = Person('Jamie', ['Server'], dict(AM=[], PM=[]))
Rhiannon = Person('Rhiannon', ['SandwichMaker', 'Griller', 'Helper', 'Server', 'Dinners'], dict(AM=[], PM=[]))
Kara = Person('Kara', ['Helper', 'Server', 'Dinners'], dict(AM=[], PM=[]))
Nathan = Person('Nathan', ['Griller', 'Helper', 'Server', 'Dinners'], dict(AM=['All'], PM=[]))
Johnny = Person('Johnny', ['Griller', 'Helper'], dict(AM=['All'], PM=[]))
Joe = Person('Joe', ['SandwichMaker', 'Griller', 'Helper', 'Dinners'], dict(AM=[], PM=[]))
Sara = Person('Sara', ['Server'], dict(AM=[], PM=[]))
EMPTY = Person('-EMPTY-', [], dict(AM=['All'], PM=['All']))

People = {Tammy, Lisa, Sherie, Tim, Peggy, Katie, Alex, Jamie, Rhiannon, Kara,
              Nathan, Johnny, Joe, Sara}

SandwichMakers = set([p for p in People if 'SandwichMaker' in p.positions])
Grillers = set([p for p in People if 'Griller' in p.positions])
Helpers = set([p for p in People if 'Helper' in p.positions])
Servers = set([p for p in People if 'Server' in p.positions])
Dinners = set([p for p in People if 'Dinners' in p.positions])

# run_once_and_print()
# run_till_completed()

Monday = Monday('Monday')
Monday.setup()
Monday.print()

Friday = Friday('Friday')
Friday.setup()
Friday.print()

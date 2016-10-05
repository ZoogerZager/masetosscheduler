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

    def set_am_position(self, position_list):
        try:
            chosen = choice(self.get_free_am_employees(position_list))
            self.set_busy(chosen)
            return chosen
        except IndexError:
            self.empty_positions += 1
            return EMPTY

    def set_pm_position(self, position_list):
        try:
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
            self.AMServers.append(self.set_am_position(Servers))
        for server in range(pm_total):
            self.PMServers.append(self.set_pm_position(Servers))

    def set_kitchen(self):
        if self.AMSandwichMaker is None:
            self.AMSandwichMaker = self.set_am_position(SandwichMakers)
        if self.PMSandwichMaker is None:
            self.PMSandwichMaker = self.set_pm_position(SandwichMakers
        if self.AMGrill is None:
            self.AMGrill = self.set_am_position(Grillers)
        if self.PMGrill is None:
            self.PMGrill = self.set_pm_position(Grillers)
        if self.AMHelper is None:
            self.AMHelper = self.set_am_position(Helpers)
        if self.PMHelper is None:
            self.PMHelper = self.set_pm_position(Helpers)

    def print_day_schedule(self):
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
        self.AMHelper = self.set_am_position(Helpers)
        self.set_servers(am_total=2, pm_total=0)


class Tuesday(Day):
    def setup(self):
        self.set_availability(People)
        self.AMSandwichMaker = self.set_position_manually(Lisa)
        self.AMGrill = self.set_position_manually(Tim)
        self.AMHelper = self.set_am_position(Helpers)
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
        self.PMDinners = self.set_pm_position(Dinners)


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
    for day in week_list:
        day.setup()
        if day.empty_positions > 0:  # Unsuccessful
            return False
    return True  # Successful


def print_schedule(week_list):
    for day in week_list:
        day.print_day_schedule()


def initialize_week():
    week = [Monday('Monday'), Tuesday('Tuesday'), Wednesday('Wednesday'), Thursday('Thursday'), Friday('Friday'),
            Saturday('Saturday')]
    return week


def run_once_and_print():
    week = initialize_week()
    set_schedule(week)
    print_schedule(week)


def run_until_completed_and_print():
    week = initialize_week()
    schedule_completed = set_schedule(week)
    while not schedule_completed:
        week = initialize_week()
        schedule_completed = set_schedule(week)
    print_schedule(week)


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

#  run_once_and_print()
run_until_completed_and_print()

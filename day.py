from random import choice
from employees import Person, Employees


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
            return Employees.EMPTY

    def set_pm_position(self, position_list):
        try:
            chosen = choice(self.get_free_pm_employees(position_list))
            self.set_busy(chosen)
            return chosen
        except IndexError:
            self.empty_positions += 1
            return Employees.EMPTY

    def set_servers(self, am_total, pm_total):
        Servers = Employees.get_servers()
        am_total -= len(self.AMServers)  # subtract servers set manually.
        pm_total -= len(self.PMServers)
        for server in range(am_total):
            self.AMServers.append(self.set_am_position(Servers))
        for server in range(pm_total):
            self.PMServers.append(self.set_pm_position(Servers))

    def set_kitchen(self):
        SandwichMakers = Employees.get_sandwichmakers()
        Grillers = Employees.get_grillers()
        Helpers = Employees.get_helpers()
        if self.AMSandwichMaker is None:
            self.AMSandwichMaker = self.set_am_position(SandwichMakers)
        if self.PMSandwichMaker is None:
            self.PMSandwichMaker = self.set_pm_position(SandwichMakers)
        if self.AMGrill is None:
            self.AMGrill = self.set_am_position(Grillers)
        if self.PMGrill is None:
            self.PMGrill = self.set_pm_position(Grillers)
        if self.AMHelper is None:
            self.AMHelper = self.set_am_position(Helpers)
        if self.PMHelper is None:
            self.PMHelper = self.set_pm_position(Helpers)

    def write_out(self):
        lines =[]
        lines.append('-- ' + self.name + ' Staff --')
        lines.append('AMSandwichMaker: ' + self.AMSandwichMaker.name)
        lines.append('AMGrill: ' + self.AMGrill.name)
        lines.append('AMHelper: ' + self.AMHelper.name)
        for server in self.AMServers:
            lines.append(('AMServer: ' + server.name))
        if self.name in ['Wednesday', 'Thursday', 'Friday', 'Saturday']:
            lines.append('PMSandwichMaker: ' + self.PMSandwichMaker.name)
            lines.append('PMGrill: ' + self.PMGrill.name)
            lines.append('PMHelper: ' + self.PMHelper.name)
            try:
                lines.append('PMDinners: ' + self.PMDinners.name)
            except AttributeError:
                pass
            for server in self.PMServers:
                lines.append('PMServer: ' + server.name)
        lines.append('Empty Positions: ' + str(self.empty_positions))
        lines.append('\n')
        return lines

class Monday(Day):
    def setup(self):
        self.set_availability(Employees.people)
        self.AMSandwichMaker = self.set_position_manually(Employees.Lisa)
        self.AMGrill = self.set_position_manually(Employees.Tim)
        self.AMHelper = self.set_am_position(Employees.get_helpers())
        self.set_servers(am_total=2, pm_total=0)


class Tuesday(Day):
    def setup(self):
        self.set_availability(Employees.people)
        self.AMSandwichMaker = self.set_position_manually(Employees.Lisa)
        self.AMGrill = self.set_position_manually(Employees.Tim)
        self.AMHelper = self.set_am_position(Employees.get_helpers())
        self.set_servers(am_total=2, pm_total=0)


class Wednesday(Day):
    def setup(self):
        self.set_availability(Employees.people)
        self.AMSandwichMaker = self.set_position_manually(Employees.Lisa)
        self.AMGrill = self.set_position_manually(Employees.Tim)
        self.AMServers.append(self.set_position_manually(Employees.Sherie))
        self.set_kitchen()
        self.set_servers(am_total=2, pm_total=2)


class Thursday(Day):
    def setup(self):
        self.set_availability(Employees.people)
        self.AMSandwichMaker = self.set_position_manually(Employees.Lisa)
        self.AMGrill = self.set_position_manually(Employees.Tim)
        self.AMServers.append(self.set_position_manually(Employees.Sherie))
        self.set_kitchen()
        self.set_servers(am_total=2, pm_total=2)


class Friday(Day):
    def setup(self):
        self.set_availability(Employees.people)
        self.AMSandwichMaker = self.set_position_manually(Employees.Lisa)
        self.AMGrill = self.set_position_manually(Employees.Tim)
        self.AMServers.append(self.set_position_manually(Employees.Sherie))
        self.set_kitchen()
        self.set_servers(am_total=3, pm_total=3)
        self.PMDinners = self.set_pm_position(Employees.get_dinners())


class Saturday(Day):
    def setup(self):
        self.set_availability(Employees.people)
        self.set_kitchen()
        self.set_servers(am_total=2, pm_total=2)

Employees = Employees()  # Not sure if this is good practice.

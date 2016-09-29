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
        self.BusyPersons = set()
        self.positions_not_filled = 0

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
            self.positions_not_filled += 1
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
            self.AMSandwichMaker = self.set_position(SandwichMakers)
        if self.PMSandwichMaker is None:
            self.PMSandwichMaker = self.set_position(SandwichMakers)
        if self.AMGrill is None:
            self.AMGrill = self.set_position(Grillers)
        if self.PMGrill is None:
            self.PMGrill = self.set_position(Grillers)
        if self.AMHelper is None:
            self.AMHelper = self.set_position(Helpers)
        if self.PMHelper is None:
            self.PMHelper = self.set_position(Helpers)


class Person:
    def __init__(self, name, positions):
        self.name = name
        assert isinstance(positions, list), "%r is not a list" % positions
        self.positions = positions


def set_schedule(week_list):
    for day in week_list:
        if day in [Monday, Tuesday]:
            day.not_available(Joe)
            day.AMSandwichMaker = day.set_position_manually(Lisa)
            day.AMGrill = day.set_position_manually(Tim)
            day.AMHelper = day.set_position(Helpers)
            day.set_servers(am_total=2, pm_total=0)
        if day is Wednesday:
            day.AMSandwichMaker = day.set_position_manually(Lisa)
            day.AMGrill = day.set_position_manually(Tim)
            day.AMServers.append(day.set_position_manually(Sherie))
            day.set_kitchen()
            day.set_servers(am_total=2, pm_total=2)
        if day is Thursday:
            day.AMSandwichMaker = day.set_position_manually(Lisa)
            day.AMGrill = day.set_position_manually(Tim)
            day.set_kitchen()
            day.set_servers(am_total=2, pm_total=2)
        if day is Friday:
            day.AMSandwichMaker = day.set_position_manually(Lisa)
            day.AMGrill = day.set_position_manually(Tim)
            day.AMServers.append(day.set_position_manually(Sherie))
            day.set_kitchen()
            day.set_servers(am_total=3, pm_total=3)
            day.PMDinners = day.set_position(Dinners)
        if day is Saturday:
            day.set_kitchen()
            day.set_servers(am_total=2, pm_total=2)


def printout_test():
    for day in Week:
        print('--', day.name, ' Staff --')
        print('AMSandwichMaker: ', day.AMSandwichMaker.name)
        print('AMGrill: ', day.AMGrill.name)
        print('AMHelper: ', day.AMHelper.name)
        for server in day.AMServers:
            print('AMServer: ', server.name)
        if day in [Wednesday, Thursday, Friday, Saturday]:
            print('PMSandwichMaker: ', day.PMSandwichMaker.name)
            print('PMGrill: ', day.PMGrill.name)
            print('PMHelper: ', day.PMHelper.name)
            try:
                print('PMDinners: ', day.PMDinners.name)
            except AttributeError:
                pass
            for server in day.PMServers:
                print('PMServer: ', server.name)
        print('Positions not filled: ', day.positions_not_filled)
        print('\n')


Monday = Day('Monday')
Tuesday = Day('Tuesday')
Wednesday = Day('Wednesday')
Thursday = Day('Thursday')
Friday = Day('Friday')
Saturday = Day('Saturday')
Week = [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday]

Tammy = Person('Tammy', ['AMServer'])
Lisa = Person('Lisa', ['SandwichMaker'] )
Sherie = Person('Sherie', ['AMServer'])
Tim = Person('Tim', ['Griller'])
Peggy = Person('Peggy', ['AMServer'])
Katie = Person('Katie', ['SandwichMaker', 'Griller', 'Helper', 'Dinners'])
Alex = Person('Alex', ['Grill', 'Helper', 'Dinners'])
Jamie = Person('Jamie', ['AMServer', 'PMServer'])
Rhiannon = Person('Rhiannon', ['SandwichMaker', 'Grill', 'Helper', 'PMServer', 'Dinners'])
Kara = Person('Kara', ['Helper', 'PMServer', 'Dinners'])
Nathan = Person('Nathan', ['Griller', 'Helper', 'PMServer', 'Dinners'])
Johnny = Person('Johnny', ['Griller', 'Helper'])
Joe = Person('Joe', ['SandwichMaker', 'Griller', 'Helper', 'Dinners'])
Sara = Person('Sara', ['AMServer', 'PMServer'])
EMPTY = Person('-EMPTY-', [])

People = [Tammy, Lisa, Sherie, Tim, Peggy, Katie, Alex, Jamie, Rhiannon, Kara,
          Nathan, Johnny, Joe, Sara]
SandwichMakers = [person for person in People if 'SandwichMaker' in person.positions]
Grillers = [person for person in People if 'Griller' in person.positions]
Helpers = [person for person in People if 'Helper' in person.positions]
AMServers = [person for person in People if 'AMServer' in person.positions]
PMServers = [person for person in People if 'PMServer' in person.positions]
Dinners = [person for person in People if 'Dinners' in person.positions]

set_schedule(Week)
printout_test()
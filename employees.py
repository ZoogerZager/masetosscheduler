class Person:
    def __init__(self, name, positions, not_available):
        assert isinstance(positions, list), "%r is not a list" % positions
        assert isinstance(not_available, dict), "%r is not a dict" % not_available
        self.name = name
        self.positions = positions
        self.not_available = not_available


class Employees:
    def __init__(self):
        self.Tammy = Person('Tammy', ['Server'], dict(AM=[], PM=['All']))
        self.Lisa = Person('Lisa', ['SandwichMaker'], dict(AM=['Saturday'], PM=['All']))
        self.Sherie = Person('Sherie', ['Server'], dict(AM=[], PM=['All']))
        self.Tim = Person('Tim', ['Griller'], dict(AM=['Saturday'], PM=['All']))
        self.Peggy = Person('Peggy', ['Server'], {'AM': [], 'PM': ['All']})
        self.Katie = Person('Katie', ['SandwichMaker', 'Griller', 'Helper', 'Dinners'], dict(AM=[], PM=[]))
        self.Alex = Person('Alex', ['Griller', 'Helper', 'Dinners'], dict(AM=[], PM=[]))
        self.Jamie = Person('Jamie', ['Server'], dict(AM=[], PM=[]))
        self.Rhiannon = Person('Rhiannon', ['SandwichMaker', 'Griller', 'Helper', 'Server', 'Dinners'], dict(AM=[], PM=[]))
        self.Kara = Person('Kara', ['Helper', 'Server', 'Dinners'], dict(AM=[], PM=[]))
        self.Nathan = Person('Nathan', ['Griller', 'Helper', 'Server', 'Dinners'], dict(AM=['All'], PM=[]))
        self.Johnny = Person('Johnny', ['Griller', 'Helper'], dict(AM=['All'], PM=[]))
        self.Joe = Person('Joe', ['SandwichMaker', 'Griller', 'Helper', 'Dinners'], dict(AM=[], PM=[]))
        self.Sara = Person('Sara', ['Server'], dict(AM=[], PM=[]))
        self.EMPTY = Person('-EMPTY-', [], dict(AM=['All'], PM=['All']))
        self.people = {self.Tammy, self.Lisa, self.Sherie, self.Tim, self.Peggy,
                       self.Katie, self.Alex, self.Jamie, self.Rhiannon,
                       self.Kara, self.Nathan, self.Johnny, self.Joe, self.Sara}


    def get_sandwichmakers(self):
        return set([p for p in self.people if 'SandwichMaker' in p.positions])


    def get_grillers(self):
        return set([p for p in self.people if 'Griller' in p.positions])


    def get_helpers(self):
        return set([p for p in self.people if 'Helper' in p.positions])


    def get_servers(self):
        return set([p for p in self.people if 'Server' in p.positions])


    def get_dinners(self):
        return set([p for p in self.people if 'Dinners' in p.positions])

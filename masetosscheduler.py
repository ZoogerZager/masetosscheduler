from day import Monday, Tuesday, Wednesday, Thursday, Friday, Saturday


class Schedule:
    def __init__(self):
        self.week = self.initialize_week()


    def initialize_week(self):
        week = [Monday('Monday'), Tuesday('Tuesday'), Wednesday('Wednesday'),
                Thursday('Thursday'), Friday('Friday'), Saturday('Saturday')]
        return week


    def set_schedule(self):
        for day in self.week:
            day.setup()
            if day.empty_positions > 0:  # Unsuccessful
                return False
        return True  # Successful


    def generate_schedule(self):
        self.week = self.initialize_week()
        return self.set_schedule()


    def generate_filled_schedule(self):
        schedule_completed = self.generate_schedule()
        while not schedule_completed:
            schedule_completed = self.generate_schedule()


    def print_to_console(self):
        for day in self.week:
            for line in day.write_out():
                print(line)


    def save_to_txt(self):
        with open('schedule.txt', 'w') as f:
            for day in self.week:
                for line in day.write_out():
                    f.write(line)
                    f.write('\n')


schedule = Schedule()
schedule.generate_filled_schedule()
schedule.print_to_console()
schedule.save_to_txt()

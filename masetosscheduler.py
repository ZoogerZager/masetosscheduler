from day import Monday, Tuesday, Wednesday, Thursday, Friday, Saturday


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
    week = [Monday('Monday'), Tuesday('Tuesday'), Wednesday('Wednesday'),
            Thursday('Thursday'), Friday('Friday'), Saturday('Saturday')]
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


run_until_completed_and_print()

class Time:
    def __init__(self, hours = 0, minutes = 0, seconds = 0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

class TimeUtils:
    def __init__(self):
        pass

    def add_time(self, time1, time2):
        total_hours = time1.hours + time2.hours
        total_min = time1.minutes + time2.minutes
        total_s = time1.seconds + time2.seconds


        ##add seconds, if > 60, reset to 0, add 1 min
        if total_s > 60:
            total_s -= 60
            total_min += 1

        #add minutes, if > 60, reset to 0, add 1 hour
        if total_min >= 60:
            total_min -= 60
            total_hours += 1

        # Uncomment this line to work in AM - PM format
        # add the hours, if higher then 12, reset to 0
        # if total_hours > 12:
        #     total_hours -= 12

        new_time = Time(total_hours, total_min, total_s)
        return new_time.hours, new_time.minutes, new_time.seconds

    def time_to_seconds(self, to_seconds):
        hours_to_s = to_seconds.hours
        min_to_s = to_seconds.minutes

        total = (hours_to_s*60*60)+(min_to_s*60)+to_seconds.seconds
        return total





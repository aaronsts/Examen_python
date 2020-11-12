from Classes import Time, TimeUtils

time_management1 = Time(12,56,00)
time_management2 = Time(1,4,00)

time_management3 = TimeUtils()

time_management4 = Time(1,0,0)





print(time_management3.add_time(time_management1,time_management2))
print(TimeUtils.time_to_seconds(time_management4))
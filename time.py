import time

t = int(input("Enter the time in seconds: "))

while t >= 0:
    minutes, seconds = divmod(t, 60)
    time_left = '{:02d}:{:02d}'.format(minutes, seconds)
    print(time_left, end='\r')
    time.sleep(1)
    t -= 1

print("Time's up!")

import time


t = (input("Enter the number of seconds for the countdown: "))

if t.isdigit():
    t = int(t)
else:
    print("Please enter a valid number.")
    quit()

while t:
    minutes , second = divmod(t, 60)  # Get minutes and seconds
    timer = '{:02d}:{:02d}'.format(minutes, second)  # Format as MM:SS
    print (timer, end="\r")
    time.sleep(1)
    t = t - 1
print("Time's up!")

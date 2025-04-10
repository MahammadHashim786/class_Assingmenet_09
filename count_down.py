# Count Down

import time

print("wellcome to the countdown time!")
print("Enter the time in second, and I'II count down for you.\n")

try:
    total_time = int(input("Enter the count down timer in second. "))
except ValueError:
    print("Invalid input! please refer a valid number ")
    exit()

while total_time > 0:
    minutes, seconds = divmod(total_time, 60)
    timer = f"{minutes:02d} : {seconds:02d}"
    print(timer,end="\r")
    time.sleep(1)
    total_time -= 1

print("Time's Up")
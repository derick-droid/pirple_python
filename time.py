
"""
other imports such as time library
"""
import time
# checking the time to taken for an algorithm to execute
current_time = time.CLOCK_PROCESS_CPUTIME_ID
print("hello world")
print("joyce omondi")
final_time = time.CLOCK_PROCESS_CPUTIME_ID
print(final_time-current_time)
# sleep when we want our program to sleep for some second before executing the next
print("hello boy")
time.sleep(1)
print("the sleep mode is over")

# using for loop
for i in range(1,23):
    print(i)
    time.sleep(3)
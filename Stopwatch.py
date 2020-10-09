import time

start = input("Press enter to start the timer")
print("the timer has started")

begin = time.time()

endtimer = input("Press enter to stop the timer")

end = time.time()

elapsed = end - begin

elapsed = int(elapsed)

print("The time elapsed is", elapsed,)

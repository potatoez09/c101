import time

def count_timer(seconds):
    while seconds > 0:
        mins = int (seconds/60)
        secs = int (seconds%60)
        timer = f"{mins}:{secs}"
        print(timer)
        seconds -= 1
    print("time up!")    
seconds = input("enter the time in seconds :=> ")
count_timer(int(seconds))
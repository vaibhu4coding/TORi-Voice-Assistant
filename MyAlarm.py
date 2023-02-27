import datetime
import winsound

def alarm(Timing):
    altime = str(datetime.datetime.now().strftime(Timing, "%I:%M %p"))
    altime = altime[11:-3]
    print(altime)
    Horeal  = altime[:2]
    Horeal = int(Horeal)
    Mireal = altime[3:5]
    Mireal = int(Mireal)
    print(f"reminder at {Timing}")
    while True:
        if Horeal == datetime.datetime.now().hour:
            if Mireal == datetime.datetime.now().minute:
                print("reminder!")
                winsound.PlaySound('abc', winsound.SND_LOOP)
            elif Mireal<datetime.datetime.now().minute:
                break
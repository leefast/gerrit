import signal
import time
import sys
def ExitHandler(singnum, stack_frame):
    print("Receice signal %s!!!" %singnum)
    sys.exit(singnum)



if __name__ == '__main__':
    catchable_signals = set(signal.Signals)
    for sig in catchable_signals:
        try:
            signal.signal(sig, ExitHandler)
        except (ValueError, OSError, RuntimeError) as m:
            pass
    time.sleep(1000)
    
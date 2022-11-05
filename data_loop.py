from datetime import datetime
import sys
import time
import traceback
import jsonpickle
from CompyterClasses import Computer


# The aim with this script is to have at least one continous loop of data gathering.
# Next steps will be focused on storing the data in a MySQL database.
# After that, that data will be migrated to Django. And finally, represented under a webpage.

def save_data_to_file(compyter_class):
    with open("compyter.json","w") as outfile:
        outfile.write(jsonpickle.encode(compyter_class))



# Argument 1: Seconds between timestamps. I recommend at least 60 seconds. If no arguments, 120 seconds are set.

def main():
    try:
        time_interval=sys.argv[1]
    except IndexError:
        #logging.WARN("No arguments provided. 60 sec set.")
        time_interval=120
    this_computer=Computer()
    while True:
        this_computer.add_timestamp()
        print("[",datetime.now(),"]: Saved timestamp. Waiting ",time_interval,"secs.")
        try:
            time.sleep(time_interval)
        except KeyboardInterrupt:
            save_data_to_file(this_computer)
            sys.exit(0)
        except Exception:
            traceback.print_exc(file=sys.stdout)
            sys.exit(0)


if __name__ == "__main__":
    main()
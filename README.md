# CompyterStats
## What does it (going to) do?
Check the status of multiple computers in your LAN in a web-interface. This includes (and is not limited to) CPU, RAM, Disk usage, most resource-intensive processes...

I'm planning to make the MySQL database compatible with Grapahana with a how-to guide on setting it up.

## Requirements
The only required thing apart from the dependencies stated in the requirements.txt is a MySQL installation for the main host computer.

I highly recommend using a Virtual Environment.

## Installation

1. Install MySQL and create a user, password and database.
2. Put the access credentials and database name in *interactor.py* and  */compyter_stats/compyter_stats/settings.py*
3. Migrate the database using Django:
```
cd compyter_stats
python manage.py makemigrations compyter_stats  
python manage.py migrate
```
4. Run data_loop.py 

## How does it (going to) work?
A main computer hosts the web interface, showing data gathered from all the others computers. These send the data to the main computer so it can include the information in the main database. This design implies that the program will leave a heavier footprint in the main computer but a smaller one in the other ones.

Right now I haven't a clear sense about which data is useful and needed, but I aim to show enough to let administrators have a clear understanding about what processes are taking the most resources in a domains machine, but trying to avoid bloat and unneccesary data that may take too much space in the database.

This and other design choices are yet to be made and determined. I'm always open for suggestions.

## What's the state of the project right now?
As of December 27th, the data gets added to the MySQL database. The only thing left is the frontend.

On the other hand, if you have any suggestion that isn't related to fake confidential info being exposed, feel free to ping me or make a PR! I'm learning and any advice is greatly appreaciated.

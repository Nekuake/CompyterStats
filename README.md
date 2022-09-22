# CompyterStats
## What does it (going to) do?
Check the status of multiple computers in your LAN in a web-interface. This includes (and is not limited to) CPU, RAM, Disk usage, most resource-intensive processes...

## How does it (going to) work?
A main computer hosts the web interface, showing data gathered from all the others computers. These send the data to the main computer so it can include the information in the main database. This design implies that the program will leave a heavier footprint in the main computer but a smaller one in the other ones.

Right now I haven't a clear sense about which data is useful and needed, but I aim to show enough to let administrators have a clear understanding about what processes are taking the most resources in a domains machine, but trying to avoid bloat and unneccesary data that may take too much space in the database.

This and other design choices are yet to be made and determined. I'm always open for suggestions.

## What's the state of the project right now?
As of September 13th of 2022, this projects is almost just testing of the Django framework. Any secret data here is not being used in any environment exposed to the Internet. You can scan for passwords here and make a pull request if you want to but it will be most probably ignored. 

On the other hand, if you have any suggestion that isn't related to fake confidential info being exposed, feel free to ping me or make a PR! I'm learning and any advice is greatly appreaciated.

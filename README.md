# CompyterStats
## What does it (going to) do?
Check the status of multiple computers in your LAN in a web-interface. This includes (and is not limited to) CPU, RAM, Disk usage, most resource-intensive processes...

## How does it (going to) work?
A main computer hosts the web interface, showing data gathered from all the others computers. These send the data to the main computer so it can include the information in the main database. This design implies that the program will leave a heavier footprint in the main computer but a smaller one in the other ones.

Right now I haven't a clear sense about which data is useful and needed, but I aim to show enough to let administrators have a clear understanding about what processes are taking the most resources in a domains machine, but trying to avoid bloat and unneccesary data that may take too much space in the database.

This and other design choices are yet to be made and determined. I'm always open for suggestions.
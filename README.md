# statusbot
a Flask webapp for posting messages about your network. uses the Materialize CSS web framework.
statusbot has been validated to work on Debian 8.8 and Windows, and theoretically should work fine on anything else.

## installing statusbot
Installation is simple:
- Install MongoDB, however your operating system mandates.
- Install the latest version of Python 3 available for your distribution. Note that versions below 3.4 have not been officially tested and might not work.
- Run the following command:
```bash
pip install pymongo flask
```
- Change whatever values you see fit in the statusbot_settings.py file - this is all nicely commented out so you know what changes what.
- Start the server by using the init.sh provided, or running the app in python normally. Note that using the init.sh will start a screen session, which will fail if screen is not installed.

## adding stuff to statusbot
For the time being, there's a Python script (db_add.py) that will automate the process of adding items to the database for you. Later on, this will be done through the web interface.

## playing with statusbot
The entire web interface is templated using jinja2, so that you can easily change stuff like the navbar and have it work across all pages. The backend code, while a bit messy, is also quite simple to modify.

Unfortunately, the codebase is a bit of a mess in its current state. The next task at hand is to clean it up and make it more functional, so that it can be changed more easily. One particular pain point is the issues.html template, which will eventually be further templated to ease the process of modifying the issue cards.

## planned features
There's a lot in the pipeline for statusbot, in chronological order:
- List of affected servers for each card. There are actually already provisions for this in the database, but there's nothing on the frontend just yet.
- Admin panel, to enable adding, removing, and updating issues to statusbot.
- Email alerts using sendgrid, so that users can subscribe to issues affecting certain servers.
- Metrics for servers (e.g. a ping graph, cpu usage, etc.)

Thanks for checking out statusbot, and feel free to submit a pull request if you wish! Hacking on the code is absolutely encouraged, and you're welcome to use the code for whatever you want. <3

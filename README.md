# BitBar-Scripts

## Installation (Mac only)
1. Install [BitBar](https://getbitbar.com/) and choose a location for your plugins folder.
2. Download and extract this repo and move the 2 scripts into the plugins folder.
3. Give each script executable permissions by running `chmod +x [script filename]`.
4. Install `pip` if you haven't already by running `sudo easy_install pip`.
5. Install the `requests` package using `pip install requests`.
6. In the menu bar, go to BitBar > Preferences > Refresh All.
7. You should now see the plugins in the menu bar.

### Coronavirus country specific setup
1. Open the `coronavirus-uk.py` file in any text editor.
2. Change line 26 `if x["country"] == "UK":` to `if x["country"] == "{country name}":`
3. In the menu bar, go to BitBar > Preferences > Refresh All.

# Package ~ directory containing multiple modules and sub-packages
# why is package helpful ~ organizes larger project
# divide large project into modules ~ group related modules into a sub-packages,
# then group sub-packages into a package

print("create a package")
import game.characters.player
game.characters.player.getplayer_info()
print()

# pip ~ standard package manager for python that helps to instuall
# and manage additional packages that are not avaliable in the python
# standard library
print("pip ~ standard package manager")
print("installed pandas 'pip install <name of package>'")
print("'pip list' ~ to see all the packages installed")
import pandas as pd
print(pd)
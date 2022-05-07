import pystray
import PIL.Image

# importing the bot settings
from bot import *

image = PIL.Image.open("icon.png")

def on_clicked(icon, item):
    if str(item) == 'Start bot':
        main()
    elif str(item) == 'Exit':
        icon.stop()
    # elif str(item) == 'Submenu Item 1':
    #     print('Sub 1')
    else:
        print('Not Implemented yet!')

icon = pystray.Icon("Assistant", image, menu=pystray.Menu(
    pystray.MenuItem("Start bot", on_clicked),
    pystray.MenuItem("Exit", on_clicked),
    # creating submenus
    # pystray.MenuItem("Submenu", pystray.Menu(
    #     pystray.MenuItem("Submenu Item 1", on_clicked),
    # ))
))

icon.run()
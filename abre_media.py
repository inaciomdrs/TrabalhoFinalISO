# -*- coding: iso-8859-1 -*-
# Baseado no código mostrado nesse site

import requests
import json
import urllib
import sys

from Handler import Handler

path = sys.argv[1]

handler = Handler()
	
handler.method = "Playlist.Clear"
handler.params = {"playlistid":1}
response = handler.post()

handler.method = "Playlist.Add"
handler.params = {"playlistid":1, "item" :{ "file" : path}}
response = handler.post()

handler.method = "Player.Open"
handler.params = {"item":{"playlistid":1, "position" : 0}}
response = handler.post()

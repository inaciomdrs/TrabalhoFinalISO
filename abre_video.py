# -*- coding: iso-8859-1 -*-

import requests
import json
import urllib
from Handler import Handler

path = "/media/inacio-medeiros/Expansion Drive/Anime/Gundam Wing/01 - The Shooting Star She Saw.avi"

handler = Handler()
	
handler.method = "Playlist.Clear"
handler.params = {"playlistid":1}
response = handler.post()
print response

handler.method = "Playlist.Add"
handler.params = {"playlistid":1, "item" :{ "file" : path}}
response = handler.post()
print response

handler.method = "Player.Open"
handler.params = {"item":{"playlistid":1, "position" : 0}}
response = handler.post()
print response

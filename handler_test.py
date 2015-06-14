# -*- coding: iso-8859-1 -*-

# ESTE PROGRAMA PAUSA UMA MÚSICA QUE TIVER TOCANDO NO KODI (OU DESPAUSA, SE ELA JÁ TIVER PAUSADA)

import requests
import json
import urllib
from Handler import Handler

handler = Handler()

handler.method = "Player.GetActivePlayers"
response = handler.get()

#response.text will look like this if something is playing
#{"id":1,"jsonrpc":"2.0","result":[{"playerid":1,"type":"video"}]}
#and if nothing is playing:
#{"id":1,"jsonrpc":"2.0","result":[]}
     
data = json.loads(response.text)
#result is an empty list if nothing is playing or paused. 
if data['result']:
	#We need the specific "playerid" of the currently playing file in order to pause it
	player_id = data['result'][0]["playerid"]

	handler.method = "Player.PlayPause"
	handler.params = { "playerid": player_id }
	
	response = handler.post()

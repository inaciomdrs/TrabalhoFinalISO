# -*- coding: iso-8859-1 -*-

# CLASSE HANDLER
# É a classe responsável pela comunicação da aplicação com o Kodi

import requests
import json
import urllib

############################## CLASS HANDLER ############################## 
class Handler:
	def __init__(self,host='localhost',port=8080):
		self.headers = {'content-type': 'application/json'} # Cabeçalhos para comunicação com o Kodi
		# "Socket" de comunicação
		self.xbmc_host = host # IP
		self.xbmc_port = port # Porta
		# URL de requisição
		self.xbmc_json_rpc_url = "http://" + self.xbmc_host + ":" + str(self.xbmc_port) + "/jsonrpc" 
		# Algumas diretivas padrão
		self.payload = {"jsonrpc": "2.0", "method": '', "id": 1}
		# Método JSON-RFC que vai ser executado no Kodi
		self.method = ''
		# (Caso o método precise) Parâmetros de configuração do método
		self.params = ''
	
	# Gets e Sets de metodo e parametro
	@property
	def method(self):
		return self.method
	@method.setter
	def method(self, value=''):
		self.method = value
	
	@property
	def params(self):
		return self.params
	@params.setter
	def params(self, value=''):
		self.params = value
	
	# Executa um GET, com base no método e parâmetro previamente especificado
	def get(self):
		self.payload["method"] = self.method
		url_param = urllib.urlencode({'request': json.dumps(self.payload)})
		return requests.get(self.xbmc_json_rpc_url + '?' + url_param,headers=self.headers)
	
	# Executa um POST, com base no método e parâmetro previamente especificado
	def post(self):
		self.payload["method"] = self.method
		self.payload["params"] = self.params
		return requests.post(self.xbmc_json_rpc_url, data=json.dumps(self.payload),headers=self.headers)
############################## CLASS HANDLER ############################## 

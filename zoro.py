import requests
class Client():
	def __init__(self):
		self.api="https://zoro.to/ajax"
		self.headers ={"Accept-Encoding": "*r","Referer": "https://zoro.to/","Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"}
	def episode_service(self,id:str):
		return requests.get(f"{self.api}/v2/episode/servers?episodeId={id}",headers =self.headers).json()
	def search(self,key:str):
		return requests.get(f"{self.api}/search/suggest?keyword={key}",headers =self.headers).json()
	def episode_sources(self,id:str):
		return requests.get(f"{self.api}/v2/episode/sources?id={id}",headers =self.headers).json()
	def episode_list(self,id:str):
		return requests.get(f"{self.api}/v2/episode/list/{id}",headers =self.headers).json()
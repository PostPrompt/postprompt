from pplib import json_parser

class Model:
	def __init__(self,uid):
		self.games = {}
		self.logged_in_uid = uid
		self.current_game_id = None
		self.version = 0

	def update_game(self,resp):
		#with open("ASDF.json","w") as f:
		#	f.write(str(resp))
		obj = json_parser.create_object(resp)
		respType = json_parser.get_string(obj,"respType")
		if respType == "ok":
			command = json_parser.get_string(obj,"command")
			gameId = json_parser.get_int(obj,"gameId")
			message = json_parser.get_string(obj,"message")
			gameRepr = json_parser.get_object(obj,"gameRepr")
			self.games[gameId] = Game(json_parser.get_object(gameRepr,"game"))
			self.current_game_id = gameId
			return message
		else:
			return 'Received error message: %s'%respType

	def get_current_game(self):
		return self.games[self.current_game_id]

class Game:
	def __init__(self,obj):
		self.me = Player_Container(json_parser.get_object(obj,'me'))
		self.them = Player_Container(json_parser.get_object(obj,'them'))
		self.super_phase = json_parser.get_int(obj,'superPhase')
		self.phase = json_parser.get_int(obj,'phase')
		self.turn_owner = json_parser.get_int(obj,'turnOwner')
		self.has_drawn = json_parser.get_bool(obj,'hasDrawn')

class Player_Container:
	def __init__(self,obj):
		self.uid = json_parser.get_int(obj,'uid')
		self.name = json_parser.get_string(obj,'name')
		self.health = json_parser.get_int(obj,'health')
		self.deck    = Card_List(json_parser.get_object(obj,'deck'))
		self.hand    = Card_List(json_parser.get_object(obj,'hand'))
		self.active  = Card_List(json_parser.get_object(obj,'active'))
		self.grave   = Card_List(json_parser.get_object(obj,'grave'))
		self.special = Card_List(json_parser.get_object(obj,'special'))

class Card_List:
	def __init__(self,obj):
		self.cards = []
		for card_element in json_parser.get_objects(obj,'cards'):
			self.cards.append(Card(card_element))

class Card:
	def __init__(self,obj):
		card = json_parser.get_object(obj,'card')
		self.name = json_parser.get_string(card,'name')

from src.model.player.player_container import Player_Container
from src.model.player import player_type
from src.model.phase.turn import Turn
from random import randint

class Game:
	def __init__(self,player1=None,player2=None):
		self.players = []
		if player1 != None:
			self.players.append(player1)
		else:
			self.players.append(Player_Container())
		if player2 != None:
			self.players.append(player2)
		else:
			self.players.append(Player_Container())
		self.current_turn_owner = self.decide_first_player()

	def decide_first_player(self):
		who = randint(0,1)
		who = 0
		return self.players[who].player.uid

	def get_me_from_uid(self,uid):
		if self.players[0].player.uid == uid:
			return self.players[0]
		elif self.players[1].player.uid == uid:
			return self.players[1]
		else:
			raise Exception("Not the uid of a player playing this game")

	def get_them_from_uid(self,uid):
		if self.players[0].player.uid == uid:
			return self.players[1]
		elif self.players[1].player.uid == uid:
			return self.players[0]
		else:
			raise Exception("Not the uid of a player playing this game")

	def xml_output(self,uid):
		out_str = "<game>"
		out_str += "<me>"
		out_str += self.get_me_from_uid(uid).xml_output(player_type.me)
		out_str += "</me>"
		out_str += "<them>"
		out_str += self.get_them_from_uid(uid).xml_output(player_type.them)
		out_str += "</them>"
		out_str += "</game>"
		return out_str


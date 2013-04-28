import os

from pplib.errors import PP_Load_Error, PP_Database_Error
from pplib import database

from model.game import Game
from model.player import Player_Container, Player
from model.collection import Collection
from control.loaded_effects import lookup_table

card_id_to_card_text = {}

def load_card_key_text():
	if card_id_to_card_text == {}:
		try:
			cards = database.select('play_card_names','*')
			for card in cards:
				key = int(card[0])+1
				val = card[2]
				if not card_id_to_card_text.has_key(int(key)):
					card_id_to_card_text[int(key)] = val
				else:
					raise PP_Load_Error("Duplicate keys in card table: %s"%key)
			if card_id_to_card_text == {}:
				raise PP_Load_Error("No data in the card table")
		except PP_Database_Error:
			raise PP_Load_Error("Could not load the card table")

def get_game(config_args):
	load_card_key_text()
	uids = [config_args.uid1,config_args.uid2]
	dids = [config_args.did1,config_args.did2]
	players = []
	for i in range(0,2):
		name = database.select('auth_user','username',where=(('id='+str(uids[i])),))[0]
		player = Player(uid=uids[i],name=name)
		cards = []
		#try:
		if True:
			deck = database.select('play_decks','card_id',where=(('uid='+str(uids[i])),('deck_id='+str(dids[i]))))
			deck = [database.select('play_cards','card_name_id',where=(('id='+str(card)),))[0] for card in deck]
		#except Exception:
		#	raise PP_Load_Error("Could not load the player's deck")
		for card_id in deck:
			cards.append(lookup_table(get_card_key_text_from_id(card_id)))
		verify_deck(cards)
		player_collection = Collection(cards=cards)
		players.append(Player_Container(player=player,collection=player_collection))

	return Game(player1=players[0],player2=players[1])

def verify_deck(cards):
	if len(cards) < 30:
		raise PP_Load_Error("Not enough cards in the player's deck, only %s, needs 40"%str(len(cards)))

def get_card_key_text_from_id(card_id):
	try:
		text = card_id_to_card_text[int(card_id)]
		return text
	except ValueError:
		raise PP_Load_Error("Player deck data contained card id %s which is not an int"%str(card_id))
	except KeyError:
		raise PP_Load_Error("Player deck data contained card id %s is not a valid card id"%str(card_id))

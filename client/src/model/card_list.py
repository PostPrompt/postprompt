from src.model.card import Card
from pyplib.xml_parser import parse_int, parse_element

class Card_List:
	def __init__(self,element):
		size = parse_int(element,'num')
		self.cards = []
		#TODO right now will just get n copies of the first card!
		for i in range(size):
			self.cards.append(Card(parse_element(element,'cards')))

		def __iter__(self):
			return self.cards

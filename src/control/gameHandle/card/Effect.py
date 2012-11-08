from src.control.gameHandle.card.instant.Instant import InstantList
from src.control.gameHandle.card.persist.Persist import PersistCondList
from src.control.gameHandle.card.pactivate.PersistActivate import PersistActivateList

class Effect:
	def __init__(self,instants,persists,pactivates,elements):
		self.instants = instants
		self.persists = persists
		self.pactivates = pactivates
		if type(elements) is list or type(elements) is tuple:
			self.elements = tuple(elements)
		else:
			self.elements = (elements)

	def onActivate(self,game,uid):
		self.instants(game,uid)

	def accountFor(self,game,uid,action):
		self.pactivates.accountFor(game,uid)

	def doesPersist(self,game,uid):
		self.persists(game,uid)

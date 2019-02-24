
class boss():
	def __init__(self,name,money,charisma):
		self.name=name
		self.money=money
		self.charisma=charisma
		self.taraftarguveni=50
		self.medyadurumu=50

class team():
	def __init__(self,name,boss,reputation):
		self.name=name
		self.boss=boss
		self.reputation=reputation
		self.position=1

class manager():
	def __init__(self,name,intel,tactic,influence,team):
		self.name=name
		self.intel=intel
		self.tactic=tactic
		self.influence=influence
		self.team=team
		self.morale=50

class player():
	def __init__(self,name,intel,age,peak,form,team):
		self.name=name
		self.intel=intel
		self.age=age
		self.peak=peak
		self.form=form
		self.team=team
		self.speed=50
		self.stamina=50
		self.power=50
		self.workrate=5
		self.leadership=1

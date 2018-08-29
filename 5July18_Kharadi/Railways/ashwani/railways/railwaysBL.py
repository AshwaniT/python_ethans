import railways.railwaysDA as db
def login(username,password):
	for user in db.getusers():
		if user['username']==username and password==user["password"]:
			return True
		return False
def CreateUser(username,password,role):
	db.setUsers(username,password)
	db.SetuserInRoles(username,role)

def canchangepassword(actorname,username):
	actor_role=db.userrole(username)
	if actor_role and actor_role=='admin':
		return True
	elif actorname==username:
		return True
	return False

def change_password(actorname,username,password):
	if db.canchangepassword(actorname,username):
		return db.change_password(username,password)
	return False
def get_trains(source,dest):
	return db.gettrain(source,dest)

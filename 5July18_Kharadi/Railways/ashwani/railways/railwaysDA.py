#from railways import * #not working
import railways

def loadtrains():
	#print trains
	railways.trains.append({'number':1, 'name':'Agra fort', 'to':'Mumbai', 'from':'Agra','seats':railways.seats.copy() })
	railways.trains.append({'number':2, 'name':'Agra fort', 'from':'Mumbai', 'to':'Agra','seats':railways.seats.copy() })
	railways.trains.append({'number':4, 'name':'Suhldev Exp', 'to':'Ghazipur', 'from':'Delhi','seats':railways.seats.copy() })
	railways.trains.append({'number':5, 'name':'Suhldev Exp', 'to':'Delhi', 'from':'Ghazipur','seats':railways.seats.copy() })
def get_train_bynumber(number):
	for tr in railways.trains:
		if tr['number']==number:
			return tr
	return {}
	
def gettrain(to,from1):
	for x in railways.trains:
		if x["to"]==to and x["from"]==from1:
			return x
	return {}
def loadusers():
	 railways.users.append([{'username':'Ashwani','password':'1234'},{'username':'Kumar','password':'xyz'},{'username':'Tiwari','password':'!@#'}])
def loadusersinroles():
	 railways.userInRoles.append([{'username':'Ashwani','role':'admin'},{'username':'Kumar','role':'customer'},{'username':'Tiwari','role':'customer'}])

def getusers():
	return railways.users
def setUsers(username,password):
	railways.users.append({'username':username,'password':password})
def GetuserInRoles():
	return railways.userInRoles
def SetuserInRoles(username,role):
	railways.userInRoles.append({'username':username,'role':role})

def getuser(username):
	for user in railways.users:
		if user['username']==username:
			return user
	return {}
def changepassword(username, passowrd):
	searched_user=getuser(username)
	if searched_user:
		searched_user["password"]=passowrd
		return True
	return False
def bookticket(trainnumber,to,dest,passengrname,age,sex,seat):
	railways.tickets.append({'trainnumber':trainnumber,'to':to,'from':dest,'passengrname':passengrname,'age':age,'sex':sex,'seat':seat})

def userrole(username):
	for ur in railways.userInRoles:
		if ur["username"]==username:
			return ur["role"]
	return ''




























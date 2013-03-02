import sqlite3
import os
from pyplib.errors import PP_Database_Error

database_path = os.path.join(os.environ['pyproot'],'opt','postprompt','database')
con = sqlite3.connect(database_path)
cur = con.cursor()

def insert(table_name,types,values):
	try:
		command = "insert into "+table_name+" values("
		for t in types:
			if t == int:
				command+="%s,"
			elif t == str:
				command+= "'%s',"
			else:
				raise Exception ('Unknown data type')
		command = command[:-1]
		command += ")"
		command = command%values
		cur.execute(command)
		con.commit()
	except sqlite3.OperationalError:
		raise PP_Database_Error("Database Error (database doesn't exist)")

def update(table_name,set_name,set_value,checks):
	try:
		command = 'update '+table_name+' set '+set_name+"='"+set_value+"' where "
		for key,value in checks:
			command += str(key)+"="+str(value)+" and "
		command = command[:-4]
		cur.execute(command)
		con.commit()
	except sqlite3.OperationalError:
		raise PP_Database_Error("Database Error (database doesn't exist)")

def select(table_name,name,where=None):
	try:
		command = 'select '+name+' from '+table_name
		if where != None:
			command += ' where '
			for w in where:
				command += w+' and '
			command = command[:-4]
		cur.execute(command)
		return cur.fetchall()
	except sqlite3.OperationalError:
		raise PP_Database_Error("Database Error (database doesn't exist)")

def delete(table_name):
	try:
		command = 'delete from '+table_name
		cur.execute(command)
		con.commit()
	except sqlite3.OperationalError:
		raise PP_Database_Error("Database Error (database doesn't exist)")

def in_table(table_name,name,value):
	return str(value) in database.select(tabel_name,name)
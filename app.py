import pymongo
from pymongo import MongoClient, GEO2D
import bottle
from  bottle import Bottle,route,run,request,template,static_file,default_app,get
from sys import argv

@route ('/', method="get" )
def inicio():
	return template ('template.tpl')

@route ('/resultado', method="post")
def resultado():
	usu = request.forms.get('usuario')
	cla = request.forms.get('clave')
	col = request.forms.get('coleccion')

	uri= "mongodb://"+usu+":"+cla+"@172.22.200.109:27017"

	cliente= MongoClient(uri)

#	db=cliente.col

	cursor=db.col.find()

	result=[]

	for resultado in cursor:
		result.append(resultado)

	return template ('template2', result=result)

run(host='0.0.0.0',port=argv[1])
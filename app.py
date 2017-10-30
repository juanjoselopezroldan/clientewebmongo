import pymongo
from pymongo import MongoClient, GEO2D
import bottle
from  bottle import Bottle,route,run,request,template,static_file,default_app,get
from sys import *
import json

@route ('/', method="get" )
def inicio():
	return template ('template.tpl')

@route ('/resultado', method="post")
def resultado():
	usu = request.forms.get('usuario')
	cla = request.forms.get('clave')
	col = request.forms.get('coleccion')
	
	uri= "mongodb://"+usu+":"+cla+"@172.22.200.109:27017/"+col
	
	cliente= pymongo.MongoClient(uri)
	db= cliente.col
	cursor= db.db.find()
	# contenido=[]

	# for result in cursor:
	#  	contenido.append(result)

	return template ('template2', cursor=cursor)

run(host='0.0.0.0',port=argv[1])
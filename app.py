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
	
	uri= "mongodb://"+usu+":"+cla+"@172.22.200.109:27017/test"

	cliente= MongoClient(uri)
	datos= cliente['test']
	coleccion= datos[col]
	cursor= coleccion.find()
	contenido=[]

	for result in cursor:
	  	contenido.append(result)

	if col == "zip" or col == "product":
		return template ('template2', cursor=contenido, col=col)
	else:
		return template ('error', cursor=contenido, col=col)

run(host='0.0.0.0',port=argv[1])
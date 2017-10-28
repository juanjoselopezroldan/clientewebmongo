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

	uri= "mongo://"+usu+":"+cla+"/"+col

	cliente= MongoClient (uri)

	return template ('template2', cliente=cliente)

run(host='0.0.0.0',port=argv[1])
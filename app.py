import pymongo
from pymongo import MongoClient, GEO2D
import bottle
from  bottle import Bottle,route,run,request,template,static_file,default_app,get

@route ('/', method="get" )
def inicio():
	return template ('template.tpl')

@route ('/resultado'method="post")
def resultado():
	usu = request.forms.get('usuario')
	cla = request.forms.get('clave')
	return template ('template2', usuario=usu, clave=cla)

run(host='0.0.0.0',port=argv[1])
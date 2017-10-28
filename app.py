import pymongo
from pymongo import MongoClient, GEO2D
import bottle
from  bottle import Bottle,route,run,request,template,static_file,default_app,get

@route ('/', method="get" )
def inicio():
	return template ('template1.tpl')

@route ('/resultado'method="get")
def resultado():
	usu = request.forms.get('usuario')
	cla = request.forms.get('clave')
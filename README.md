# clientewebmongo
Cliente Web de Mongo realizado en python

Este cliente para consultas en base de datos mongodb esta reaizado con python sobre bottle.

En el caso de necesitar este programa, saber que funciona correctamente ya que se le han
realizado las pruebas necesarias que determinan su correcto funcionamiento.

En dicho repositorio dejo el requirements.txt que indica que versiones de programas he llegado a utilizar.

A continuacion se describe el funcionamiento del programa por partes (si o necesitas tendrias que cambiar los parametros necesarios para que se adapte a su caso)



/
import pymongo
from pymongo import MongoClient, GEO2D
import bottle
from  bottle import Bottle,route,run,request,template,static_file,default_app,get
from sys import *
import json
\		(Importación de los complementos necesarios para la ejecución del .py)




/
@route ('/', method="get" )
def inicio():
	return template ('template.tpl')
\		(Redirección al primer template que contiene un formulario para la solicitud de la coleccion)





/
@route ('/resultado', method="post")
def resultado():
	usu = request.forms.get('usuario')
	cla = request.forms.get('clave')
	col = request.forms.get('coleccion')
\		(Recogida de información del formulario de datos de usuario, colección y asignación a las variables)





/	
	uri= "mongodb://"+usu+":"+cla+"@172.22.200.109:27017/test"
\		(Dirección para el acceso a la base de datos con los datos de cuenta de usuario y base de datos)





/
	cliente= MongoClient(uri)
	datos= cliente['test']
	coleccion= datos[col]
	cursor= coleccion.find()
\		(Petición con la función de mongoclient, petición a base de datos con credenciales y búsqueda de información en la colección indicada)





/
	contenido=[]
	for result in cursor:
	  	contenido.append(result)
\		(Recorrer resultado del cursor del diccionario de respuesta y agregación en una lista para mostrarla posteriormente el resultado de dicha petición en el template)




/
	if col == "zip" or col == "product":
		return template ('template2', cursor=contenido, col=col)
	else:
		return template ('error', cursor=contenido, col=col)
\		(Redirección del contenido al template deseado en caso de haber introducido la colección correctamente, en el caso de no haberlo introducido correctamente nos redirige a otro template con un mensaje de error)





/
run(host='0.0.0.0',port=argv[1])
\		(Función necesaria para la correcta ejecución en el entorno virtual de bottle)

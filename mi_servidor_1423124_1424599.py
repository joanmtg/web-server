#!/usr/bin/env python

import commands
import os
from socket import *

s = socket(AF_INET,SOCK_STREAM)
port=9000
s.bind(("",port))
s.listen(5)

while True:
	c,a = s.accept()
    	rec = c.recv(100000)
	lista = rec.split(" ")
	
	if lista != ['']:

		peticion = lista[1]
		print "Received connection from", a

		c.send("HTTP/1.0 200 OK \r\n")
        	c.send("Content-type, text/html\r\n")
	        c.send("\r\n")

		
		if peticion in ["/index.html", "/index.htm", "/"]:

			c.send("<p>Servidor Web presentado por:<br>1423124 Tovar <br>1424599 Calero</p>")

		elif peticion == "/dir":

			resultado = commands.getoutput("ls")
			directorios = resultado.split("\n")

			c.send("<h1>Listado de archivos</h1>")
		
			for dir in directorios:
			
				if os.path.isfile(dir):
					c.send("<a href='http://localhost:%s/%s'>%s</a><br>"%(port,dir,dir))

		else:
			nombreArchivo = peticion.replace("/", "")
		
			if os.path.exists(nombreArchivo):

				contenido = commands.getoutput("cat %s"%(nombreArchivo))
				c.send(contenido)
		
			else:
				c.send("<html> <h3> El archivo %s no fue encontrado </h3> </html>"%(nombreArchivo))
	

		c.close()




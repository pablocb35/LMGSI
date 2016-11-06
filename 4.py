#!/public_html/LM/B1Prog$ ipython 
#-*- coding: utf-8 -*-


def operacion (lista):
	
	resultado = 0
	
	if 'operacion' == 'sumar':
		
		for elemento in lista:
		resultado = resultado + elemento
		
	else 'operation' == 'restar':
		
		for elemento in lista:
		resultado = resultado - elemento
	
	return resultado


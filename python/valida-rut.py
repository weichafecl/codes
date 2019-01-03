###########################################################
# This code validate the chilean ID (RUT)
# Regex is used for identify the inputed ID
# The Check Digit Algorithm Mod 11 is applied to validate 
# the inputed digit ID
###########################################################

import re

rut_ingresado = input('Ingrese su RUT: ')

match = re.search(r'\d{0,1}\d.{0,1}\d\d\d.{0,1}\d\d\d-{0,1}\d',rut_ingresado)

if match:
	
	#extrae los numeros del rut ingresado(sin simbolos)
	num_rut = re.findall(r'\d+',rut_ingresado)	

	rut = ''
	#concatena los digitos del rut ingresado
	for num in num_rut:
		rut = rut + num

	print('RUT informado:',rut)

	dv_informado = rut[len(rut)-1:]

	#se esta considerando un rut valido, un rut con un largo menor a 10 digitos (<100000000)
	if len(rut) < 10:

		#calculo digito verificador se leen los digitos de derecha a izquierda y
		#se multiplica por la serie 2,3,4,5,6,7.  se suman los resultados de cada
		#multiplicacion. Si se ha aplicado la serie hasta el final y quedan digitos
		#por multiplicar, se comienza nuevamente
	
		#rut inverso sin digito verificador
		rut_inv_sin_dv = rut[(len(rut)-2)::-1]

		#lista de series (2,3,4,5,6,7) de acuerdo al los digitos del rut
		series=[]	
		j=2
		for i in range(len(rut_inv_sin_dv)):
			if i <= 5:
				series.append(j)
				j+=1
			else:
				if (j>7):
					j = 2
				series.append(j)
				j+=1
	
		#lista de resultados de la serie x digitos del rut
		resultados=[]
		for n in range(len(rut_inv_sin_dv)):
			resultados.append(int(rut_inv_sin_dv[n]) * int(series[n]))

		#suma de los resultados
		suma = 0
		for x in range(len(resultados)):
			suma += int(resultados[x])

		#modulo 11
		modulo = suma%11

		#calculo dv
		dv = 11-modulo
		if dv == 11:
			dv_calculado = 0
		elif dv == 10:
			dv_calculado = 'K'
		else:
			dv_calculado = dv

		print('DV calculado:',dv_calculado)

		if str(dv_informado) == str(dv_calculado):
			print('RUT válido')
		else:
			print('RUT inválido')
	else:
		print('RUT inválido')
else:
	print('RUT inválido')	

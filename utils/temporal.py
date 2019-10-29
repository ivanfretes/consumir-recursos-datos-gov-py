
def prueba(buscado):

	while True:
		
		print("termino buscado \"{}\", en 5 archivos json".format(buscado))

		print("1 - Cantidad de coindicencias : 6")
		print("2 - Decretos / Reglamentos / Leyes  : 6")
		print("3 - Conlusiones Encontradas: 4")
		print("4 - Proyectos de Ley: 4")
		print("5 - Solicitudes Similares: 3")
		print("6 - Autoridades: 5")
		print("7 - Funcionarios: 50")
		print("8 - Oficinas: 5")
		print("9 - Presupuesto: N/A")
		print("10 - Entidades Relacionadas : 3")
		print("11 - Más Opciones ..")
		print("-1 - Salir")

		data_input = input()

		if data_input == '-1':
			print("Finalizado")
			exit()

		print("Por favor indique, el numero a visualizar")


	

if __name__ == '__main__':

	print("""
/////////////////////////////////////////////////////
		Bienvenido/a a IA Soluciones v0.0.5
/////////////////////////////////////////////////////		
		""")
	print("Por favor relacione un termino")
	_buscado = input()
	prueba(_buscado)

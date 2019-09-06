import pymysql
import pymysql.cursors
import time





con = pymysql.connect(host='localhost',
	user='root',
	password='senha',
	db='TrabalhoBD',
	charset='utf8',
	cursorclass=pymysql.cursors.DictCursor
	)



try:
	with con:

	 bazinga = 100

	 while bazinga != 5:

	 		
			print('1- Nova tarefa')
			print('2- Exibir lista')
			print('3- Concluir tarefa')
			print('4- Remover tarefa')
			print('5- Sair')
			print('-----------------')

			bazinga= int(input("Insira uma opcao: "))

			cur= con.cursor()



			if bazinga == 1:
				print('Nova tarefa')	
				
				now = time.strftime('%Y-%m-%d %H:%M')
				
				


				
				descricao= input("insira desc. da tarefa: ")
				prioridade = input("Prioridade (1,2 ou 3): ")

				concluido = "nao"

				
				cur.execute("INSERT INTO tarefas (descricao, prioridade, data, concluido) VALUES ('"+descricao+"','"+prioridade+"','"+now+"','"+concluido+"')")
				



			if bazinga == 2:
				cur.execute("SELECT * FROM tarefas")
				rows = cur.fetchall()

				print("----------------------------------------------------------------------------")
				print("| id | descricao | data | prioridade | concluida |")

				for row in rows:
					print("----------------------------------------------------------------------------")
					print("|",row["id"],"|", row["descricao"],"|", row["data"],"|", row["prioridade"],"|", row["concluido"],"|")

				print("----------------------------------------------------------------------------")


			if bazinga == 3:

			
				idd=input("insira id: ")
				

				cur = con.cursor()
				cur.execute("UPDATE Tarefas SET concluido='sim' WHERE id='"+idd+"'")

			if bazinga == 4:

			
				idd2=input("Insira id: ")

				
				cur.execute("DELETE FROM Tarefas WHERE id = '"+idd2+"' ")

finally:
    con.close()








		
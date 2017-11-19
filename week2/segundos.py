segundos = input("Por favor, entre com o número de segundos que deseja converter: ")
segundos = int(segundos)

dias = segundos // 86400
segundos = segundos % 86400
horas = segundos // 3600
segundos = segundos % 3600
minutos = segundos // 60
segundos = segundos % 60

#2 dias, 1 horas, 36 minutos e 55 segundos.
print(dias,"dias,",horas,"horas,",minutos,"minutos e",segundos,"segundos.")


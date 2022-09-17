#Importamos primeramente date, para poder manejar el formato "fechas"
from datetime import date
#A continuación, definimos la fecha futura que queremos en formato YYY-MM-DD
#future_date = date(2020, 12, 31)
future_date = date(2022,11,11)
#Ahora vamos a definir el día de hoy, la fecha actual.
today = date.today()
#Posterior a ello realizamos una resta entre estas fechas y lo convertimos a días.
remaining_days = (future_date - today).days
#Finalmente mandamos a imprimir los días restantes
print(f"Faltan {remaining_days} días para fin de año")
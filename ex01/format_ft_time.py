import time
import datetime

#valeur en secondes
epoch_time = time.time()

#Format avec float 4 chiffres et e+
formatted_epoch_time = f"Seconds since January 1, 1970: {epoch_time:.4f} or {epoch_time:.2e} in scientific notation"

#donne la date format Mois date annee
current_time = datetime.datetime.now().strftime("%b %d %Y")


print(formatted_epoch_time)
print(current_time)
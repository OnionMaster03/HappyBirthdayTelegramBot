import pickle
import time
now = time.localtime()
bd = {"chat_id" : "INSERT HERE YOUR CHAT ID", "1" : {"giorno" : now[2], "mese" : now [1], "nome" : "UNNAMED"}}
pickle.dump(bd, open("INSERT HERE YOUR CHAT ID" + ".dates", "wb"))
db = {"db":["INSERT HERE YOUR CHAT ID.dates"]}
pickle.dump(db, open("database.db", "wb"))

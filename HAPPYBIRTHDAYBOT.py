import random
import time
import telepot
import pickle
def handle(msg):
    try:
        command = msg["text"]
    except:
        command = ""
    try:
        chat_id = msg["chat"]["id"]
    except:
        chat_id = None
    if command == "/start":
        bot.sendMessage(chat_id, "Buongiorno! Buonasera! Buonsalve! BUON COMPLEANNO! \n Un salutone dal Team di TechCompany ed Onicorp che vi offrono con questo bot la possibilità di ricevere un bell'augurio di compleanno nel giorno del genetliaco! \n Usa /set-n-d-m-N per aggiungere una persona con nome e data (Al posto di \"n\" potete inserire un numero intero a qualsiasi numero di cifre, al posto di \"d\" il giorno e al posto di \"m\" il mese, non chiediamo l'anno per mantenere la privacy, al posto di \"N\" inserire il nome)")
    elif command[:4] == "/set":
        inx = command.split("-")
        try:
            n = int(inx[1])
        except ValueError:
            bot.sendMessage(chat_id, "Ehy!" + str(inx[2]) + "non è un numero intero! Ricorda che valgono solo quelli!")
        except:
            bot.sendMessage(chat_id, "Errore sconosciuto contattare @TechCompany per segnalare l'errore (Numero errore: 01)")
        try:
            d = int(inx[2])
            if d > 31 or d < 1:
                raise ValueError
        except ValueError:
            bot.sendMessage(chat_id, "Ehy!" + str(inx[2]) + "non è un giorno, \"Trenta giorni a Novembre, con Aprile, Giugno e Settembre, di 28 ce n'è uno, tutti gli altri ne han 31!\"")
        except:
            bot.sendMessage(chat_id, "Errore sconosciuto contattare @TechCompany per segnalare l'errore (Numero errore: 02)")
        try:
            m = int(inx[3])
            if m > 12 or m < 1:
                raise ValueError
        except ValueError:
            bot.sendMessage(chat_id, "Ehy!" + str(inx[2]) + "non è un mese! I mesi vanno da 1 a 12")
        except:
            bot.sendMessage(chat_id, "Errore sconosciuto contattare @TechCompany per segnalare l'errore (Numero errore: 03)")
        try:
            if m == 2:
                if d > 28 or d < 1:
                    raise ValueError
            if m == 11 or m == 4 or m == 6 or m == 8:
                if d > 30 or d < 1:
                    raise ValueError
        except:
            bot.sendMessage(chat_id, "\"Trenta giorni a Novembre, con Aprile, Giugno e Settembre, di 28 ce n'è uno, tutti gli altri ne han 31!\"")
        n = str(inx[1])
        N = inx[4]
        try:
            bd = pickle.load(open(str(chat_id) + ".dates", "rb"))
            bd[n] = {"giorno" : d, "mese" : m, "nome" : N}
            pickle.dump(bd, open(str(chat_id) + ".dates", "wb"))
        except:
            bd = {"chat_id" : chat_id, n : {"giorno" : d, "mese" : m, "nome" : N}}
            pickle.dump(bd, open(str(chat_id) + ".dates", "wb"))
            db = pickle.load(open("database.db", "rb"))
            database = db["db"]
            database.append(str(chat_id) + ".dates")
            db = {"db": database}
            pickle.dump(db, open("database.db", "wb"))
    elif msg["TRUE"] == True:
        print("controllo avviato")
        try:
            db = pickle.load(open("database.db", "rb"))
        except EOFError:
            raise
        if db == None:
            print("Database Nullo")
            None
        else:
            print("Database pieno")
            database = db["db"]
            x = 0
            for i in database:
                print(database[x])
                bd = pickle.load(open(database[x], "rb"))
                print(bd)
                keys = bd.keys()
                values = bd.values()
                keys = list(keys)
                values = list(values)
                print(keys)
                print(values)
                z = 0
                for i in keys:
                    if keys[z] == "chat_id":
                        print("salto il chat_id")
                        None
                    else:
                        print("avvio il confronto")
                        c = keys[z]
                        print(c)
                        values2 = bd[c].values()
                        values2 = list(values2)
                        print(values2)
                        m = values2[1]
                        print(m)
                        d = values2[0]
                        print(d)
                        now = time.localtime()
                        cm = now[1]
                        print(cm)
                        cd = now[2]
                        print(cd)
                        if m == cm and cd == d:
                            if bd["chat_id"] == "INSERT HERE YOUR CHAT ID":
                                print("salto test")
                            else:
                                print("confronto riuscito")
                                bot.sendMessage(bd["chat_id"], "Buon Compleanno " + values2[2] +"!")
                    z += 1
                x+=1
bot = telepot.Bot('644563887:AAH0ZxPXxtIMkJoNOLj-SOoLjLFbXLfit-s')
bot.message_loop(handle)
print ('Il bot è in funzione')
while 1:
    msg = {}
    msg["TRUE"] = True
    handle(msg)
    msg["TRUE"] = False
    time.sleep(43200)

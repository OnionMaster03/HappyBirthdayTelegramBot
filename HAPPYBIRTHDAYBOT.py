import random
import time
import telepot
import pickle

def handle(msg):
    try:
        command = msg["text"]
    except:
        command = ""
    chat_id = msg["chat"]["id"]
    if command == "/start":
        bot.sendMessage(chat_id, "Buongiorno! Buonasera! Buonsalve! BUON COMPLEANNO! \n Un salutone dal Team di TechCompany ed Onicorp che vi offrono con questo bot la possibilità di ricevere un bell'augurio di compleanno nel giorno del genetliaco! \n Usa /set-n-d-m per aggiungere una persona con nome e data (Al posto di \"n\" potete inserire un numero intero a qualsiasi numero di cifre, al posto di \"d\" il giorno e al posto di \"m\" il mese, non chiediamo l'anno per mantenere la privacy)")
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
        bd = {"chat_id" : chat_id, n : None}
        

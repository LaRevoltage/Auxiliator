import telebot
import modules.exploitsearch as exploitsearch
import modules.wafmeow as wafmeow
import modules.scanner as scanner
import modules.censys as censys
bot = telebot.TeleBot("YOUR_TOKEN")
def extract_arg(arg):
    return arg.split()[1:]
@bot.message_handler(commands=['searchbyip'])
def searchbyip(message):
    try:
        IP=extract_arg(message.text)[0]
        info="\n".join(censys.SearchByIp(IP))
        bot.send_message(message.chat.id, info)
    except:
        bot.send_message(message.chat.id, "Error!")
@bot.message_handler(commands=['searchbydomain'])
def searchbydomain(message):
    try:
        domain=extract_arg(message.text)[0]
        info="\n".join(censys.SearchByDomain(domain))
        bot.send_message(message.chat.id, info)
    except:
        bot.send_message(message.chat.id, "Error!")
@bot.message_handler(commands=['scan'])
def scan(message):
    try:
        target=extract_arg(message.text)[0]
        bot.send_message(message.chat.id, "Scanning Started!")
        openedports=scanner.portscan(target)
        info="\n".join(str(port) for port in openedports)
        bot.send_message(message.chat.id, "Opened Ports\n"+info)
    except:
        bot.send_message(message.chat.id, "Error!")
@bot.message_handler(commands=['waf'])
def waf(message):
    try:
        target=extract_arg(message.text)[0]
        if("https" in target):
            firewall=wafmeow.wafsearch(target.replace("https://", ""), "https://")
            bot.send_message(message.chat.id, firewall)
        if("http" in target):
            firewall=wafmeow.wafsearch(target.replace("http://", ""), "http://")
            bot.send_message(message.chat.id, firewall)
        else:
            bot.send_message(message.chat.id, "No scheme is provided, use either http or https!")
    except:
        bot.send_message(message.chat.id, "Error!")
@bot.message_handler(commands=['searchsploit'])
def searchsploit(message):
    try:
        query=" ".join(extract_arg(message.text))
        print(query)
        info=exploitsearch.searchsploit(query)
        for exploit in info:
            bot.send_message(message.chat.id, exploit+": "+info[exploit])
    except:
        bot.send_message(message.chat.id, "Error!")
bot.polling()
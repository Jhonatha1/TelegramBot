import telebot

CHAVE_API = "5444702048:AAG1iN0L-wStAU_ouZ-SrBiv7yashEe_H-8"

bot = telebot.TeleBot(CHAVE_API)



@bot.message_handler(commands=["op1"])
def op1(mensagem):
    print(mensagem)
    bot.send_message(mensagem.chat.id, "Tamo junto! O Yanky mandou um abraço de volta :).")


@bot.message_handler(commands=["op2"])
def op2(mensagem):
    bot.send_message(mensagem.chat.id, """Meus contatos:
    Whatsapp: 37998450590
    E-mail: yankyboa@gmail.com
    GitHub: https://github.com/Jhonatha1
    """)

@bot.message_handler(commands=["op3"])
def op3(mensagem):
    bot.send_location(mensagem.chat.id, latitude= -20.186861, longitude= -44.772278)





def verificar(mensagem):
    return True
@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = """
    Escolha uma opção para continuar:
/op1 Mandar um abraço pro Yanky.
/op2 Saber mais sobre o bot.  
/op3 Saber onde o dono do bot nasceu. 
    """


    bot.reply_to(mensagem, texto)

bot.polling()
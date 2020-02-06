import telebot
import pyowm
owm = pyowm.OWM('e8a0ae0aba933764d3d479a56bb02a1d', language = 'ru')
bot = telebot.TeleBot('846927212:AAHFIfIAECgkKaK_LlOXx8kVDHc1JBLtn1k')
@bot.message_handler(content_types=["text"])
def send_echo(message):
    if message.text == "/start":
        bot.send_message(message.from_user.id,
                         "Здравствуйте. Вы можете узнать здесь погоду. Просто напишите название города." + "\n")
    else:
        try:
            observation = owm.weather_at_place(message.text)
            w = observation.get_weather()
            temp = w.get_temperature('celsius')["temp"]
            answer = "В городе " + message.text + " сейчас: " + "\n"  + w.get_detailed_status() + "\n"
            answer += "Температура " + " сейчас примерно: " + "\n" + str(temp) + " C" + "\n"
            if temp < -10:
                answer += "Очень холодно, лучше посиди дома" + "\n"
            elif temp < 10:
                answer += "Холодно,лучше одеть куртку потеплей " + "\n"
            elif temp > 25:
                answer += "Очень жарко,куртку лучше снять" + "\n"
            else:
                answer += "Погода замечательная " + "\n"
            answer += "Процент влажности:  " + "\n" +  str(w.get_humidity()) + "%" + "\n"
            answer += "Восход солнца примерно: " + "\n" + str(w.get_sunrise_time('iso')) + "\n"
            answer += " Заход солнца примерно:  " + "\n" +  str(w.get_sunset_time('iso')) + "\n"

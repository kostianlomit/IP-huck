
import requests.utils
import folium
from pyfiglet import Figlet
from os_data import token
import requests
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(token=token)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start_message(message):
    await message.reply("Hello!")



@dp.message_handler()
async def main(message: types.Message):

    try:
        response = requests.get(url=f'http://ip-api.com/json/{message}').json()
        # print(response)

        data = {
            '[IP]': response.get('query'),
            '[Org]': response.get('org'),
            '[timezone]': response.get('timezone'),
            '[Country]': response.get('country'),
            '[City]': response.get('city'),
            '[Lat]': response.get('lat'),
            '[Lon]': response.get('lon'),
            }

        for k, v in data.items():
            await message.reply(f'{k} ; {v}')
        area = folium.Map(location=[response.get('lat'), response.get('lon')])
        folium.Marker([response.get('lat'), response.get('lon')]).add_to(area)
        area.save(f'{response.get("query")}_{response.get("city")}.html')
    except requests.exceptions.ConnectionError:
        await message.reply('[!] Please check your connection!')



if __name__ == '__main__':
    # main()
    executor.start_polling(dp)

# def get_info_by_ip(ip='127.0.0.1'):
#     try:
#         response = requests.get(url=f'http://ip-api.com/json/{ip}').json()
#         # print(response)
#
#         data = {
#             '[IP]': response.get('query'),
#             '[Org]': response.get('org'),
#             '[timezone]': response.get('timezone'),
#             '[Country]': response.get('country'),
#             '[City]': response.get('city'),
#             '[Lat]': response.get('lat'),
#             '[Lon]': response.get('lon'),
#
#
#
#         }
#
#         for k, v in data.items():
#             print(f'{k} ; {v}')
#
#         area = folium.Map(location=[response.get('lat'), response.get('lon')])
#         folium.Marker([response.get('lat'), response.get('lon')]).add_to(area)
#         area.save(f'{response.get("query")}_{response.get("city")}.html')
#     except requests.exceptions.ConnectionError:
#         print('[!] Please check your connection!')
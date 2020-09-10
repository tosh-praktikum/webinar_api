import os

import requests
from dotenv import load_dotenv

class TelegramBotClient:
	BOT_KEY = None
	HOST = "https://api.telegram.org"

	def __init__ (self):
		load_dotenv()

		self.BOT_KEY = os.getenv('TG_BOT_KEY')

	def call_method (self, method_name, data):
		url = f"{self.HOST}/bot{self.BOT_KEY}/{method_name}"
		print(f"Calling url {url}...")
		resp = requests.post(url, data = data)

		return resp.json()
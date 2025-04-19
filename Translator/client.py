import requests
from utils.headers import HEADERS
class Translator:
	def __init__(self):
		pass

	def google(self, text, target, source='auto'):
		resp = requests.post('https://api.aitranslator.com/v1/translation/google',
							headers=HEADERS,
							json={
  "text": text,
  "source_language_code": self.detect(text)['data']['language_probability']['code'] if source == 'auto' else source,
  "target_language_code": target,
  "share_id": self._shareId()['share_id']
})
		resp.raise_for_status()
		return resp.json()

	def deepl(self, text, target, source='auto'):
		resp = requests.post('https://api.aitranslator.com/v1/translation/deepl',
							headers=HEADERS,
							json={
  "text": text,
  "source_language_code": self.detect(text)['data']['language_probability']['code'] if source == 'auto' else source,
  "target_language_code": target,
  "share_id": self._shareId()['share_id']
})
		resp.raise_for_status()
		return resp.json()

	def amazon(self, text, target, source='auto'):
		resp = requests.post('https://api.aitranslator.com/v1/translation/amazon',
							headers=HEADERS,
							json={
  "text": text,
  "source_language_code": self.detect(text)['data']['language_probability']['code'] if source == 'auto' else source,
  "target_language_code": target,
  "share_id": self._shareId()['share_id']
})
		resp.raise_for_status()
		return resp.json()

	def modern_mt(self, text, target, source='auto'):
		resp = requests.post('https://api.aitranslator.com/v1/translation/modern-mt',
							headers=HEADERS,
							json={
  "text": text,
  "source_language_code": self.detect(text)['data']['language_probability']['code'] if source == 'auto' else source,
  "target_language_code": target,
  "share_id": self._shareId()['share_id']
})
		resp.raise_for_status()
		return resp.json()

	def libre(self, text, target, source='auto'):
		resp = requests.post('https://api.aitranslator.com/v1/translation/libre',
							headers=HEADERS,
							json={
  "text": text,
  "source_language_code": self.detect(text)['data']['language_probability']['code'] if source == 'auto' else source,
  "target_language_code": target,
  "share_id": self._shareId()['share_id']
})
		resp.raise_for_status()
		return resp.json()

	def detect(self, text):
		resp = requests.post('https://api.aitranslator.com/v1/detect/language',
							headers=HEADERS,
							json={"text": text[:100]})
		resp.raise_for_status()
		return resp.json()

	def _shareId(self):
		resp = requests.post('https://api.aitranslator.com/v1/translation/share-id',
							headers=HEADERS,
							json={"total_words": None})
		resp.raise_for_status()
		return resp.json()
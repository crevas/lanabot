class Config:
	is_debug = False

	activity = "라나가 테스트 중이라고 말"
	
	prefixes = ['l/', '라나야 ']

	version = '1.0'

	admin = [734023826559729734]

	def using_token(self):

  	if self.is_debug:
			return self.test_token
		else:
			return self.token
	
	def prefixes_no_space(self):
		result = []
		for i in self.prefixes:
			result.append(i.replace(' ', ''))
		return result

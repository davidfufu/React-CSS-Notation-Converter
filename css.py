import sublime, sublime_plugin, re, string


def finalizeCapital(match):

	fstWord = match.group(1)
	scndWord = match.group(2)
	CapLetter = match.group(4)
	restOfWrd = match.group(5)
	allothervalues = match.group(7)
	if scndWord:
		print("match2")
		print(match.group(1)+match.group(4).upper()+match.group(5))
		
		return fstWord+CapLetter.upper()+restOfWrd+": " + "\"" + allothervalues + "\","
	else:
		print("match1")
		print(match.group(1))
		return fstWord+": " + "\"" + allothervalues + "\","

class reactcssCommand(sublime_plugin.TextCommand): #create Webify Text Command
	def run(self, edit):   #implement run method
		for region in self.view.sel():  #get user selection
				s = self.view.substr(region)  #assign s variable the selected region
				news = re.sub('([a-z]+)((-)(\w)([a-z]+)?)?:(\s)*(.+);',finalizeCapital,s)
				self.view.replace(edit, region, news) #replace # print ("news = s.replace(case[0], case[1])")

#for css propperties that only have one word as the property name that ned pxs after a number
def reverseCapital(match):
	fstWord = match.group(1)
	scndWord = match.group(2)
	capLetter = match.group(3)
	restOfWrd = match.group(4)
	allothervalues = match.group(7)

	if scndWord:
		initial = fstWord + "-" + capLetter.lower() + restOfWrd
		print('match two words')
		return initial+": " + allothervalues +";"
			
	else:
		initial = fstWord
		print('match one word')
		return initial+": " + allothervalues +";"

class unreactcssCommand(sublime_plugin.TextCommand): #create Webify Text Command
	def run(self, edit):   #implement run method
		for region in self.view.sel():  #get user selection
				s = self.view.substr(region)  #assign s variable the selected region
				news = re.sub('([a-z]+)(([A-Z])([a-z]+)?)?:(\s)*("(.+)")?,',reverseCapital,s)

				self.view.replace(edit, region, news) #replace # print ("news = s.replace(case[0], case[1])")

#random command I created to make making this plugin easier feel free to change it to whatever
class freeuseCommand(sublime_plugin.TextCommand): #create Webify Text Command
	def run(self, edit):   #implement run method
		for region in self.view.sel():  #get user selection
				s = self.view.substr(region)  #assign s variable the selected region
				news = re.sub(r'\"\\\"\"',"+",s)

				self.view.replace(edit, region, news) #replace # print ("news = s.replace(case[0], case[1])")

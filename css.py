import sublime, sublime_plugin, re, string


def finalizeCapital(match):
	if match.group(2):
		print("match2")
		return "\""+match.group(1)+match.group(4).upper()+match.group(5)+"\"" +": "
	else:
		print("match1")
		return "\""+match.group(1)+"\""+": "

class cssCommand(sublime_plugin.TextCommand): #create Webify Text Command
	def run(self, edit):   #implement run method
		for region in self.view.sel():  #get user selection
				s = self.view.substr(region)  #assign s variable the selected region
				print(s)
				print(type(s))
				# news = re.sub("px","",s)
				# news = re.sub(";","",news)
				news = re.sub('(\w+)((-)(?P<capLet>\S){1}(?P<restWord>\w+))?: ',finalizeCapital,s)
				#handle numbers
				news = re.sub('(\d*)(px);', "\""+r"\1"+"\",",news)
				#just kill the px
				news = re.sub('px', '', news)
				#wrap value with quotes
				news = re.sub(':(\s*)?(.+);', ":\""+r'\2'+"\",",news)
				self.view.replace(edit, region, news) #replace # print ("news = s.replace(case[0], case[1])")

#for css propperties that only have one word as the property name that ned pxs after a number
singleNeedPx = ["padding", "margin", "font"]
doubleNeedPx = ['font-size']
def reverseCapital(match):
	if match.group(2):
		fullProperty = match.group(1)+"-"+match.group(3).lower()+match.group(4)
		print(fullProperty)
		if fullProperty in doubleNeedPx:
			return match.group(1)+"-"+match.group(3).lower()+match.group(4)+ ": " +match.group(7)+"px;"
		else:
			return match.group(1)+"-"+match.group(3).lower()+match.group(4)+ ": " +match.group(7)+";"
	else:
		print("match1")
		if match.group(1) in singleNeedPx:
			return match.group(1)+ ": " +match.group(7)+"px;"
		else:
			return match.group(1)+ ": " +match.group(7)+";"
class uncssCommand(sublime_plugin.TextCommand): #create Webify Text Command
	def run(self, edit):   #implement run method
		for region in self.view.sel():  #get user selection
				s = self.view.substr(region)  #assign s variable the selected region
				news = re.sub('"([a-z]+)(([A-Z])?([a-z]+))?":(\s)?"(((.+)(px)?(\s)?))"(,)?',reverseCapital,s)

				self.view.replace(edit, region, news) #replace # print ("news = s.replace(case[0], case[1])")
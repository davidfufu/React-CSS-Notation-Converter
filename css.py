import sublime, sublime_plugin, re, string


def finalizeCapital(match):

	fstWord = match.group(1)
	scndWord = match.group(2)
	CapLetter = match.group(4)
	restOfWrd = match.group(5)
	pixelValue = match.group(9)
	keyWord = match.group(12)
	colorCode = match.group(14)
	if scndWord:
		print("match2")
		if pixelValue and keyWord and colorCode:
			return "\""+fstWord+"\""+": " + "\"" + pixelValue + " "+ keyWord + " " + colorCode + "\""+","
		elif keyWord and not pixelValue and not colorCode:
			return "\""+fstWord+"\""+": " + "\"" + keyWord + "\""+","
		elif pixelValue and not keyWord and not colorCode:
			return "\""+fstWord+CapLetter.upper()+restOfWrd+"\""+": " + "\"" + pixelValue + "\""+","
		elif colorCode and not pixelValue and not keyWord:
			return "\""+fstWord+CapLetter.upper()+restOfWrd+"\""+": " + "\"" + colorCode + "\""+","
	else:
		print("match1")
		if pixelValue and keyWord and colorCode:
			return "\""+fstWord+"\""+": " + "\"" + pixelValue + " "+ keyWord + " " + colorCode + "\"" + ","
		elif keyWord and not pixelValue and not colorCode:
			return "\""+fstWord+"\""+": " + "\"" + keyWord + "\"" + ","
		elif pixelValue and not keyWord and not colorCode:
			return "\""+fstWord+"\""+": " + "\"" + pixelValue + "\"" + ","
		elif colorCode and not pixelValue and not keyWord:
			return "\""+fstWord+"\""+": " + "\"" + colorCode + "\"" + ","

class reactcssCommand(sublime_plugin.TextCommand): #create Webify Text Command
	def run(self, edit):   #implement run method
		for region in self.view.sel():  #get user selection
				s = self.view.substr(region)  #assign s variable the selected region
				news = re.sub('([a-z]+)((-)(\w)([a-z]+)?)?:(\s)*(((\d+)(px))?(\s)*([a-z]+)?(\s)*(#.+)?);',finalizeCapital,s)
				self.view.replace(edit, region, news) #replace # print ("news = s.replace(case[0], case[1])")

#for css propperties that only have one word as the property name that ned pxs after a number
def reverseCapital(match):
	fstWord = match.group(1)
	scndWord = match.group(2)
	capLetter = match.group(3)
	restOfWrd = match.group(4)
	pixelValue = match.group(8)
	keyWord = match.group(10)
	colorCode = match.group(12)

	if scndWord:
		initial = fstWord + "-" + capLetter.lower() + restOfWrd
		print('match two words')
		if pixelValue and keyWord and colorCode:
			return initial+": " + pixelValue + "px" + " "+ keyWord + " " + colorCode +";"
		elif keyWord and not pixelValue and not colorCode:
			return initial+": " + keyWord +";"
		elif pixelValue and not keyWord and not colorCode:
			return initial+": " + pixelValue +"px;"
		elif colorCode and not pixelValue and not keyWord:
			return initial+": " + colorCode +";"
	else:
		initial = fstWord
		print('match one word')
		if pixelValue and keyWord and colorCode:
			return initial+": " + pixelValue + "px" + " "+ keyWord + " " + colorCode +";"
		elif keyWord and not pixelValue and not colorCode:
			return initial+": " + keyWord +";"
		elif pixelValue and not keyWord and not colorCode:
			return initial+": " + pixelValue +"px;"
		elif colorCode and not pixelValue and not keyWord:
			return initial+": " + colorCode +";"

class unreactcssCommand(sublime_plugin.TextCommand): #create Webify Text Command
	def run(self, edit):   #implement run method
		for region in self.view.sel():  #get user selection
				s = self.view.substr(region)  #assign s variable the selected region
				news = re.sub('"([a-z]+)(([A-Z])([a-z]+)?)?":(\s)*"((("?\d+"?))?(\s)*("?[a-z]+"?)?(\s)*(#.+)?"),',reverseCapital,s)

				self.view.replace(edit, region, news) #replace # print ("news = s.replace(case[0], case[1])")

#random command I created to make making this plugin easier feel free to change it to whatever
class freeuseCommand(sublime_plugin.TextCommand): #create Webify Text Command
	def run(self, edit):   #implement run method
		for region in self.view.sel():  #get user selection
				s = self.view.substr(region)  #assign s variable the selected region
				news = re.sub(r'\"\\\"\"',"+",s)

				self.view.replace(edit, region, news) #replace # print ("news = s.replace(case[0], case[1])")

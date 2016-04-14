from mechanize import Browser
from random import choice
import re
import string

"""
[+] Author  : B3mB4m
[~] Contact : b3mb4m@protonmail.com
[~] Greetz  : Bomberman,T-Rex,Pixi
"""


class Shellcode(object):
	"""
	Maybe later we can add some options for it that's why we made it with class.
	"""

	@staticmethod
	def useragent():
		uagent = ['Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.5; en-US; rv:1.9.1b3) Gecko/20090305 Firefox/3.1b3 GTB5',
					'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.5; ko; rv:1.9.1b2) Gecko/20081201 Firefox/3.1b2',
					'Mozilla/5.0 (X11; U; SunOS sun4u; en-US; rv:1.9b5) Gecko/2008032620 Firefox/3.0b5',
					'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.8.1.12) Gecko/20080214 Firefox/2.0.0.12',
					'Mozilla/5.0 (Windows; U; Windows NT 5.1; cs; rv:1.9.0.8) Gecko/2009032609 Firefox/3.0.8',
					'Mozilla/5.0 (X11; U; OpenBSD i386; en-US; rv:1.8.0.5) Gecko/20060819 Firefox/1.5.0.5',
					'Mozilla/5.0 (Windows; U; Windows NT 5.0; es-ES; rv:1.8.0.3) Gecko/20060426 Firefox/1.5.0.3',
					'Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.7.9) Gecko/20050711 Firefox/1.0.5']
		agents = choice(uagent)		
		return agents


	def downloadAll(self):
		url = 'http://0day.today/shellcode/{}' 
		ECX = 0	
		br = Browser()
		br.set_handle_robots(False) 
		br.addheaders = [('User-agent',  self.useragent())]
		try:  	      	
			data = br.open("http://0day.today/webapps")
		except:
			from sys import exit
			exit("Site seems like down.")
	

		for form in br.forms():
		    br.select_form(nr=0)
		    for control in br.form.controls:
		    	if control != None:
			    	if control.name == "agree":
			    		br.submit()		
				
		
			

		for x in range(1,23):
			try:
				page = x
				data = br.open(url.format(x))
				search = re.findall("'/exploit/description/\S+'", data.read())

				if not search: #Empty ..
					print "Exploit Not Found ..";
				else:	
					for i in search:
						cut = i.replace("'", "").replace("/description", "")
						cut = "http://0day.today" + cut
						data = br.open(cut)
						searchtitle = re.search('<title>(.*)</title>', data.read(), re.IGNORECASE).group(1)
						title = searchtitle.replace('&quot;', '')
							
						top = False
						end = False
						logger = ""
						data = br.open(cut)

						for x in data.readlines():
							if "</tr></table><br><pre class=" in x.strip():
								top = True
								continue
							if "#</pre><script type='text/javascript'" in x.strip():
								end = True
								continue

							if top == True:
								if end == False:
									x = x.strip().replace("&lt", "")
									x = x.replace("&gt", "")
									x = x.replace("&quot;", "")
									x = x.replace("&#039;", "")
									x = x.replace("&amp;", "")
									logger += x+"\n"
							
						if logger:
							title = title.replace("/", "+")
							title = "".join([x for x in title if x in string.ascii_letters+string.digits+" "+"-"+"+"+"_"])
							filename = title+".txt"
							with open(filename, "w") as shellcode:
								shellcode.write(logger)
								shellcode.close()
								logger = ""
							ECX += 1
				print "Download Page : {0}".format(page)
			
			except:
				pass

		print "Total shellcode : {0}".format(ECX)



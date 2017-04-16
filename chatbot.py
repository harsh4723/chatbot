from difflib import SequenceMatcher
from newspaper import Article
import newspaper
import sys
import webbrowser
#print mydict.keys()[mydict.values().index(19)]

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def hindu():
	
	print "which language do you prefer,select,language code from below"
	print newspaper.languages()
	print "user>>"
	lang=raw_input()
	print "plz wait.."
	cnn=newspaper.build("http://thehindu.com",language=lang)
	print "user>>"
	print "top news"
	for article in cnn.articles:
		article.download()
		article.parse()
		print article.url
		print "do you want to see the full text here yes/no"
		print "user>>"
		s2=raw_input()
		print "bot>>"
		if(s2=="yes"):
			print article.text
		print "do you want to see the top image of this article yes/no"
		print "user>>"
		sr=raw_input()
		if(sr=="yes"):
			webbrowser.open_new(article.top_image)
	
		print "do you want to open in browser yes/no"
		print "user>>"
		s3=raw_input()
		if(s3=="yes"):
			webbrowser.open_new(article.url)
		print "bot>>"
		print "want to read more yes/no"
		s4=raw_input()
		if(s4!="yes"):
			break
		else:
			print "plz wait.."


def hindustantimes():
	
	print "which language do you prefer,select,language code from below"
	print newspaper.languages()
	print "user>>"
	lang=raw_input()
	print "plz wait.."
	cnn=newspaper.build("http://hindustantimes.com",language=lang)
	print "bot>>"
	print "top news"
	for article in cnn.articles:
		article.download()
		article.parse()
		print article.url
		print "do you want to see the full text here yes/no"
		print "user>>"
		s2=raw_input()
		print "bot>>"
		if(s2=="yes"):
			print article.text
		print "do you want to see the top image of the article yes/no"
		print "user>>"
		sr=raw_input()
		if(sr=="yes"):
			webbrowser.open_new(article.top_image)
	
		print "do you want to open in browser yes/no"
		print "user>>"
		s3=raw_input()
		if(s3=="yes"):
			webbrowser.open_new(article.url)
		print "bot>>"
		print "want to read more yes/no"
		s4=raw_input()
		if(s4!="yes"):
			break
		else:
			print "plz wait.."


def toi():
	
	print "which language do you prefer,select,language code from below"
	print newspaper.languages()
	print "user>>"
	lang=raw_input()
	print "plz wait.."
	cnn=newspaper.build("http://timesofindia.indiatimes.com",language=lang)
	print "top news"
	for article in cnn.articles:
		article.download()
		article.parse()
		print article.url
		print "do you want to see the full text here yes/no"
		print "user>>"
		s2=raw_input()
		print "bot>>"
		if(s2=="yes"):
			print article.text
		print "do you want to see the top image of this article yes/no"
		print "user>>"
		sr=raw_input()
		if(sr=="yes"):
			webbrowser.open_new(article.top_image)
	
		print "do you want to open in browser yes/no"
		print "user>>"
		s3=raw_input()
		if(s3=="yes"):
			webbrowser.open_new(article.url)
		print "bot>>"
		print "want to read more yes/no"
		s4=raw_input()
		if(s4!="yes"):
			break
		else:
			print "plz wait.."

def topimages():
	webbrowser.open_new("http://in.reuters.com/news/pictures")

def sports():
	print "plz wait.."
	cnn=newspaper.build("http://www.hindustantimes.com/sport-news/")
	for article in cnn.articles:
		article.download()
		article.parse()
		print article.url
		'''print "do you want to see the full sports  text here yes/no"
		print "user>>"
		s2=raw_input()
		print "bot>>"
		if(s2=="yes"):
			print article.text
		print "do you want to see the top image of this sports article yes/no"
		print "user>>"
		sr=raw_input()
		if(sr=="yes"):
			webbrowser.open_new(article.top_image)'''
	
		print "do you want to open in browser yes/no"
		print "user>>"
		s3=raw_input()
		if(s3=="yes"):
			webbrowser.open_new(article.url)
		print "bot>>"
		print "want to read more sports yes/no"
		s4=raw_input()
		if(s4!="yes"):
			break
		else:
			print "plz wait.."

def entertainment():
	print "plz wait.."
	cnn=newspaper.build("http://www.hindustantimes.com/entertainment/")
	for article in cnn.articles:
		article.download()
		article.parse()
		print article.url
		'''print "do you want to see the full entertainment  text here yes/no"
		print "user>>"
		s2=raw_input()
		print "bot>>"
		if(s2=="yes"):
			print article.text
		print "do you want to see the top image of this entertainment article yes/no"
		print "user>>"
		sr=raw_input()
		if(sr=="yes"):
			webbrowser.open_new(article.top_image)'''
	
		print "do you want to open in browser yes/no"
		print "user>>"
		s3=raw_input()
		if(s3=="yes"):
			webbrowser.open_new(article.url)
		print "bot>>"
		print "want to read more entertainment news yes/no"
		s4=raw_input()
		if(s4!="yes"):
			break
		else:
			print "plz wait.."

def tech():
	print "plz wait.."
	cnn=newspaper.build("http://www.hindustantimes.com/tech/")
	for article in cnn.articles:
		article.download()
		article.parse()
		print article.url
		'''print "do you want to see the full tech  text here yes/no"
		print "user>>"
		s2=raw_input()
		print "bot>>"
		if(s2=="yes"):
			print article.text
		print "do you want to see the top image of this tech article yes/no"
		print "user>>"
		sr=raw_input()
		if(sr=="yes"):
			webbrowser.open_new(article.top_image)'''
	
		print "do you want to open in browser yes/no"
		print "user>>"
		s3=raw_input()
		if(s3=="yes"):
			webbrowser.open_new(article.url)
		print "bot>>"
		print "want to read more tech yes/no"
		s4=raw_input()
		if(s4!="yes"):
			break
		else:
			print "plz wait.."





dict_cat={"hindu":"news from the hindu","hindustantimes":"news from hindustan times/hindustantimes","toi":"news from timesofindia/timesof india/toi",
			"topimages":"give top images","sports":"give me news from sports","entertainment":"give me news from entertainment","tech":"news from technology","wrongchat":"kuch bhi"}
lkeys=dict_cat.keys()
print "bot>>"
print "hello ,scope of this bot, give news from hindusan times ,toi,the hindu,give top images of the some articles,give news from sports and entertaiment and politics"

while(True):
	print "bot>>"
	print "ask "
	print "user>>"
	s1=raw_input()
	nmax=similar(s1,dict_cat["wrongchat"])
	key=lkeys[-1]
	for x in dict_cat.values():
		if(similar(x,s1)>nmax):
			nmax=similar(x,s1)
			key=dict_cat.keys()[dict_cat.values().index(x)]
	print key

	if(key=="hindu"):
		hindu()
	elif(key=="hindustantimes"):
		hindustantimes()
	elif(key=="toi"):
		toi()
	elif(key=="topimages"):
		topimages()
	elif(key=="sports"):
		sports()
	elif(key=="entertainment"):
		entertainment()
	elif(key=="tech"):
		tech()
	else:
		print "wrong chat for the bot"




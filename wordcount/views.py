from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
	return render(request,'home.html')

def count(request):
	fulltext = request.GET['fulltext']
	worldlist = fulltext.split()
	worddictionary = {} 
	for word in worldlist:
		if word in worddictionary:
			#increase
			worddictionary[word] += 1
		else:
			#add to  the dictionary
			worddictionary[word] = 1

	sortedwords = sorted(worddictionary.items(), key=operator.itemgetter(1),reverse=True)
	return render(request,'count.html',{'fulltext': fulltext,'count':len(worldlist),'sortedwords':sortedwords})

def about(request):
	return render(request,'about.html')
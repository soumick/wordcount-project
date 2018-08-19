from django.http import HttpResponse
from django.shortcuts import render
import operator


def homepage(request):
    return render(request,'home.html')

def Testshow(request):
    return HttpResponse('<h1>Displaying a test page</h1>')

def count(request):
    gettext = request.GET['fulltext']
    wordlist = gettext.split()

    #Counting the words
    worddictionary={}
    for word in wordlist:
        if word in worddictionary:
            worddictionary[word]+=1
        else:
            worddictionary[word]=1

    sortedlist = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse =True)
    return render(request,'count.html',{'gettext':gettext,'wordcount':len(wordlist),'sortedwordlist':sortedlist})

def about(request):
    return render(request,'about.html')

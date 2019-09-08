from django.http import HttpResponse
from django.shortcuts import render
import operator

def hello(request):
    return render(request,"../Project1/template/kani.html",)


def count(request):
        fulltext=request.GET["fulltext"]
        wordlist=fulltext.split()
        worddic={}
        for word in wordlist:
            if word in worddic:
                worddic[word]+=1
            else:
                worddic[word] =1
        sortedpage=sorted(worddic.items(),key=operator.itemgetter(1),reverse=True)
        return render(request,"../Project1/template/count.html",{"fulltext":fulltext,"count":len(wordlist),"sortedpage":sortedpage})
def abot(request):
    return render(request, "../Project1/template/about.html", )



from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.
def homepage(requests):
    return render(requests,'wcount/home.html')
def about(requests):
    return render(requests,'wcount/about.html')
def count(requests):
    fulltext=requests.GET['text']
    word_count=len(fulltext.split())
    word_dict={}
    for w in fulltext.split():
        if w in word_dict:
            word_dict[w]+=1
        else:
            word_dict[w]=1
    word_list=[(list(word_dict.keys())[i],list(word_dict.values())[i]) for i in range(word_count)]
    return render(requests,'wcount/count.html',{'fulltext':fulltext,'word_count':word_count,'word_list':word_list})

from django.shortcuts import render,HttpResponse
# Create your views here.
parent_list = [{'A': 'val1', 'B': 'val2'}, {'C': 'val3', 'D': 'val4'}]
import pandas as pd
from . import dataProcessing as dp
def homepage(request):
    htmlformat=dp.mydata().T.to_dict().values()
    return render(request,"homepage.html",{"data":htmlformat})

def searchfunction(request):
    searchKeyWord=request.GET["keyword"]
    df=dp.searchFunction(searchKeyWord)
    htmlformat=df.T.to_dict().values()
    searchfn=request.GET["year"]

    if(searchfn==""):
        return render(request,"homepage.html",{"data":htmlformat})
    else:
        if(searchKeyWord==" "):
            print(searchKeyWord,"2222222222222222222222222222222")
            htmlformat=dp.findyear(df,searchfn).T.to_dict().values()
            return render(request,"homepage.html",{"data":htmlformat})
        else:   
            htmlformat=dp.findyear(dp.mydata(),searchfn).T.to_dict().values()
            return render(request,"homepage.html",{"data":htmlformat})
           
        

def sortFunction(request):
    searchKeyWord=request.GET["sort"]
    if(searchKeyWord=="low_to_high"):
        return render(request,"homepage.html",{"data":dp.sortAscending().T.to_dict().values()})
    else:
        return render(request,"homepage.html",{"data":dp.sortDescending().T.to_dict().values()})

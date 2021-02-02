import pandas as pd

data=[{"name":"visual studio code","author":"microsoft","version":"10.2","year":2017,"price":0},
{"name":"pycharm","author":"intellij jetbrains",'version':"2020.2",'year':2020,'price':900},
{"name":"eclipse","author":"EclipseSystems",'version':"7",'year':2019,'price':100},
{"name":"finalcut","author":"apple","version":"10",'year':2019,'price':1000},
{"name":"chrome","author":"google","version":"20",'year':2020,'price':0},
{"name":"firefox","author":"FOX","version":"12",'year':2021,'price':20},
{"name":"safari","author":"apple","version":"12",'year':2021,'price':200},
{"name":"primerpro","author":"adobesystems",'version':"30",'year':2020,'price':999},
{"name":"pubg","author":"china","version":"10",'year':2020,'price':1213},
{"name":"gta5","author":"ea games","version":"5",'year':2021,'price':200}
]
print("working in...")
def mydata():
    d=pd.DataFrame(data)
    return d
def searchFunction(keyword):
    print(keyword)
    d=pd.DataFrame(data)
    searchData=d[d["author"]==keyword].sort_values(by=['year'],ascending=True)
    return searchData
def getdataFrame():
    return pd.DataFrame(data)
def sortAscending():
    return pd.DataFrame(data).sort_values(by=['price'])
def sortDescending():
    return pd.DataFrame(data).sort_values(by=['price'],ascending=False)
def findyear(df,year):
    dataout=df[df["year"]==int(year)].sort_values(by=['year'])
    print(dataout)
    return dataout
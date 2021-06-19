from django.shortcuts import render
import joblib



def home(request):
    return render (request,'index.html')


def prediction(request):
    clf=joblib.load('classifier.sav')
    
    list=[]
    list.append((float(request.GET['fa'])-6.839346124715981)/0.8668597405075877)
    list.append((float(request.GET['va'])-0.2805377429941934)/0.10343708697304993)
    list.append((float(request.GET['ca'])-0.33433223933350165)/0.12244609076939264)
    list.append((float(request.GET['rs'])-5.914819490027771)/4.861646307806225)
    list.append((float(request.GET['ch'])-0.045905074476142387)/0.02310271480397696)
    list.append((float(request.GET['fsd'])-34.889169401666244)/17.210020611149623)
    list.append((float(request.GET['tsf'])-137.19351173945972)/43.129065240251904)
    list.append((float(request.GET['d'])-0.9937895304216107)/ 0.0029045957783314803)
    list.append((float(request.GET['ph'])-3.1954582176218125)/0.15154556715055686)
    list.append((float(request.GET['s'])- 0.4903509214844736)/0.11352280532150708)
    list.append((float(request.GET['a'])-10.58935790625263)/1.2170763113068002)

    print(list)

    pred=clf.predict([list])
    
    if pred[0]==1:
        x='poor'
        print('poor')
    else :
        x='good' 
        print ('good')

    good=["good"]
    poor=["poor"]
    
    
    
    return render(request,'prediction.html',{'answer':x,"good":good,"poor":poor})


def index(request):
    return render(request,'Acceuil.html')
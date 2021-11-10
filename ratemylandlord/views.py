from django.shortcuts import render
from django.http import HttpResponse
#becca was here.

#Madaleine Was Here lolzzzzzzzzzzzzz

#can you see this

def indexPageView(request) :
    return render(request, 'ratemylandlord/index.html')

def viewReviewsPageView(request) :
    return HttpResponse('RateMyLandLord: Welcome to the view reviews page')

def editReviewsPageView(request) :
    return HttpResponse('RateMyLandLord: Welcome to the edit reviews page')
    
def aboutPageView(request) :
    return render(request, 'ratemylandlord/about.html')

    #Connor was here
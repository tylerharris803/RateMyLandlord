from django.shortcuts import render
from django.http import HttpResponse
#becca was here

#Madaleine Was Here lolz

#hey

def indexPageView(request) :
    return HttpResponse('This is the RateMyLandlord homepage')

def viewReviewsPageView(request) :
    return HttpResponse('RateMyLandLord: Welcome to the view reviews page')

def editReviewsPageView(request) :
    return HttpResponse('RateMyLandLord: Welcome to the edit reviews page')
    
def contactPageView(request) :
    return HttpResponse('RateMyLandLord: Contact info goes here')

    #Connor was here
from django.shortcuts import render
from django.http import HttpResponse
#becca was here.

#Madaleine Was Here lolzzzzzzzzzzzzz

#can you see this

def indexPageView(request) :
    return render(request, 'ratemylandlord/index.html')

def viewReviewsPageView(request) :
    return render(request, 'ratemylandlord/viewreviews.html')

def editReviewsPageView(request) :
    return render(request, 'ratemylandlord/editreviews.html')
    
def aboutPageView(request) :
    return render(request, 'ratemylandlord/about.html')

    #Connor was here
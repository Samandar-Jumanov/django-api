from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponse, HttpResponseRedirect
from django.urls import reverse
# Create your views here.



month_dummy_data ={
    "january":"Januray data",
    "february":"Febrary data",
    "march":"March data",
    "may":"Nay data",
    "june":None

}



def get_links(request):
  months = list(month_dummy_data.keys())
  return render(request, 'challanges/index.html', {
     'months':months
  })

def month_number(request , month):
    months = list(month_dummy_data.keys())
    response = months[month -1 ]

    if month > len(months [month -1]):
       return HttpResponseNotFound('Cannot find the route ')
    
    redirect = reverse('challanges', args=[response])
     
    return HttpResponse(redirect)


def months(request , month):
   try:
      response = month_dummy_data[month]
      name = month
      return render(request,'challanges/challange.html', {
         "response":f' Task :{response} ', 
         "name":name 
      }) 
   except:
      return HttpResponseNotFound('Cannot find the route ')
 
def get_names(request):
   name = list(month_dummy_data.keys())
   try:
      return render(request, 'challanges/index.html', {
         "name":name 
      })
   except:
    return HttpResponseNotFound('Cannot find ')
   

#what are we doing here basically:
  # THe first functiosn returns a month based on its index like this 
  #I want march which is index of 2 (computer begins from zero)

  #THe fundtion is 

# def demo_func(request , month): #define function 
#     months_demo = len(month_dummy_data.keys()) # get items in the dummy data 
#     text_demo = months_demo[month -1 ] # get the exact item len 
#     if month > len(text_demo): #check if it is valid 
#         return HttpResponseNotFound('Cannot find  the url data 404') #if not send the 404 response 
#     return HttpResponseRedirect(text_demo) # if valid send HttpResponse 

#Get with the word s

# def get_word_demo(request , month):
#     try:
#         text_demo_word = month_dummy_data[month]
#         return HttpResponse(text_demo_word)
#     except:
#         return HttpResponseNotFound('Cannopt find the url')
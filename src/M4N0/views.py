from django.http import HttpResponse
from django.shortcuts import render
from pathlib import Path
from visits.models import PageVisitis

CURRENT_PATH = Path(__file__).resolve().parent














def about_view(request, *args, **kwargs):
   qset = PageVisitis.objects.all()
   page_qset =PageVisitis.objects.filter(path = None)
   try:
        percent  =round( (page_qset.count() *100 ) / qset.count(),2)
   except ZeroDivisionError:
        percent = 0
   my_page =  {
       "page_name": "M4N0",     
       "page_visit_count" : qset.count(), 
       "total_page_visit_count" : page_qset.count(),
       "percent" : percent
   }
   
   if percent >= 50:
        PageVisitis.objects.create(path = request.path)
   elif percent < 50:
       PageVisitis.objects.create(path = None)

   
   return render(request, "home.html", my_page)


def base_page_view(request, *args, **kwargs):
    return render(request,"base.html")
    

def welcome_page_view(request, *args, **kwargs):
    return render(request, "welcome-user-msg.html")
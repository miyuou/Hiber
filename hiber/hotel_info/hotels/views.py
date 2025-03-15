
from django.shortcuts import render
from .models import Hotel

def hotel_list(request):
    hotels = Hotel.objects.all()
    return render(request, 'hotels/hotel_list.html', {'hotels': hotels})




def list_filtre(request):
    return render(request, 'hotels/list_filtre.html', {})
from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets
from .seriallizers import MenuSerializer
from .seriallizers import BookingSerializer
from .models import Menu
from .models import Booking

# Create your views here.
def index(request):
    return render(request, 'index.html', {})


#View for listing or creating  Menu Items:
class MenuItemsView(generics.ListCreateAPIView):
    queryset=Menu.objects.all()
    serializer_class=MenuSerializer

#View for updating,retrieving,or deleting a single menu item:
class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Menu.objects.all()
    serializer_class=MenuSerializer

#View for table booking
class BookingViewSet(viewsets.ModelViewSet):
    queryset= Booking.objects.all()
    serializer_class=BookingSerializer
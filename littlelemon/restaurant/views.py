from django.shortcuts import render
from django.http import response

from rest_framework import generics
from rest_framework import viewsets

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from .seriallizers import MenuSerializer
from .seriallizers import BookingSerializer
from .models import Menu
from .models import Booking

#View with Authentication:
@api_view()
@permission_classes([IsAuthenticated])
def msg(request):
    return response({"message":"This view is protected"})

# Create your views here.
def index(request):
    return render(request, 'index.html', {})


#View for listing or creating  Menu Items:
class MenuItemsView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset=Menu.objects.all()
    serializer_class=MenuSerializer

#View for updating,retrieving,or deleting a single menu item:
class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Menu.objects.all()
    serializer_class=MenuSerializer

#View for table booking
class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset= Booking.objects.all()
    serializer_class=BookingSerializer


from django.shortcuts import render
from PIL import Image  #pip install Pillow
import stepic    #pip install stepic

# Create your views here.
def index(request):
    return render(request,'index.html')

def encryption_view(request):
    return render(request,'encryption.html')

def decryption_view(request):
    return render(request,'decryption.html')
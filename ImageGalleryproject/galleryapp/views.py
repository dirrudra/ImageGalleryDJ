from django.shortcuts import render, redirect
from .forms import ImageUploadForm
from .models import Image
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required



def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('gallery')
    else:
        form = ImageUploadForm()
    return render(request, 'upload_image.html', {'form': form})


# @login_required(login_url='login.html')
def gallery(request):
    images = Image.objects.order_by('-uploaded_at')
    return render(request, 'gallery.html', {'images': images})



def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Log the user in.
            login(request, user)
            return redirect('gallery')  # Redirect to your gallery page
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

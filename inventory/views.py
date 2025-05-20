from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.urls import reverse
import qrcode
from io import BytesIO
from .models import Container, Item
from .forms import ContainerForm
# Create your views here.

def generate_qr(request, container_id):
    url = request.build_absolute_uri(reverse('container_detail', args=[container_id]))
    
    qr = qrcode.make(url)
    buffer = BytesIO()
    qr.save(buffer, format='PNG')
    buffer.seek(0)
    
    return HttpResponse(buffer.getvalue(), content_type='image/png')

# inventory/views.py (add this)


def container_detail(request, container_id):
    container = get_object_or_404(Container, id=container_id)

    # Handle adding an item
    if request.method == "POST":
        if 'add_item' in request.POST:
            item_name = request.POST.get('item_name')
            if item_name:
                Item.objects.create(name=item_name, container=container)
                return redirect('container_detail', container_id=container.id)

        # Handle removing an item
        elif 'remove_item' in request.POST:
            item_id = request.POST.get('item_id')
            Item.objects.filter(id=item_id, container=container).delete()
            return redirect('container_detail', container_id=container.id)

    return render(request, 'container_detail.html', {'container': container})

def create_container(request):
    if request.method == 'POST':
        form = ContainerForm(request.POST)          # Bind data to form
        if form.is_valid():                        # Check that required fields (like name) are present
            container = form.save()               # Save the new Container object
            # Redirect to the detail page of the newly created container
            return redirect('container_detail', container_id=container.pk)
    else:
        form = ContainerForm()  # empty form for GET requests
    
    return render(request, 'create_container.html', {'form': form})


def home(request):
    containers = Container.objects.all() or []  # Ensures an empty list if none found
    return render(request, 'home.html', {'containers': containers})
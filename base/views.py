from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, FormView

from base.forms import RoomForm
from base.models import Room


# Create your views here.
def hello(request):
    s = request.GET.get('s', '')
    return HttpResponse(f'Hello, {s} world!')


def search(request):
    q = request.GET.get('q', '')  # 127.0.0.1/search?q=Dja
    if q == '':
        return HttpResponse("Prosím zadejte hledaný výraz.")
    rooms = Room.objects.filter(
        Q(description__contains=q) |
        Q(name__contains=q)
    )
    context = {'query': q, 'rooms': rooms}
    return render(request, "base/search.html", context)


def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {'room': room}
    return render(request, 'base/room.html', context)


class RoomsView(ListView):
    template_name = 'base/rooms.html'
    model = Room


class RoomCreateView(FormView):
    template_name = 'base/room_form.html'
    form_class = RoomForm
    success_url = reverse_lazy('rooms')

    def form_valid(self, form):
        result = super().form_valid(form)
        cleaned_data = form.cleaned_data
        Room.objects.create(
            name=cleaned_data['name'],
            description=cleaned_data['description'],
        )
        return result

    def form_invalid(self, form):
        return super().form_invalid(form)

# def room_create(request):
#     # request.method == 'POST'
#     if request.method == 'POST':
#         form = RoomForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('rooms')
#     # request.method == 'GET'
#     form = RoomForm()
#     context = {'form': form}
#     return render(request, 'base/room_form.html', context)

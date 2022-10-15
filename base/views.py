from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, FormView, CreateView, UpdateView, DeleteView

from base.forms import RoomForm
from base.models import Room, Message


# Create your views here.
def hello(request):
    s = request.GET.get('s', '')
    return HttpResponse(f'Hello, {s} world!')

@login_required
def search(request):
    q = request.GET.get('q', '')  # 127.0.0.1/search?q=Dja
    if q == '':
        return HttpResponse("Prosím zadejte hledaný výraz.")
    rooms = Room.objects.filter(
        Q(description__contains=q) |
        Q(name__contains=q)
    )
    context = {'query': q, 'rooms': rooms, 'pokus': "testing\r\njavascript 'string\" <b>escaping</b>"}
    return render(request, "base/search.html", context)

@login_required
def room(request, pk):
    room = Room.objects.get(id=pk)
    messages = room.message_set.all()

    # POST
    if request.method == 'POST':
        Message.objects.create(
            user=request.user,
            room=room,
            body=request.POST.get('body')
        )
        room.participants.add(request.user)
        return redirect('room', pk=room.id)

    # GET
    context = {'room': room, 'messages': messages}
    return render(request, 'base/room.html', context)


class RoomsView(LoginRequiredMixin, ListView):
    template_name = 'base/rooms.html'
    model = Room


class RoomCreateView(LoginRequiredMixin, CreateView):
    template_name = 'base/room_form.html'
    form_class = RoomForm
    success_url = reverse_lazy('rooms')

    def form_invalid(self, form):
        return super().form_invalid(form)


class RoomUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'base/room_form.html'
    model = Room
    form_class = RoomForm
    success_url = reverse_lazy('rooms')

    def form_invalid(self, form):
        return super().form_invalid(form)


class RoomDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'base/room_confirm_delete.html'
    model = Room
    success_url = reverse_lazy('rooms')

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

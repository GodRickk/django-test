from django.shortcuts import render
from django.shortcuts import render, redirect
import random
from channels.layers import get_channel_layer
import asyncio
from django.contrib.auth import logout
from django.views.generic import FormView


async def index(request):
    import pdb; pdb.set_trace()
    return render(request, 'index.html')


async def random_number_app(request):
    return render(request, 'random_numbers.html')
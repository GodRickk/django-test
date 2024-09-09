from django.shortcuts import render
from django.shortcuts import render, redirect
import random
from channels.layers import get_channel_layer
import asyncio
from django.contrib.auth import logout




async def index(request):
    return render(request, 'index.html')

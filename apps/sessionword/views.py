# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, HttpResponse
from django.utils import timezone

def index(request):
    return render(request, 'sessionword/index.html')

def add_word(request):
    if request.method == "POST":
        if 'words' not in request.session:
            request.session['words'] = []

        word = request.POST['word']
        color = request.POST['color']
        if 'big_font' in request.POST:
            font_size = "2rem"
        else:
            font_size = "1rem"
        time = timezone.now().strftime('%-I:%M:%S%p, %B %d %Y')

        word_data = {
            'word': word,
            'color': color,
            'font_size': font_size,
            'time': time
        }
        request.session['words'].insert(0, word_data)
        request.session.modified = True
        return redirect('/session_words')
    else:
        return redirect('/session_words')

def clear(request):
    if request.method == "POST":
        request.session['words'] = []
        return redirect('/session_words')
    else:
        return redirect('/session_words')
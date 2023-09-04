from django.shortcuts import render, HttpResponse, redirect
from django.core.paginator import Paginator
from app.models import Data

# Create your views here.

def index(request):

    data = Data.objects.all()
    paginator = Paginator(data, 5) 
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)

    chart_labels = [entry.date for entry in data]
    chart_closes = [entry.close for entry in data]

    # Prepare the chart data as a dictionary
    chart_data = {
        'labels': chart_labels,
        'closes': chart_closes,
    }

    return render(request, 'index.html', {'page': page, 'chart_data': chart_data})


def add(request):
    if request.method == "POST":
        date = request.POST.get('date')
        trade_code = request.POST.get('trade_code')
        high = request.POST.get('high')
        low = request.POST.get('low')
        open = request.POST.get('open')
        close = request.POST.get('close')
        volume = request.POST.get('volume')

        data = Data(
            date = date,
            trade_code = trade_code,
            high = high,
            low = low,
            open = open,
            close = close,
            volume = volume
        )  

        data.save()
        return redirect('home')

def edit(request):

    data = Data.objects.all()
    context = {
        'data': data,
    }

    return redirect(request, 'index.html', context)

def delete(request, id):
    data = Data.objects.get(pk=id)
    data.delete()

    return redirect('home')

def update(request, id):
    data = Data.objects.get(pk=id)

    return render(request, 'update.html', {'data': data})

def doupdate(request, id):

    if request.method == "POST":
        date = request.POST.get('date')
        trade_code = request.POST.get('trade_code')
        high = request.POST.get('high')
        low = request.POST.get('low')
        open = request.POST.get('open')
        close = request.POST.get('close')
        volume = request.POST.get('volume')

        data = Data.objects.get(pk=id)

        data.date = date
        data.trade_code = trade_code
        data.high = high
        data.low = low
        data.open = open
        data.close = close
        data.volume = volume

        data.save()

        return redirect("home")

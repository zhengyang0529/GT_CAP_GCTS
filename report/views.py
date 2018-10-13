from django.shortcuts import render, HttpResponse, redirect

from .forms import CellReportForm


def home(request):
    if request.method == 'POST':
        form = CellReportForm(request.POST, request.FILES or None)
        if form.is_valid():
            form.save()
            # return redirect('home')
    else:
        form = CellReportForm()
    return render(request, 'report/home.html', {
        'form': form
    })

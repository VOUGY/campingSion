from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import BookForm


def book(request, location_id=None):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = BookForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            form.save(location_id=location_id)

            return HttpResponseRedirect('/thanks')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = BookForm()

    return render(request, 'book.html', {'form': form, 'location_id': location_id})


def thanks(request):
    return render(request, 'thanks.html')

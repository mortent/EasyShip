from django.shortcuts import render
from root.models import ServiceLevel, Zone, Rate
from root.forms import SearchForm

def search(request):
    """
    Uses the submit parameter from the submit button in the page to distinquiush between a new request and a
    search request. Since it is a search function with no state change to the application we use GET rather than POST.
    """
    rate = None
    is_submit = request.GET.has_key('submit')
    if is_submit:
        form = SearchForm(request.GET)
        if form.is_valid():
            rate = find_rate(form)
    else:
        form = SearchForm()

    return render(request, 'search.html', {'form': form, 'show_result': is_submit,
                                           'rate': rate})


def find_rate(form):
    """
    Looks up a rate from the database by first finding the correct zone with the find_zone method.
    """
    zone = find_zone(form)
    if zone is None:
        return None
    rate_query_set = Rate.objects.filter(weight=form.cleaned_data['weight'], service_level=zone.service_level,
        zone_number=zone.zone_number)
    if not rate_query_set:
        return None
    return rate_query_set[0]


def find_zone(form):
    """
    Look up a zone from the database. There can only be 0 or 1 rows in the result set.
    """
    zone_query_set = Zone.objects.filter(service_level=form.cleaned_data['service_level'],
        zip_code=form.cleaned_data['zip_code'][:3])
    if not zone_query_set:
        return None
    return zone_query_set[0]
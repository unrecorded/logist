from django.shortcuts import render
from geo.models import Geo
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from geo.forms import ContactForm
from django.core.paginator import Paginator
from django.db.models import Sum

# Create your views here.
def GeoList(request):
    template_name = 'index.html',

    geo_list = Geo.objects.all()
    paginator = Paginator(geo_list, 15)

    dolg_sum = Geo.objects.filter(paid_driver=2)
    dolg_summ = dolg_sum.aggregate(Sum('price_dilevery')) #Сумма неоплаченных рейсов

    rashod_filter = Geo.objects.filter(paid_driver=2)
    rashod = rashod_filter.aggregate(Sum('cost_dilevery')) #Сумма расходов неоплаченных рейсов

    page_number = request.GET.get('page')
    page_list = paginator.get_page(page_number)

    return render(request, template_name, {'geo': page_list, 'dolg_sum':dolg_summ, 'rashod': rashod,})

def GeoFull(request):
    template_name = 'table.html',

    geo_list = Geo.objects.all()
    paginator = Paginator(geo_list, 15)

    page_number = request.GET.get('page')
    page_list = paginator.get_page(page_number)

    return render(request, template_name, {'geo': page_list,})

def GeoDetails(request, id):
    template_name = 'detail.html'

    geo_details = get_object_or_404(Geo, id=id)

    return render(request, template_name, {'geo_detail': geo_details,})

def GeoCreate(request):
    template_name = 'create.html'

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/') 
        else:
            return HttpResponseRedirect(request.user) 
    form = ContactForm()

    return render(request, template_name,{'form': form})

def GeoEdit(request, id):
    template_name='edit.html'

    contact = get_object_or_404(Geo, id=id)
    form = ContactForm(request.POST or None, instance=contact)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path) 
        else:
            return HttpResponse(status=400)   

    return render(request, template_name, {'form':form})
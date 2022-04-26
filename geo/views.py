from django.shortcuts import render
from geo.models import Geo
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from geo.forms import ContactForm
from django.core.paginator import Paginator
from django.db.models import Sum
from django.contrib.auth.views import LoginView
from geo.forms import LoginForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
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

@login_required
def GeoFull(request):
    template_name = 'table.html',

    geo_list = Geo.objects.all()
    paginator = Paginator(geo_list, 15)

    page_number = request.GET.get('page')
    page_list = paginator.get_page(page_number)

    return render(request, template_name, {'geo': page_list,})

@login_required
def GeoDetails(request, id):
    template_name = 'detail.html'

    geo_details = get_object_or_404(Geo, id=id)

    return render(request, template_name, {'geo_detail': geo_details,})

@login_required
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

@login_required
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

# Авторизация
class CustomLoginView(LoginView):
    form_class = LoginForm

    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')

        if not remember_me:
            # если юзер сказал не запоминать себя, то пошел он нахер после закрытия браузера
            self.request.session.set_expiry(0)

            # объявляем сессию с измененнными кукисами
            self.request.session.modified = True

        # если юзер сказал помнить себя то держим значение кукисов на основе настроек
        return super(CustomLoginView, self).form_valid(form)
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import NameForm, FormView
from django.views.generic import TemplateView
# Create your views here.
class Index(TemplateView):
    template_name = 'contact/index.html'
    # if request.method == 'POST':
    #     form = NameForm(request.POST)
    #     if form.is_valid():
    #         print ("Form Valid")
    #         myName = form.cleaned_data['yourName']
    #         return render(request, 'contact/index.html', {'val':request.POST['yourName']})
    #
    #     print ("Form InValid")
    #     return render(request, 'contact/index.html', {'val':request.POST['yourName']})
    # else:
    #     return render(request, 'contact/index.html', {'val':'notget'})

def indexforms(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            myName = form.cleaned_data['yourName']
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return render(request, 'contact/index.html', {'val': myName, 'form': form})
    else:
        form = NameForm()

    return render(request, 'contact/index.html', {'form': form})


class ContactForm(TemplateView):
    template_name = 'contact/formview.html'


    def get(self, request):
        form1 = FormView()
        return render(request, self.template_name, {'form': form1})

    def post(self, request):
        print (request.FILES)
        form1 = FormView(request.POST, request.FILES)
        if form1.is_valid():
            username = form1.cleaned_data['username']
            print ("Success validation")
            form1.save()
            return render(request, self.template_name, {'form': form1, 'error': username })
        else :
            print ("Failed validation")

        return render(request, self.template_name, {'form': form1})

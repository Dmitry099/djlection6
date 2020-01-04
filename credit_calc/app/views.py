from django.shortcuts import render

from .forms import CalcForm


def calc_view(request):
    template = "app/calc.html"

    form = CalcForm

    if request.method == 'GET':
        form = CalcForm(request.GET)
        if form.is_valid():
            initial_fee, rate, months_count = form.cleaned_data['initial_fee'], \
                                               form.cleaned_data['rate'], \
                                               form.cleaned_data['months_count']

            common_result = initial_fee + initial_fee * (rate / 100)
            result = common_result / months_count
            context = {
                'form': form,
                'common_result': common_result,
                'result': result
            }
            return render(request, template, context)

    context = {
        'form': form
        }

    return render(request, template, context)

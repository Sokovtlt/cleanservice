from django.views.generic import DetailView, CreateView
from django.urls import reverse, reverse_lazy
from .models import *
from .forms import OrderForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


class OrderView(CreateView):
    """Main page where creating an order"""
    model = Order
    template_name = 'index_page.html'
    form_class = OrderForm
    success_url = reverse_lazy('index_page')

    def get_success_url(self):
        # route to order page
        return reverse('order_page', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        clothes_list = Cloth.objects.all()
        # show all items if they exist
        if len(clothes_list) != 0:
            kwargs['clothes_list'] = clothes_list
        else:
            kwargs['clothes_list'] = False
        kwargs['category'] = Category.objects.all()
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        calc_number = self.object.calculation
        calculation = Calculation.objects.get(pk=calc_number)
        list_clothes = calculation.data['items']
        order_text = ''
        for item in list_clothes:
            order_text += str(item['number']) + ' x ' + item['name'] + ' - ' + str(item['cost']) + ' Euro' + '<br>'
        self.object.order_list = order_text
        self.object.save()
        return super().form_valid(form)


class DetailOrderView(DetailView):
    """Order info"""
    model = Order
    template_name = 'order_page.html'
    context_object_name = 'get_order'


@csrf_exempt
def process_cloth_data(request):
    if request.method == 'POST':
        try:
            # We receive data from the request
            data = json.loads(request.body)
            if len(data) != 0:
                calculation = []
                all_cost = 0
                for item in data:
                    cloth_id = item['id']
                    quantity = item['quantity']
                    # Logic for processing each product
                    cloth = Cloth.objects.get(pk=cloth_id)
                    cost = int(cloth.price) * int(quantity)
                    all_cost += cost
                    # creating json and saving in the database
                    calculation.append({
                        'id': cloth.id,
                        'name': cloth.name,
                        'number': quantity,
                        'cost': cost,
                        'image': cloth.img.url,
                    })
                last_calculation = Calculation.objects.order_by('id').last()
                if last_calculation:
                    last_id = last_calculation.id + 1
                else:
                    last_id = 1
                data_json = {"items": calculation, "order_cost": all_cost, "calculation": last_id}
                new_calculation = Calculation(data=data_json)
                new_calculation.save()
                # We return the successful answer
                return JsonResponse(data_json, safe=False)
        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON'}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)

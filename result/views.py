from django.shortcuts import render

# Create your views here.


from django.http import JsonResponse
import json

from django.views.decorators.csrf import csrf_exempt

from .models import Result

@csrf_exempt
def save_result(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        username = data.get('username')
        category = data.get('category')
        seconds = data.get('seconds')

        if username and category is not None and seconds is not None:
            result = Result(user=username, category=category, seconds=seconds)
            result.save()
            return JsonResponse({'message': 'Rezultat je spremljen.'})
        else:
            return JsonResponse({'error': 'Nedostaju podaci.'}, status=400)

    return JsonResponse({'error': 'Metoda nije podržana.'}, status=405)


def get_all_result(request, category):
    if category not in ['16', '32']:
        return JsonResponse({'error': 'Neispravna kategorija.'}, status=400)

    results = Result.objects.filter(category=category).order_by('seconds')  # Sortiranje po broju sekundi
    results_data = [{'username': result.user, 'seconds': result.seconds} for result in results]

    return JsonResponse({'results': results_data})
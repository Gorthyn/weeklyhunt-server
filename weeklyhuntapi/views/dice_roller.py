import random
from django.http import JsonResponse
from weeklyhuntapi.models import DiceRoll

def roll_2d6(request):
    modifier = int(request.GET.get('modifier', 0))  # Optional modifier
    result_1 = random.randint(1, 6)
    result_2 = random.randint(1, 6)
    total = result_1 + result_2 + modifier
    
    # Save the result to the database
    DiceRoll.objects.create(result_1=result_1, result_2=result_2, modifier=modifier, total=total, roll_type='2d6')
    
    return JsonResponse({
        'result_1': result_1,
        'result_2': result_2,
        'modifier': modifier,
        'total': total
    })

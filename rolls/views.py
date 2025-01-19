from django.shortcuts import render, redirect
from .models import Roll, Contact, CartItem, Order
from django.http import JsonResponse

# Vista per la home page
def home(request):
    rolls = Roll.objects.all()
    return render(request, 'rolls/index.html', {'rolls': rolls})

def home(request):
    return render(request, 'rolls/index.html', {'request': request})

# Vista per la pagina del menu
def menu(request):
    rolls = Roll.objects.all()
    return render(request, 'rolls/Menu.html', {'rolls': rolls})

# Aggiungi al carrello
def aggiungi_al_carrello(request, roll_id):
    roll = Roll.objects.get(id=roll_id)
    quantita = int(request.POST.get("quantita", 1))
    
    # Gestione del carrello nella sessione
    carrello = request.session.get('carrello', {})
    if str(roll_id) in carrello:
        carrello[str(roll_id)] += quantita
    else:
        carrello[str(roll_id)] = quantita
    request.session['carrello'] = carrello

    # Calcola il totale degli articoli nel carrello
    cart_count = sum(carrello.values())

    return JsonResponse({'cart_count': cart_count})

# Mostra il carrello
def carrello(request):
    carrello = request.session.get('carrello', {})
    cart_items = []
    totale = 0

    for roll_id, quantita in carrello.items():
        roll = Roll.objects.get(id=roll_id)
        cart_items.append({'roll': roll, 'quantita': quantita, 'totale': roll.prezzo * quantita})
        totale += roll.prezzo * quantita

    return render(request, 'rolls/carrello.html', {'cart_items': cart_items, 'totale': totale})

def rimuovi_dal_carrello(request, roll_id):
    carrello = request.session.get('carrello', {})
    if str(roll_id) in carrello:
        del carrello[str(roll_id)]
    request.session['carrello'] = carrello
    return redirect('carrello')


# Conferma ordine
def conferma_ordine(request):
    carrello = request.session.get('carrello', {})
    totale = 0
    ordine = Order.objects.create(totale=0)

    for roll_id, quantita in carrello.items():
        roll = Roll.objects.get(id=roll_id)
        totale += roll.prezzo * quantita
        cart_item = CartItem.objects.create(roll=roll, quantita=quantita)
        ordine.items.add(cart_item)

    ordine.totale = totale
    ordine.save()

    # Svuota il carrello dopo la conferma
    request.session['carrello'] = {}

    return render(request, 'rolls/conferma_ordine.html', {'ordine': ordine})

# Vista per la pagina contattaci
def contact(request):
    if request.method == "POST":
        nome = request.POST.get("nome")
        cognome = request.POST.get("cognome", "")
        email = request.POST.get("email")
        telefono = request.POST.get("telefono", "")
        messaggio = request.POST.get("messaggio")
        Contact.objects.create(
            nome=nome,
            cognome=cognome,
            email=email,
            telefono=telefono,
            messaggio=messaggio
        )
        return redirect("successo_contatto")
    return render(request, "rolls/contattaci.html")

# Vista per il successo del contatto
def successo_contatto(request):
    return render(request, 'rolls/Successo Contatto.html')
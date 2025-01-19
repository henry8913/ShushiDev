from django.db import models

class Roll(models.Model):
    immagine = models.ImageField()
    nome = models.CharField(max_length=20)
    prezzo = models.FloatField()
    descrizione = models.TextField(default="Descrizione non disponibile")

    def __str__(self):
        return self.nome

class Contact(models.Model):
    nome = models.CharField(max_length=100)
    cognome = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField()
    telefono = models.CharField(max_length=20, blank=True, null=True)
    messaggio = models.TextField()
    data_invio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome} {self.cognome} ({self.email})"

class CartItem(models.Model):
    roll = models.ForeignKey(Roll, on_delete=models.CASCADE)
    quantita = models.PositiveIntegerField(default=1)

    def totale(self):
        return self.roll.prezzo * self.quantita

    def __str__(self):
        return f"{self.quantita} x {self.roll.nome}"

class Order(models.Model):
    items = models.ManyToManyField(CartItem)
    totale = models.FloatField()
    data_creazione = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Ordine #{self.id} - Totale: €{self.totale}"
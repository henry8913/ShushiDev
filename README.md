<h1 align="center">
    <img src="https://readme-typing-svg.herokuapp.com/?font=Iosevka&size=30&color=FFA500&center=true&vCenter=true&width=800&height=60&lines=SushiDev+-+Il+Progetto+di+Sushi+in+Django+🍣&repeat=false" alt="SushiDev - Il Progetto di Sushi in Django">
</h1>

Benvenuto in **SushiDev**, un progetto sviluppato in Django che simula un sito web per ordinare sushi. Questo progetto include una pagina del menu, un carrello per gestire gli ordini, e un sistema per gestire file statici e multimediali.

<p align="center">
    <img src="https://github.com/henry8913/ShushiDev/blob/main/rolls/static/rolls/cover.jpg" alt="Cover" width="100%" />
</p>

## **Funzionalità Principali**

- **Menu**: Visualizza un elenco di prodotti (roll) con immagini, descrizioni e prezzi.
- **Carrello**: Aggiungi prodotti al carrello e gestiscili.
- **Ordini**: Conferma l'ordine e visualizza il totale da pagare.
- **Contattaci**: Una pagina per inviare messaggi di contatto.

---

## **Come Testare il Progetto in Locale**

Segui questi semplici passaggi per avviare il progetto in locale:

### **1. Pre-requisiti**
Assicurati di avere installato:
- **Python 3.8+**: Puoi scaricarlo da [python.org](https://www.python.org/downloads/).
- **pip**: Normalmente incluso con Python.
- **Git**: Per clonare il repository.

### **2. Clona il Repository**
Clona il repository GitHub nella tua macchina locale:
```bash
git clone <URL_DEL_REPOSITORY>
cd ShushiDev
```

### **3. Avvia il Server di Sviluppo**
Apri la cartella clonata in Visual Studio Code o un altro editor, quindi esegui:
```bash
python3 manage.py runserver
```
Visita il sito su [http://127.0.0.1:8000](http://127.0.0.1:8000). Questo indirizzo funziona solo sulla tua macchina locale.

### **4. Accesso all'Amministrazione**
Se vuoi accedere alla parte di amministrazione di Django:
1. Crea un superutente (se non lo hai già fatto):
   ```bash
   python3 manage.py createsuperuser
   ```
2. Segui le istruzioni per impostare username, email e password.
3. Visita [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin) per accedere al pannello di amministrazione.

---

## **Struttura del Progetto**

```
SushiDev/
├── SushiDev/                  # Configurazione principale di Django
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── rolls/                     # App principale
│   ├── models.py              # Modelli dei dati
│   ├── views.py               # Viste dell'app
│   ├── templates/             # Template HTML
│   └── static/                # File statici
├── manage.py                  # Script per gestire Django
├── requirements.txt           # Dipendenze del progetto
└── db.sqlite3                 # Database SQLite (opzionale)
```

---

## **Contribuire al Progetto**
Siamo aperti a contributi! Se hai idee, miglioramenti o vuoi aggiungere nuove funzionalità, sentiti libero di fare un fork del progetto e inviare una pull request.

Grazie per aver provato **SushiDev**! 🍣




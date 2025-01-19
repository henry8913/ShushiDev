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

## **Come Scaricare e Usare il Progetto**

Segui questi passaggi per scaricare e avviare il progetto in locale:

### **1. Clona il Repository**
Clona il repository GitHub nella tua macchina locale:
```bash
git clone <URL_DEL_REPOSITORY>
cd ShushiDev
```

### **2. Crea un Ambiente Virtuale**
Crea e attiva un ambiente virtuale per gestire le dipendenze:
```bash
python3 -m venv env
source env/bin/activate  # Su macOS/Linux
env\Scripts\activate   # Su Windows
```

### **3. Installa le Dipendenze**
Installa tutte le dipendenze necessarie:
```bash
pip install -r requirements.txt
```

### **4. Configura il File `.env`**
Crea un file `.env` nella root del progetto con le seguenti variabili di ambiente:
```env
SECRET_KEY=la-tua-chiave-segreta
DEBUG=True
ALLOWED_HOSTS=*
```

### **5. Esegui le Migrazioni**
Applica le migrazioni al database:
```bash
python manage.py migrate
```

### **6. Carica i File Statici**
Raccogli i file statici:
```bash
python manage.py collectstatic
```

### **7. Avvia il Server**
Avvia il server di sviluppo:
```bash
python manage.py runserver
```
Visita il sito su `http://127.0.0.1:8000`.

---

## **Prova il Progetto su Vercel**
Se preferisci, puoi vedere una versione live del progetto su Vercel. Visita il seguente URL:
```
<URL_DEL_PROGETTO_SU_VERCEL>
```

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



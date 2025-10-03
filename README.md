# 📋 Gestore Task (To-Do List Avanzato)

Un'applicazione web completa per la gestione dei task, sviluppata con Django e MySQL.

![Python](https://img.shields.io/badge/Python-3.13-blue)
![Django](https://img.shields.io/badge/Django-5.2-green)
![MySQL](https://img.shields.io/badge/MySQL-8.0-orange)

## 📸 Screenshot



## ✨ Funzionalità

- ✅ **CRUD Completo**: Crea, leggi, modifica ed elimina task
- 🔐 **Sistema di Autenticazione**: Registrazione, login e logout utenti
- 📊 **Dashboard Analitica**: Statistiche e visualizzazione dati
- 🎯 **Priorità**: Alta, Media, Bassa con codifica colori
- 📅 **Date di Scadenza**: Con notifica visiva per task scaduti
- 🏷️ **Categorie**: Organizza i task per categoria
- 👥 **Assegnazione Utenti**: Assegna task a utenti specifici
- 🔍 **Filtri Avanzati**: Filtra per stato, priorità e assegnazione
- 📈 **Statistiche**: Contatori in tempo reale e analisi

## 🛠️ Tecnologie Utilizzate

- **Backend**: Django 5.2
- **Database**: MySQL (via XAMPP)
- **Frontend**: HTML5, CSS3 (Vanilla)
- **ORM**: Django ORM
- **Autenticazione**: Django Auth System

## 📋 Prerequisiti

- **Python 3.8+**
- **MySQL Server (XAMPP consigliato)**
- **pip (gestore pacchetti Python)**

___

## Installazione

### 1. Clona il repository

```bash
git clone https://github.com/TUO-USERNAME/gestore-task.git
cd gestore-task
```

### 2. Crea e attiva l'ambiente virtuale
Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

Mac/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```
###  3. Installa le dipendenze

```bash
pip install -r requirements.txt
```
### 4. Configura il Database
1. Avvia XAMPP e il servizio MySQL
2. Crea un database chiamato todo_db in phpMyAdmin
3. Modifica todolist/settings.py con le tue credenziali MySQL (se diverse):

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'todo_db',
        'USER': 'root',
        'PASSWORD': '',  # Inserisci la tua password se necessario
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

### 5. Esegui le migrazioni
```bash
python manage.py makemigrations
python manage.py migrate
```
### 6. Crea un superutente
```bash
python manage.py createsuperuser
```
### 7. Avvia il server
```bash
python manage.py runserver

Apri il browser su: http://127.0.0.1:8000
```
---

## 📱 Utilizzo
1. **Registrati** o effettua il **login**
2. Crea il tuo primo task cliccando su "➕ Nuovo Task"
3. Visualizza la **Dashboard** per statistiche e analisi
4. Usa i **filtri** nella Home per organizzare i task
5. Segna i task come completati o modificali


## 🗂️ Struttura del Progetto

```bash
gestore-task/
│
├── todolist/              # Configurazione progetto Django
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── tasks/                 # App principale
│   ├── models.py         # Modello Task
│   ├── views.py          # Logica applicazione
│   ├── forms.py          # Form Django
│   ├── urls.py           # URL routing
│   ├── admin.py          # Configurazione admin
│   └── templates/        # Template HTML
│       └── tasks/
│
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md
```
---

## 🎓 Competenze Dimostrate

- **Django ORM**: Modelli, query, relazioni ForeignKey
- **Views**: Function-based views, CRUD operations
- **Templates**: Template inheritance, tags, filters
- **Forms**: ModelForm, validazione, widgets
- **Autenticazione**: User registration, login/logout
- **Database**: MySQL integration, migrations
- **Security**: CSRF protection, password hashing

## 📝 MIT License

Questo progetto è stato creato per scopi educativi
Copyright (c) 2025 Alessandro Bagnuoli

## 👤 Autore
Alessandro Bagnuoli

- **GitHub**: @Axel0689
- **Linktree**: https://linktr.ee/alexbagnuoli

## 🙏 Ringraziamenti
Progetto sviluppato come parte del portfolio per dimostrare competenze in Django e sviluppo web.

---

⭐ Se questo progetto ti è stato utile, lascia una stella su GitHub!
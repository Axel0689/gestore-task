from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Task
from .forms import TaskForm
from django.contrib import messages
from django.db.models import Count
from datetime import timedelta


def task_list(request):
    """Vista per mostrare tutti i task"""
    tasks = Task.objects.all()
    
    # Filtri opzionali
    filter_status = request.GET.get('status', 'all')
    filter_priority = request.GET.get('priority', 'all')
    filter_user = request.GET.get('user', 'all')
    
    if filter_status == 'completed':
        tasks = tasks.filter(completed=True)
    elif filter_status == 'pending':
        tasks = tasks.filter(completed=False)
    
    if filter_priority != 'all':
        tasks = tasks.filter(priority=filter_priority)
    
    if filter_user != 'all':
        if filter_user == 'me' and request.user.is_authenticated:
            tasks = tasks.filter(assigned_to=request.user)
        elif filter_user == 'unassigned':
            tasks = tasks.filter(assigned_to__isnull=True)
    
    # Statistiche
    total_tasks = Task.objects.count()
    completed_tasks = Task.objects.filter(completed=True).count()
    pending_tasks = Task.objects.filter(completed=False).count()
    overdue_tasks = Task.objects.filter(
        completed=False, 
        due_date__lt=timezone.now()
    ).count()
    
    context = {
        'tasks': tasks,
        'filter_status': filter_status,
        'filter_priority': filter_priority,
        'filter_user': filter_user,
        'total_tasks': total_tasks,
        'completed_tasks': completed_tasks,
        'pending_tasks': pending_tasks,
        'overdue_tasks': overdue_tasks,
    }
    return render(request, 'tasks/task_list.html', context)


def task_detail(request, pk):
    """Vista per mostrare i dettagli di un task"""
    task = get_object_or_404(Task, pk=pk)
    context = {
        "task": task,
    }
    return render(request, "tasks/task_detail.html", context)


@login_required
def task_toggle_complete(request, pk):
    """Vista per completare/scompletare un task"""
    task = get_object_or_404(Task, pk=pk)
    task.completed = not task.completed
    task.save()
    return redirect("task_list")


# Nuove funzioni per creare, modificare ed eliminare task


@login_required
def task_create(request):
    """Vista per creare un nuovo task"""
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            # Se non è assegnato a nessuno, assegna all'utente corrente
            if not task.assigned_to:
                task.assigned_to = request.user
            task.save()
            messages.success(request, "Task creato con successo!")
            return redirect("task_list")
    else:
        form = TaskForm()

    context = {"form": form, "action": "Crea"}
    return render(request, "tasks/task_form.html", context)


@login_required
def task_update(request, pk):
    """Vista per modificare un task esistente"""
    task = get_object_or_404(Task, pk=pk)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, "Task modificato con successo!")
            return redirect("task_detail", pk=task.pk)
    else:
        form = TaskForm(instance=task)

    context = {"form": form, "task": task, "action": "Modifica"}
    return render(request, "tasks/task_form.html", context)


@login_required
def task_delete(request, pk):
    """Vista per eliminare un task"""
    task = get_object_or_404(Task, pk=pk)

    if request.method == "POST":
        task.delete()
        messages.success(request, "Task eliminato con successo!")
        return redirect("task_list")

    context = {"task": task}
    return render(request, "tasks/task_confirm_delete.html", context)


from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User

# Funzioni per la registrazione, login e logout

def register_view(request):
    """Vista per la registrazione di nuovi utenti"""
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        # Validazioni
        if password1 != password2:
            messages.error(request, "Le password non corrispondono!")
            return redirect("register")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username già esistente!")
            return redirect("register")

        # Crea l'utente
        user = User.objects.create_user(
            username=username, email=email, password=password1
        )
        messages.success(
            request, "Registrazione completata! Ora puoi effettuare il login."
        )
        return redirect("login")

    return render(request, "tasks/register.html")

def login_view(request):
    """Vista per il login"""
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f"Benvenuto {username}!")
            return redirect("task_list")
        else:
            messages.error(request, "Username o password non corretti!")
            return redirect("login")

    return render(request, "tasks/login.html")


def logout_view(request):
    """Vista per il logout"""
    logout(request)
    messages.success(request, "Logout effettuato con successo!")
    return redirect("login")

# Vista per la dashboard con statistiche

def dashboard(request):
    """Vista per la dashboard con statistiche"""
    # Statistiche per priorità
    high_priority = Task.objects.filter(priority='high', completed=False).count()
    medium_priority = Task.objects.filter(priority='medium', completed=False).count()
    low_priority = Task.objects.filter(priority='low', completed=False).count()
    
    # Task per categoria
    categories = Task.objects.values('category').annotate(total=Count('id')).order_by('-total')
    
    # Task in scadenza nei prossimi 7 giorni
    next_week = timezone.now() + timedelta(days=7)
    upcoming_tasks = Task.objects.filter(
        completed=False,
        due_date__range=[timezone.now(), next_week]
    ).order_by('due_date')[:5]
    
    context = {
        'high_priority': high_priority,
        'medium_priority': medium_priority,
        'low_priority': low_priority,
        'categories': categories,
        'upcoming_tasks': upcoming_tasks,
    }
    return render(request, 'tasks/dashboard.html', context)
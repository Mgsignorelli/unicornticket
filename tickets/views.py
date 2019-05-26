from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from tickets.forms import TicketForm
from tickets.models import Bug, Feature


@login_required()
def create_ticket(request):
    """Allows Ticket Creation"""

    # Form is handled based on it's ticket type
    if request.method == 'POST':
        form = TicketForm(request.POST)

        if form.is_valid():
            # ticket = form.save(commit=False)
            if form.cleaned_data['type'] == 'bug':
                ticket = Bug()
            elif form.cleaned_data['type'] == 'feature':
                ticket = Feature()

            ticket.status = 'todo'
            ticket.title = form.cleaned_data['title']
            ticket.description = form.cleaned_data['description']
            ticket.creator = auth.get_user(request)
            ticket.save()
            messages.success(request, "Ticket successfully created!")

            return redirect('show_' + form.cleaned_data['type'], id=ticket.id)

    else:
        form = TicketForm()

    return render(request, 'ticket_create.html', {'form': form})


def show_bug(request, id):
    return render(request, 'ticket_show.html')


def show_feature(request, id):
    return render(request, 'ticket_show.html')


def index_bug(request):
    bugs = Bug.objects.all()
    return render(request, 'bug_index.html', {'bugs': bugs})


def index_feature(request):
    features = Feature.objects.all()
    return render(request, 'feature_index.html', {'features': features})

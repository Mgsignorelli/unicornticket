from django.shortcuts import render
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from ticket_creation.forms import TicketForm


@login_required()
def create_ticket(request):
    """Allows Ticket Creation"""

    # Form is handled based on it's ticket type
    if request.method == 'POST':
        form = TicketForm(request.POST)

        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.status = 'todo'
            ticket.creator = auth.get_user(request)
            ticket.save()
            messages.success(request, "Ticket successfully created!")

    else:
        form = TicketForm()

    return render(request, 'ticket_creation.html', {'form': form})

def read_ticket(request):
    return render(request, 'ticket_read.html')
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from tickets.forms import TicketForm, BugForm, FeatureForm
from tickets.models import Bug, Feature, BugVote, FeatureVote


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
    bug = get_object_or_404(Bug, pk=id)
    user = auth.get_user(request)

    if request.method == 'POST':
        form = BugForm(request.POST, instance=bug)

        if form.is_valid():
            form.save()
            messages.success(request, "The bug has been updated")

    form = BugForm(instance=bug)
    has_voted = True if user.is_authenticated and bug.bugvote_set.filter(voter_id__exact=user.id).count() > 0 else False
    return render(request, 'bug_show.html', {'bug': bug, 'form': form, 'user_has_voted': has_voted})


@login_required()
def vote_bug(request, id, direction):
    bug = get_object_or_404(Bug, pk=id)

    if request.method == 'POST':
        user = auth.get_user(request)
        votes = bug.bugvote_set.filter(voter_id__exact=user.id)

        if direction == 'up':
            if len(votes) == 0:
                vote = BugVote()
                vote.voter = user
                vote.bug = bug
                vote.save()
                messages.success(request, "Thank you for your vote")
            else:
                messages.error(request, "You have already voted for this bug")
        elif direction == 'down':
            if len(votes) > 0:
                votes.delete()
            else:
                messages.error(request, "You have not voted on this bug")

        else:
            messages.error(request, "Invalid direction")
    else:
        messages.error(request, "You have to post")

    return redirect('show_bug', id=bug.id)


def show_feature(request, id):
    feature = get_object_or_404(Feature, pk=id)
    user = auth.get_user(request)

    if request.method == 'POST':
        form = FeatureForm(request.POST, instance=feature)

        if form.is_valid():
            form.save()
            messages.success(request, "The feature has been updated")

    form = FeatureForm(instance=feature)
    has_voted = True if user.is_authenticated and feature.featurevote_set.filter(
        voter_id__exact=user.id).count() > 0 else False
    return render(request, 'feature_show.html', {'feature': feature, 'form': form, 'user_has_voted': has_voted})


@login_required()
def vote_feature(request, id):
    feature = get_object_or_404(Feature, pk=id)

    if request.method == 'POST':
        user = auth.get_user(request)
        votes = feature.featurevote_set.filter(voter_id__exact=user.id)

        if len(votes) == 0:
            vote = FeatureVote()
            vote.voter = user
            vote.feature = feature
            vote.save()
            messages.success(request, "Thank you for your vote")
        else:
            messages.error(request, "You have already voted for this feature")

    else:
        messages.error(request, "You have to post")

    return redirect('show_feature', id=feature.id)


def index_bug(request):
    bugs = Bug.objects.all()
    return render(request, 'bug_index.html', {'bugs': bugs})


def index_feature(request):
    features = Feature.objects.all()
    return render(request, 'feature_index.html', {'features': features})

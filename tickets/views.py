import json

from dateutil.relativedelta import relativedelta
from dateutil.utils import today
from django.core.paginator import Paginator
from django.db.models import Count
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse, resolve
from django.utils.timezone import now

from tickets.forms import TicketForm, BugForm, FeatureForm, CommentForm
from tickets.helpers import get_aggregate_count
from tickets.models import Bug, Feature, BugVote, FeatureVote, BugWork, FeatureWork, BugComment, FeatureComment
from UnicornTicketSystem.helpers import datetime_range, get_model_count_for_date_range


def index(request):
    chart_data = {
        'monthly': {
            'bugs': [],
            'features': [],
        },

        'daily': {
            'bugs': [],
            'features': [],
        },
    }

    one_year_ago = today() + relativedelta(months=-12)

    for i in range(12):
        one_year_ago = one_year_ago + relativedelta(months=+1)
        chart_data['monthly']['bugs'].append(
            get_model_count_for_date_range(BugWork, datetime_range(one_year_ago, 'month')))
        chart_data['monthly']['features'].append(
            get_model_count_for_date_range(FeatureWork, datetime_range(one_year_ago, 'month')))

    one_week_ago = today() + relativedelta(weeks=-1)

    for i in range(7):
        one_week_ago = one_week_ago + relativedelta(days=+1)
        chart_data['daily']['bugs'].append(get_model_count_for_date_range(BugWork, datetime_range(one_week_ago, 'day')))
        chart_data['daily']['features'].append(
            get_model_count_for_date_range(FeatureWork, datetime_range(one_week_ago, 'day')))

    bugs = Bug.objects.annotate(votecount=Count('bugvote')).order_by('-votecount')
    features = Feature.objects.annotate(votecount=Count('featurevote')).order_by('-votecount')
    mostvoted = {
        'bug': bugs[:1][0] if bugs.count() > 0 else [],
        'feature': features[:1][0] if features.count() > 0 else [],
    }
    return render(request, 'index.html', {'chart_data': json.dumps(chart_data), 'mostvoted': mostvoted})


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
    is_staff = True if user.is_staff else False
    return render(request, 'bug_show.html',
                  {'bug': bug, 'form': form, 'comment_form': CommentForm(), 'user_has_voted': has_voted,
                   'user_is_staff': is_staff
                   })


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
    has_votes = True if user.is_authenticated and user.featurevote_set.filter(
        feature_id__exact=None).count() > 0 else False

    has_voted = True if user.is_authenticated and feature.featurevote_set.filter(
        voter_id__exact=user.id).count() > 0 else False
    is_staff = True if user.is_staff else False
    return render(request, 'feature_show.html',
                  {'feature': feature, 'form': form, 'comment_form': CommentForm(), 'user_has_voted': has_voted,
                   'user_has_votes': has_votes, 'user_is_staff': is_staff})


@login_required()
def vote_feature(request, id):
    feature = get_object_or_404(Feature, pk=id)

    if request.method == 'POST':
        user = auth.get_user(request)
        votes = user.featurevote_set.filter(feature_id__exact=None)

        if len(votes) > 0:
            vote = votes[0]
            vote.voter = user
            vote.feature = feature
            vote.save()
            messages.success(request, "Thank you for your vote")
        else:
            messages.error(request, "You must buy votes")

    else:
        messages.error(request, "You have to post")

    return redirect('show_feature', id=feature.id)


@login_required()
def add_comment(request, id):
    url_name = resolve(request.path_info).url_name

    if request.method == "POST":
        form = CommentForm(request.POST)

        if form.is_valid():
            if url_name == 'comment_bug':
                comment = BugComment()
                comment.bug_id = id
            elif url_name == 'comment_feature':
                comment = FeatureComment()
                comment.feature_id = id

            comment.commenter = auth.get_user(request)
            comment.content = form.cleaned_data['content']
            comment.save()

            messages.success(request, "Thank you for your comment!")

        else:
            messages.error(request, "There was a problem... please try again!")

    return redirect(reverse(url_name.replace('comment', 'show'), args=(id)))


def index_bug(request):
    bugs_list = Bug.objects.annotate(votecount=Count('bugvote')).order_by('-votecount').all()
    paginator = Paginator(bugs_list, 5)
    page = request.GET.get('page')
    page = page if page is not None else '1'

    return render(request, 'bug_index.html', {'bugs': paginator.page(page)})


def index_feature(request):
    features_list = Feature.objects.annotate(votecount=Count('featurevote')).order_by('-votecount')
    paginator = Paginator(features_list, 5)
    page = request.GET.get('page')
    page = page if page is not None else '1'
    return render(request, 'feature_index.html', {'features': paginator.page(page)})

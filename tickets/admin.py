from django.contrib import admin

from tickets.models import Feature, Bug, Comment, FeatureComment, BugComment


def add_work(modeladmin, request, queryset):
    for ticket in queryset:
        if isinstance(ticket, Bug):
            ticket.bugwork_set.create()

        if isinstance(ticket, Feature):
            ticket.featurework_set.create()


add_work.short_description = "Mark as worked on"


def delete_ticket(modeladmin, request, queryset):
    for ticket in queryset:
        ticket.delete()


delete_ticket.short_description = "Delete ticket"


def delete_comment(modeladmin, request, queryset):
    for comment in queryset:
        if isinstance(comment, Bug):
            comment.delete()

        if isinstance(comment, Feature):
            comment.delete()


delete_comment.short_description = "Delete comment"


# Permits Admin to see Feature and Bug Tickets and delete them in Admin panel
@admin.register(Feature, Bug)
class TicketAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
    ordering = ['title']
    actions = [add_work, delete_ticket]


# Permits Admin to see Feature and Bug Comments and delete them in Admin panel
@admin.register(FeatureComment, BugComment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['content', 'created_date']
    ordering = ['created_date']

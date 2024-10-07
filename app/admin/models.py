from django.http import HttpResponseRedirect
from django.urls import path

from app.models import Game, Tournament, Player, Team

from django.contrib import admin

class PlayerInline(admin.StackedInline):
    model = Player
    extra = 1

@admin.register(Tournament)
class TournamentAdmin(admin.ModelAdmin):
    change_form_template = "admin/tournament/change_form.html"

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('<int:tournament_id>/myaction/', self.admin_site.admin_view(self.create_pools),
                 name='create_tournament_pools'),
        ]
        return custom_urls + urls

    def create_pools(self, request, tournament_id):
        # Implement your action logic here
        # For example, redirect to the change page after the action:
        self.message_user(request, "Custom action executed!")
        return HttpResponseRedirect(request.META['HTTP_REFERER'])


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    pass

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    pass

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    inlines = [PlayerInline]

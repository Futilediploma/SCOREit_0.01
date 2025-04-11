from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from leagues.models import League
from .forms import TeamForm
from .models import Team

def add_team(request, league_id):
    league = get_object_or_404(League, id=league_id)
    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            team = form.save(commit=False)
            team.league = league  # Associate this team with the league
            team.save()
            messages.success(request, "Team created successfully!")
            return redirect('dashboard')  # or wherever you want to redirect
    else:
        form = TeamForm()

    context = {
        'form': form,
        'league': league,
    }
    return render(request, 'teams/add_team.html', context)

def view_teams(request, league_id):
    league = get_object_or_404(League, id=league_id)
    teams = Team.objects.filter(league=league)  # Get all teams for this league
    context = {
        'league': league,
        'teams': teams,
    }
    return render(request, 'teams/view_teams.html', context)

@login_required
def edit_team(request, team_id):
    # Get the team or return a 404 if it doesn't exist.
    team = get_object_or_404(Team, id=team_id)
    
    # Check if the request is POST (form submission) or GET (load form with current data).
    if request.method == 'POST':
        form = TeamForm(request.POST, instance=team)
        if form.is_valid():
            form.save()
            messages.success(request, "Team updated successfully!")
            # Redirect to a teams view page (example: view_teams) or dashboard.
            # Here we redirect to view the teams for the team’s league.
            return redirect('view_teams', league_id=team.league.id)
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = TeamForm(instance=team)
        
    # Render the edit team template with the form.
    context = {
        'form': form,
        'team': team,
    }
    return render(request, 'teams/edit_team.html', context)
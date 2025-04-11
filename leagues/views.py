from django.shortcuts import get_object_or_404, redirect, render
from .models import League
from .forms import LeagueForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required
def add_league(request):
    if request.method == 'POST':
        form = LeagueForm(request.POST)
        if form.is_valid():
            league = form.save(commit=False)
            league.created_by = request.user
            league.save()
            messages.success(request, "League created successfully!")
            return redirect('league_list')
    else:
        form = LeagueForm()

    return render(request, 'leagues/add_league.html', {'form': form})



@login_required
def league_list(request):
    leagues = League.objects.filter(created_by=request.user)
    return render(request, 'leagues/league_list.html', {'leagues': leagues})

@login_required
def edit_league(request, league_id):
    league = League.objects.get(id=league_id, created_by=request.user)

    if request.method == 'POST':
        form = LeagueForm(request.POST, instance=league)
        if form.is_valid():
            form.save()
            return redirect('league_list')
    else:
        form = LeagueForm(instance=league)

    return render(request, 'leagues/edit_league.html', {'form': form, 'league': league})

@login_required
def delete_league(request, league_id):
    league = get_object_or_404(League, id=league_id, created_by=request.user)
    if request.method == 'POST':
        league.delete()
        messages.success(request, "League deleted successfully!")
        return redirect('dashboard')
    # Optionally, you could add a confirmation page:
    return render(request, 'leagues/confirm_delete.html', {'league': league})
from django.shortcuts import render, get_object_or_404, redirect
from .models import TeamMember
from .forms import TeamMemberForm


# Create your views here.
def team_member_list(request):
    team_members = TeamMember.objects.all()
    return render(request, 'team/team_member_list.html', {'team_members': team_members})


def team_member_add(request):
    if request.method == 'POST':
        form = TeamMemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('team_member_list')
    else:
        form = TeamMemberForm()
    return render(request, 'team/team_member_form.html', {'form': form, 'action': 'Add'})


def team_member_edit(request, pk):
    team_member = get_object_or_404(TeamMember, pk=pk)
    if request.method == 'POST':
        form = TeamMemberForm(request.POST, instance=team_member)
        if form.is_valid():
            form.save()
            return redirect('team_member_list')
    else:
        form = TeamMemberForm(instance=team_member)
    return render(request, 'team/team_member_form.html', {'form': form, 'action': 'Edit', 'team_member': team_member})


def team_member_delete(request, pk):
    team_member = get_object_or_404(TeamMember, pk=pk)
    team_member.delete()
    return redirect('team_member_list')

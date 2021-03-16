from django.shortcuts import render, redirect, get_object_or_404
from .forms import ListForm
from django.contrib import messages
from .models import List, ScoreStat
from django.contrib.auth.decorators import login_required, permission_required
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class HomeView(generic.TemplateView):
    template_name = "todo/home.html"


class DashboardView(LoginRequiredMixin, generic.View):
    login_url = '/user/auth/login/'
    redirect_field_name = 'home'
    template_name = 'todo/dashboard.html'
    context = {}

    def get(self, request, *args, **kwargs):
        incomplete_tasks = List.objects.filter(user=request.user, is_completed=False)
        complete_tasks = List.objects.filter(user=request.user, is_completed=True)

        score_stat, created = ScoreStat.objects.get_or_create(user=self.request.user)
        score_stat.refresh_score
        score_stat.calculate_score
        score_stat.save()

        seven_days_scores = score_stat.calculate_seven_days_score
        current_score = score_stat.current_score
        
        self.context = {
            'incomplete_tasks_count': incomplete_tasks.count(),
            'complete_tasks_count': complete_tasks.count(),
            'current_score': current_score,
            'seven_days_scores': seven_days_scores
        }
        return render(self.request, self.template_name, self.context)
    
    def post(self, request, *args, **kwargs):
        pass


class ManageListView(generic.View):
    context = {}
    template_name = 'todo/task-manager.html'
    
    def get(self, request, *args, **kwargs):
        tasks = List.objects.filter(user=request.user)
        form = ListForm()
        self.context = {
            'tasks': tasks,
            'task_form': form
            # 'complete_tasks_count': complete_tasks.count(),
            # 'current_score': current_score,
        }
        return render(self.request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        form = ListForm(request.POST or None)
        if form.is_valid():
            print(form.cleaned_data)
            name = form.cleaned_data['name']
            weight = form.cleaned_data['weight']
            List.objects.create(user=request.user, name=name, weight=weight)
            form.save()
            # all_tasks = List.objects.filter(user=request.user).all()
            #     self.context['all_tasks'] = all_tasks
            messages.success(request, ("Task has been added to the list!"))
            # return render(self.request, self.template_name, self.context)
            return redirect('task-manager')


@login_required
def delete(request, id):
    item = get_object_or_404(List, id=id)
    item.delete()
    messages.success(request, ('Item has been deleted successfully!'))
    return redirect('task-manager')

@login_required
def done(request, id):
    item = get_object_or_404(List, id=id)
    item.is_completed = True
    item.status = 'Work completed'
    item.save()
    return redirect('task-manager')

@login_required
def undone(request, id):
    item = get_object_or_404(List, id=id)
    item.is_completed = False
    item.status = 'Work not completed'    
    item.save()
    return redirect('task-manager')

@login_required
def update(request, id):
    if request.method == "POST":
        item = get_object_or_404(List, id=id)
        form = ListForm(request.POST or None, instance=item)
        print(form)
        if form.is_valid():
            form.save()
            messages.success(request, ('Item has been edited'))
            return redirect('task-manager')
    else:
        return redirect('task-manager')

# def contact_view(request):
#     template_name = 'todo_list/contact_page.html'
#     context = {'emails': ['sandipan.das898@gmail.com', 'sisir.das983@gmail.com'], 
#                 'github': 'https://github.com/sandipan89',
#                 'linkedin': 'https://www.linkedin.com/in/sandipan-das-528166175/',
#                 }
#     return render(request, template_name, context)

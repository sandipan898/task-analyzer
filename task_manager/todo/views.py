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

        score_stat = ScoreStat.objects.get(user=self.request.user)
        current_score = score_stat.calculate_score
        print(current_score)
        
        self.context = {
            'incomplete_tasks_count': incomplete_tasks.count(),
            'complete_tasks_count': complete_tasks.count(),
            'current_score': current_score
        }
        return render(self.request, self.template_name, self.context)
    
    def post(self, request, *args, **kwargs):
        pass


class ManageListView(generic.View):
    context = {}
    template_name = 'todo/task-manager.html'
    def get(self, request, *args, **kwargs):
        pass

    def post(self, request, *args, **kwargs):
        form = ListForm(request.POST or None)
        if form.is_valid():
            print(form.cleaned_data)
            item = form.cleaned_data['item']
            weight = form.cleaned_data['weight']
            List.objects.create(user=request.user, item=item, weight=weight)
            form.save()
            print(request.user.list_set)
            all_tasks = List.objects.filter(user=request.user).all()
            self.context['all_tasks'] = all_tasks
            messages.success(request, ("Task has been added to the list!"))
        return render(self.request, self.template_name, self.context)


@login_required
def delete(request, id):
    item = get_object_or_404(List, id=id)
    item.delete()
    messages.success(request, ('Item has been deleted successfully!'))
    return redirect('home')

@login_required
def done(request, id):
    item = get_object_or_404(List, id=id)
    item.completed = True
    item.save()
    return redirect('home')

@login_required
def undone(request, id):
    item = get_object_or_404(List, id=id)
    item.completed = False
    item.save()
    return redirect('home')

@login_required
def update(request, id):
    template_name = 'todo_list/update.html'
    context = {}
    if request.method == "POST":
        item = get_object_or_404(List, id=id)
        form = ListForm(request.POST or None, instance=item)

        if form.is_valid():
            form.save()
            messages.success(request, ('Item has been edited'))
            return redirect('home')
    
    else:
        item = get_object_or_404(List, id=id)
        context['object'] = item
        return render(request, template_name, context)


# def about_view(request):
#     template_name = 'todo_list/about_page.html'
#     context = {}
#     return render(request, template_name, context)

# def contact_view(request):
#     template_name = 'todo_list/contact_page.html'
#     context = {'emails': ['sandipan.das898@gmail.com', 'sisir.das983@gmail.com'], 
#                 'github': 'https://github.com/sandipan89',
#                 'linkedin': 'https://www.linkedin.com/in/sandipan-das-528166175/',
#                 }
#     return render(request, template_name, context)

# def help_view(request):
#     template_name = 'todo_list/help_page.html'
#     context = {}
#     return render(request, template_name, context)

from django.shortcuts import redirect
from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
#from . import forms


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

    

"""
    class SeatChoiceView(View):
        def get(self, request):
            form = forms.SeatChoiceForm()
            context = {
                'form': form
            }

            return render(request, 'blog/post_detail.html', context)

    class SeatChoiceAddView(View):
        def get(self, request):
            form = forms.SeatChoiceAddForm()
            form.fields['choice1'].choices = [
                ('1', '1番目'),
                ('2', '2番目'),
                ('3', '3番目'),
                ('4', '4番目'),
                ('5', '5番目'),
            ]
            context = {
                'form': form
            }

            return render(request, 'blog/post_detail.html', context)

    seat_choice_view = SeatChoiceView.as_view()
    seatchoice_add_view = SeatChoiceAddView.as_view()

"""
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

"""
def get_form_kwargs(self, *args, **kwargs):
    kwgs = super().get_form_kwargs(*args, **kwargs)
    category_choice = (("SS", "SS"), ("S", "S"), ("A", "A"), ("B", "B"), ("stand", "立見")),
    kwgs["categories"] = category_choice
    return kwgs


def post(request):
    # Forms
    seat_form = SeatForm()

    # Model Forms
    seat_model_form = SeatModelForm()


    return render(request, 'post_detail.html', {
        'seat_form': seat_form,
        'seat_model_form': seat_model_form,
    })

"""
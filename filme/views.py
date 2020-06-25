from django.shortcuts import render, redirect

from filme.forms import FilmeForm
from filme.models import Filme


def list_filme(request):
    filmes = Filme.objects.all()
    return render(request, 'filme.html', {'filmes': filmes})


def create_filme(request):
    form = FilmeForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_filme')

    return render(request, 'filme-form.html', {'form': form})


def update_filme(request, id):
    filme = Filme.objects.get(id=id)
    form = FilmeForm(request.POST or None, instance=filme)

    if form.is_valid():
        form.save()
        return redirect('list_filme')

    return render(request, 'filme-form.html', {'form': form, 'filme': filme})


def delete_filme(request, id):
    filme = Filme.objects.get(id=id)

    if request.method == 'POST':
        filme.delete()
        return redirect('list_filme')

    return render(request, 'filme-delete-confirm.html', {'filme': filme})

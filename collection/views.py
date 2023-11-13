from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from collection.models import Artwork, Collection
import random
from django.contrib.postgres import search
from django.core.paginator import Paginator
from .forms import CollectionForm, ConfirmDeleteForm

def register(request):
    if request.method == 'POST':
        f = UserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            username = f.cleaned_data.get('username')
            raw_password = f.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)

            return HttpResponseRedirect('/')

    else:
        f = UserCreationForm()

    return render(request, 'registration/registration_form.html', {'form': f})


def index(request):
    artworks = list(Artwork.objects.all())
    random_works = []
    if artworks:
        random_works = random.sample(artworks, 12)
    return render(request, 'collection/index.html', {'artworks': random_works})


def artwork(request, artwork_id):
    artwork = Artwork.objects.get(pk=artwork_id)
    return render(request, 'collection/artwork.html',{'artwork':artwork})

def random_artworks(request):
    artworks = list(Artwork.objects.all())
    random_works = []
    if artworks:
        random_works = random.sample(artworks, 12)
    return render(request, 'collection/artworks_random.html',
                  {'artworks': random_works})

def search_artworks(request):
    if request.method == 'GET':
        value = request.GET['search']
        artworks = ft_artworks(value)

        paginator = Paginator(artworks, 4)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        return render(request, 'collection/artwork_search.html',
                      {'artworks': artworks, 'search_value': value,
                       "page_obj": page_obj})
    else:
        return render(request, 'collection/index.html',
                      {'artworks': [], 'search_value': None})


def ft_artworks(value):
    vector = (
        search.SearchVector("title", weight="A")
        + search.SearchVector("author__name", weight="B")
        + search.SearchVector("style__name", weight="C")
        + search.SearchVector("genre__name", weight="C")
    )
    query = search.SearchQuery(value, search_type="websearch")
    return (
        Artwork.objects.annotate(
            search=vector,
            rank=search.SearchRank(vector, query),
        )
        .filter(search=query)
        .order_by("-rank")
    )

def collections(request):
    collections = Collection.objects.filter(owner=request.user)
    return render(request, 'collection/collections.html',
                  {'collections': collections})


def collection_list(request):
    collections = Collection.objects.filter(owner=request.user)
    for c in collections:
        random_image(c.pk)
    return render(request, 'collection/collection_list.html',
                  {'collections': collections})

def random_image(request, collection_id):
    collections = Collection.objects.get(pk=collection_id)
    print(collections.artworks.all())
    x = list(collections.artworks.all())
    if x:
        a = random.sample(x, 1)
        print(a)
    return render(request, 'collection/collection_list.html',
                  {'collections': collections, 'a': a})


def collection_add(request):
    form = None
    if request.method == 'POST':
        form = CollectionForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            collection = Collection(
                    name=name,
                    description=description,
                    owner=request.user)
            collection.save()
            return HttpResponse(status=204,
                                headers={'HX-Trigger': 'listChanged'})

    return render(request,
                  'collection/collection_form.html',
                  {'form': form})

def collection_edit(request, collection_id):
    collection = get_object_or_404(Collection, id=collection_id) if collection_id else None

    if request.method == 'POST':
        form = CollectionForm(request.POST)
        if form.is_valid():
            # Guardar o actualizar la colección según sea necesario
            if collection:
                collection.name = form.cleaned_data['name']
                collection.description = form.cleaned_data['description']
                collection.save()
            else:
                Collection.objects.create(
                    name=form.cleaned_data['name'],
                    description=form.cleaned_data['description'],
                    owner=request.user
                )

            return HttpResponse(status=204, headers={'HX-Trigger': 'listChanged'})
    else:
        # Si no hay colección existente, crea un formulario en blanco
        initial_data = {'name': collection.name, 'description': collection.description} if collection else None
        form = CollectionForm(initial=initial_data)

    return render(request, 'collection/collection_formedit.html', {'collection': collection,'form': form})


def collection_delete(request, collection_id):
    collection = get_object_or_404(Collection, id=collection_id)

    if request.method == 'POST':
        form = ConfirmDeleteForm(request.POST)

        if form.is_valid():
            # Verifica que el usuario que solicita la eliminación sea el propietario de la colección
            print("Es valida")
            if request.user == collection.owner:
                print("pertence al usuario")
                # Realiza la eliminación
                collection.delete()

                # Redirige al usuario a donde desees después de la eliminación
                return HttpResponse(status=204, headers={'HX-Trigger': 'listChanged'})
            else:
                # Devuelve una respuesta no autorizada si el usuario no es el propietario
                return HttpResponse(status=401)
        else:
            # Maneja el caso en que el formulario no sea válido (puede ser necesario mostrar un mensaje de error)
            return HttpResponse(status=400)
    else:
        form = ConfirmDeleteForm()

    return render(request, 'collection/confirm_delete.html', {'collection': collection, 'form': form})


def collection_artworks(request, collection_id):
    collections = Collection.objects.get(pk=collection_id)
    return render(request, 'collection/artwork_collection.html', {'artworks': collections.artworks.all()})


def artwork_add_to_collectionFORM(request, artwork_id):
    collection = Collection.objects.filter(owner=request.user)
    artwork = Artwork.objects.get(pk=artwork_id)
    form = None
    if request.method == 'POST':
        print(request)
        form = CollectionForm(request.POST)
        artwork = Artwork.objects.get(pk=artwork_id)
        print('Entro')
        collection = Collection(
                artworks = artwork
                )
        collection.save()
        return HttpResponse(status=204,
                            headers={'HX-Trigger': 'listChanged'})
        
    return render(request,
                  'collection/select_collection.html',
                  {'form': form, 'collections': collection, 'artwork': artwork})



def SendArtworkTo(request, artwork_id, collection_id):
    collection = Collection.objects.get(pk=collection_id)
    artwork = Artwork.objects.get(pk=artwork_id)
    form = None
    if request.method == 'POST':
        form = CollectionForm(request.POST)
        artwork = Artwork.objects.get(pk=artwork_id)
        print('Entro a Send')
        collection.artworks.add(artwork)
        collection.save()
        return HttpResponse(status=204,
                            headers={'HX-Trigger': 'listChanged'})
    return render(request,
                  'collection/select_collection.html',
                  {'form': form, 'collections': collection, 'artwork': artwork})
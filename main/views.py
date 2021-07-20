from django.shortcuts import render, redirect
from rest_framework.permissions import  IsAuthenticatedOrReadOnly
from main.models import Book
from .serializers import BookSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
def log_in(request):
    if not request.user.is_anonymous:
        return redirect('homepage')
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("homepage")
        else:
            return render(request=request, 
                    template_name="login.html",
                    context={"error_message": "Invalid credentials.!"})
    return render(request, template_name="login.html")


def logout_view(request):
    logout(request)
    messages.info(request, "Logged out successfully.!")
    return redirect("login")


@login_required(login_url="login")
def detail(request, pk):
    return render(request, 
    template_name="detail.html",
    context={"pk": pk})

class BookListView(LoginRequiredMixin, ListView):        
    login_url = "/login/"
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    context_object_name = 'books'
    paginate_by = 8
    template_name = 'index.html'  


class BookView(APIView):
    
    response = {
        'status': False
    }
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, pk):
        books = Book.objects.get(pk=pk)
        books_serializer = BookSerializer(books)
        book = books_serializer.data
        self.response['status'] = True
        self.response['book'] = book
        return Response(self.response)
            
    
    def post(self, request):
        try:
            data = request.data
            serializer = BookSerializer(data=data)

            if serializer.is_valid(raise_exception=True):
                serializer.create(data)
            
            self.response['status'] = True
            self.response['message'] = f"Book {data['name']} successfully created."
            messages.info(request, self.response['message'])
            return Response(self.response)
        except Exception as e:
            self.response['error'] = f"{e.__class__.__name__}"
            return Response(self.response)


    def put(self, request, pk):
        try:
            book = Book.objects.get(pk=pk)
            serializer = BookSerializer(book, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
            self.response['status'] = True
            self.response['message'] = f"Book successfully updated."
            messages.info(request, self.response['message'])
            return Response(self.response)
        except Exception as e:
            self.response['error'] = f"{e.__class__.__name__}"
            return Response(self.response)


    def delete(self, request, pk):
        try:
            book = Book.objects.get(pk = pk)
            book_name = book.name
            book.delete()
            self.response['status'] = True
            self.response['message'] = f"Book {book_name} successfully deleted."
            messages.info(request, self.response['message'])
            return Response(self.response)
        except Exception as e:
            self.response['error'] = f"{e.__class__.__name__}"
            return Response(self.response)


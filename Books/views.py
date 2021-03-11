from django.shortcuts import render,redirect
# Create your views here.
from Books.models import Book
from django.urls import reverse_lazy
from Books.forms import BookCreateForm
from django.views.generic import CreateView,ListView,UpdateView,DeleteView,DetailView,TemplateView


# class BookCreate(CreateView):
#     model=Book
#     fields="__all__"
#     template_name = "books/book_form.html"
#     success_url = reverse_lazy('list')
#
# class BookList(ListView):
#     model = Book
#     fields="__all__"
#     template_name = "books/book_list.html"
#     context_object_name = "books"
# class BookEdit(UpdateView):
#     model=Book
#     fields="__all__"
#     success_url = reverse_lazy('list')
#     template_name="books/book_edit.html"
#
# class BookDelete(DeleteView):
#     model=Book
#     fields="__all__"
#     success_url = reverse_lazy('list')
#     template_name="books/book_delete.html"
#
# class BookView(DetailView):
#     model = Book
#     context_object_name = "book"
#     template_name="books/book_detail.html"
#

class BookCreate(TemplateView):
    form_class=BookCreateForm()
    template_name="books/book_form.html"
    context={}
    def get(self, request,*args,**kwargs):
        form=BookCreateForm()
        self.context["form"]=form
        return render(request,self.template_name,self.context)
    def post(self,request,*args,**kwargs):
        form=BookCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list")

class BookList(TemplateView):
    model=Book
    template_name = "books/book_list.html"
    context={}

    def get_query_set(self):
        return self.model.objects.all()

    def get(self,request,*args,**kwargs):
        self.context["books"]=self.get_query_set()
        return render(request,self.template_name,self.context)

class BookEdit(TemplateView):
    model=Book
    template_name = "books/book_edit.html"
    context={}

    def get_query_set(self,id):
        return self.model.objects.get(id=id)

    def get(self,request,*args,**kwargs):
        book=self.get_query_set(kwargs.get("pk"))
        form=BookCreateForm(instance=book)
        self.context["form"]=form
        return render(request,self.template_name,self.context)
    def post(self,request,*args,**kwargs):
        book=self.get_query_set(kwargs.get("pk"))
        form=BookCreateForm(instance=book,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("list")

class BookDelete(TemplateView):
    model=Book
    def get_object(self,id):
        return self.model.objects.get(id=id)
    def get(self,request,*args,**kwargs):
        book=self.get_object(kwargs.get("pk"))
        book.delete()
        return redirect("list")







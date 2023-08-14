from django.urls import path
# from book.views import home, store_book, show_books, edit_book, delete_book
from . import views

urlpatterns = [
    # path('', views.home), # function based view
    path('', views.TemplateView.as_view(template_name='home.html')), #template based view
    path('<int:roll>/', views.MyTemplateView.as_view(),{'author': 'Rahim'}, name='home'), #class based view
    # path('store_new_book/', views.store_book, name='storebook'), #function based
    path('store_new_book/', views.BookFormView.as_view(), name='storebook'),
    # path('show_books/', views.show_books, name='show_books'), #function based
    path('show_books/', views.BookListView.as_view(), name='show_books'), #class based
    path('book_details/<int:id>', views.BookDetailView.as_view(), name='book_details'), #class based
    # path('edit_book/<int:pk>', views.edit_book, name='edit_book'), # function based
    path('edit_book/<int:pk>', views.BookUpdateView.as_view(), name='edit_book'), # class based
    # path('delete_book/<int:pk>', views.delete_book, name='delete_book'), # function based
    path('delete_book/<int:pk>', views.DeleteBookView.as_view(), name='delete_book'), # class based
]

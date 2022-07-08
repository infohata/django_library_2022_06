from django import forms
from . models import BookReview, BookInstance


class BookReviewForm(forms.ModelForm):
    class Meta:
        model = BookReview
        fields = ('content', 'book', 'reviewer')
        widgets = {
            'book': forms.HiddenInput(),
            'reviewer': forms.HiddenInput(),
        }


class DateInput(forms.DateInput):
    input_type = 'date'


class BookInstanceForm(forms.ModelForm):
    class Meta:
        model = BookInstance
        fields = ('book', 'due_back', )
        widgets = {'due_back': DateInput(), }

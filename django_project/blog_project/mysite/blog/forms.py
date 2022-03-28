from tkinter import Widget
from django import forms
from blog.models import Post,Comment


class PostForm(forms.ModelForm):

    class Meta():
        model = Post 
        fields = ('author','title','text')

        Widget ={
            'title':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea'})
        }


class CommentForm(forms.ModelForm):

    class Meta():
        model = Comment
        fields =('author','text')

        Widgets = {
            'author':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea'})

        }
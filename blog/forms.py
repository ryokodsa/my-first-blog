from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'place', 'date', 'time', 'seat', 'ticket',)

"""
    class SeatForm(forms.Form):
        COLORS = (
            (11, 'SALT & PEPPER'),
            (12, 'DARK GREY'),
            (21, 'GREY'),
            (22, 'CHOCOLATE'),
            (23, 'BROWN'),
            (31, 'CINNAMON'),
            (32, 'DARK CINNICOT'),
        )
        name = forms.DecimalField()
        birthday = forms.DateField()
        ColorType = forms.ChoiceField(choices=COLORS)

class SeatChoiceForm(forms.Form):
    choice1 = forms.fields.ChoiceField(
        choices = (
            ('SS', 'SS'),
            ('S', 'S'),
            ('A', 'A'),
            ('B', 'B'),
            ('stand', '立見')
        ),
        required=True,
        widget=forms.widgets.Select
    )

class SeatChoiceAddForm(forms.Form):
    choice1 = forms.fields.ChoiceField(
        required=True,
        widget=forms.widgets.Select
    )



class LeadForm(forms.ModelForm):
    category = forms.ChoiceField()

    class Meta:
        model = Post
        fields = "__all__"

    def __init__(self, categories=None, *args, **kwargs):
        self.base_fields["category"].choices = categories
        super().__init__(*args, **kwargs)
"""
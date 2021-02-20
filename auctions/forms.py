from django import forms

from .models import Listing


class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ['title', 'description', 'starting_bid', 'image', 'category']


class BidingForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.min_value = kwargs.pop('min_bid')
        super(BidingForm, self).__init__(*args, **kwargs)
        self.fields['bidding'] = forms.FloatField(min_value=self.min_value)

    bidding = forms.FloatField()
from logging import getLogger

from django.core.exceptions import ValidationError
from django.forms import ModelForm, CharField

from base.models import Room

LOGGER = getLogger()


class RoomForm(ModelForm):
    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) < 2:
            validation_error = ValidationError("Name must contains minimal 2 chars.")
            LOGGER.warning(f'{validation_error}: {name}')
            raise validation_error
        return name

    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['participants']

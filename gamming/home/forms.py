from django import forms
from.models import Registration


class Registration_form(forms.ModelForm):

    class Meta:
        model = Registration
        fields = ('team_name', 'team_image',
                  'player_1', 'player_1_pubg_id',
                  'player_2', 'player_2_pubg_id',
                  'player_3', 'player_3_pubg_id',
                  'player_4', 'player_4_pubg_id',
                  'contact_number',

                  )

    def clean_player_1(self):
        player_1 = self.cleaned_data.get('player_1')
        qs = Registration.objects.player_exists(player_1)
        if qs.exists():
            raise forms.ValidationError('Player name {} already taken if you are not please contact our support team'.format(player_1))
        return player_1

    def clean_player_2(self):
        player_2 = self.cleaned_data.get('player_2')
        qs = Registration.objects.player_exists(player_2)
        if qs.exists():
            raise forms.ValidationError('Player name {} already taken if you are not please contact our support team'.format(player_2))
        return player_2

    def clean_player_3(self):
        player_3 = self.cleaned_data.get('player_3')
        qs = Registration.objects.player_exists(player_3)
        if qs.exists():
            raise forms.ValidationError('Player name {} already taken if you are not please contact our support team'.format(player_3))
        return player_3


    def clean_player_4(self):
        player_4 = self.cleaned_data.get('player_4')
        qs = Registration.objects.player_exists(player_4)
        if qs.exists():
            raise forms.ValidationError('Player name {} already taken if you are not please contact our support team'.format(player_4))
        return player_4

    def clean_player_1_pubg_id(self):
        player_1_pubg_id = self.cleaned_data.get('player_1_pubg_id')
        qs = Registration.objects.id_exists(player_1_pubg_id)
        if qs.exists():
            raise forms.ValidationError('Player {} pubg_id  already taken if you are not please contact our support team'.format(player_1_pubg_id))
        return player_1_pubg_id

    def clean_player_2_pubg_id(self):
        player_2_pubg_id = self.cleaned_data.get('player_2_pubg_id')
        qs = Registration.objects.id_exists(player_2_pubg_id)
        if qs.exists():
            raise forms.ValidationError('Player {} pubg_id already taken if you are not please contact our support team'.format(player_2_pubg_id))
        return player_2_pubg_id

    def clean_player_3_pubg_id(self):
        player_3_pubg_id = self.cleaned_data.get('player_3_pubg_id')
        qs = Registration.objects.id_exists(player_3_pubg_id)
        if qs.exists():
            raise forms.ValidationError('Player {} pubg_id already taken if you are not please contact our support team'.format(player_3_pubg_id))
        return player_3_pubg_id

    def clean_player_4_pubg_id(self):
        player_4_pubg_id = self.cleaned_data.get('player_4_pubg_id')
        qs = Registration.objects.id_exists(player_4_pubg_id)
        if qs.exists():
            raise forms.ValidationError('Player {} pubg_id already taken if you are not please contact our support team'.format(player_4_pubg_id))
        return player_4_pubg_id

    def clean_contact_number(self):
        phone_no = self.cleaned_data.get('contact_number')
        if phone_no is None:
            raise forms.ValidationError("Please enter a valid phone number")

        return phone_no


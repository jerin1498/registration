from django.contrib import admin
from .models import Registration

# Register your models here.


class RegistrationAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'verified', 'qualified', 'match_day',
                    'semi_final_match', 'final_match',  'team_position', 'contact_number']

    list_filter = ('verified', 'qualified', )

    search_fields = ('team_name', 'player_1', 'player_1_pubg_id', 'player_2', 'player_2_pubg_id',
                     'player_3', 'player_3_pubg_id', 'player_4', 'player_4_pubg_id', 'contact_number')

    class Meta:
        model = Registration
        fields = [
            'team_name',
            'team_image',
            'team_position',
            'player_1',
            'player_1_pubg_id',
            'player_2',
            'player_2_pubg_id',
            'player_3',
            'player_3_pubg_id',
            'player_4',
            'player_4_pubg_id',
            'timestamp',
            'slug',
            'verified',
            'qualified',
            'semi_final_match',
            'final_match',
            'match_day',
            'contact_number'
        ]



admin.site.register(Registration, RegistrationAdmin)



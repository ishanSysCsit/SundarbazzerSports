
from django import forms
from .models import Match,Goal,Fall,MatchTimeManager,Substitution,MatchPauseResume
from sportsApp.models import EventTeam
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.db import models
from datetime import timedelta,datetime
from django.utils.timezone import now

class MatchForm(forms.ModelForm):
    class Meta:
        model = Match
        fields = ['event', 'team1', 'team2','status', 'is_address_default', 'match_date', 'match_time', 'place', 'match_complete', 'notes','schedule']
        widgets = {
            'match_date': forms.DateInput(attrs={'type': 'date'}),
            'match_time': forms.TimeInput(attrs={'type': 'time'}),
            'notes': forms.Textarea(attrs={'rows': 4, 'cols': 50}),
        }
    def __init__(self, *args, **kwargs):
            # Capture the selected event if passed as an argument
            event = kwargs.pop('event', None)
            super().__init__(*args, **kwargs)
            
            # If an event is specified, filter teams to those related to that event
            if event:
                self.fields['team1'].queryset = EventTeam.objects.filter(event=event)
                self.fields['team2'].queryset = EventTeam.objects.filter(event=event)
            else:
                # Default to an empty queryset if no event is provided
                self.fields['team1'].queryset = EventTeam.objects.none()
                self.fields['team2'].queryset = EventTeam.objects.none()


    def clean(self):
        cleaned_data = super().clean()
        event = cleaned_data.get('event')
        team1 = cleaned_data.get('team1')
        team2 = cleaned_data.get('team2')
        match_date = cleaned_data.get('match_date')
        match_time = cleaned_data.get('match_time')
        today = timezone.now().date()

        # 1. Check if the same team is selected for both team1 and team2
        if team1 and team2 and team1 == team2:
            raise ValidationError("A team cannot play against itself.")

        # Creation-specific validations
        if not self.instance.pk:  # Only for new instances
            # Check for existing match on the same date and time between the same teams
            if team1 and team2 and match_date and match_time:
                existing_match = Match.objects.filter(
                    match_date=match_date,
                    match_time=match_time
                ).filter(
                    (models.Q(team1=team1) & models.Q(team2=team2)) |
                    (models.Q(team1=team2) & models.Q(team2=team1))
                ).exists()
                if existing_match:
                    raise ValidationError("A match between these teams already exists at the same date and time.")

            # Check if match_date is today or a future date
            if match_date and match_date < today:
                raise ValidationError({'match_date': "Invalid Date Selected. Please select a future date."})

            # Check if match_date is after the event start date
            if event and match_date:
                event_start_date_only = event.event_start_date.date()
                if match_date < event_start_date_only:
                    raise ValidationError({'match_date': f"Match date cannot be before the event start date ({event_start_date_only})."})

        return cleaned_data



class GoalForm(forms.ModelForm):
    class Meta:
        model = Goal
        fields = ['match', 'player', 'goal_description', 'goal_type', 'goal_time']
        widgets = {
            'goal_description': forms.TextInput(attrs={'placeholder': 'Describe the goal', 'class': 'form-control'}),
            'goal_type': forms.Select(attrs={'class': 'form-select'}),
            'goal_time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'match': forms.Select(attrs={'class': 'form-select'}),
            'player': forms.Select(attrs={'class': 'form-select'}),
        }
        labels = {
            'goal_description': 'Description',
            'goal_type': 'Type of Goal',
            'goal_time': 'Time of Goal',
        }


    def clean(self):
        cleaned_data = super().clean()
        match = cleaned_data.get('match')
        player = cleaned_data.get('player')

        print('player',player)
        

        return cleaned_data

    def save(self, commit=True):
        # Perform validation again before saving
        self.clean()
        return super().save(commit=commit)



class CustomRadioSelect(forms.RadioSelect):
    template_name = 'widgets/custom_radio.html'  # Custom template for radio buttons

class FoulForm(forms.ModelForm):
    class Meta:
        model = Fall
        fields = ['match', 'player', 'fall_category', 'fall_type', 'fall_description', 'fall_time']
        widgets = {
            'fall_category': CustomRadioSelect,  # Use radio buttons for this field
            'fall_type': forms.Select,      # Use radio buttons for this field
        }
        labels = {
            'fall_category': 'Foul Category',
            'fall_type': 'Foul Type',
            'fall_description': 'Description',
            'fall_time': 'Time of Foul',
        }


class MatchTimeManagerForm(forms.ModelForm):
    class Meta:
        model = MatchTimeManager
        fields = [
            'start_time',
            'extra_time_first_half',
            'extra_time_full_time',
            'is_half_time_over',
            'match_ended'
        ]
        
        widgets = {
            'start_time': forms.DateTimeInput(attrs={'type': 'datetime-local','required':True}),
            'extra_time_first_half': forms.TimeInput(attrs={'type': 'duration'}),
            'extra_time_full_time': forms.TimeInput(attrs={'type': 'duration'}),
        }
    

    # def __init__(self,*args,**kwargs):
    #     instance = kwargs.get('instance')

    #     if instance and instance.start_time is None:
    #         match = instance.match

    #         if match.match_time:
    #             instance.start_time = match.match_time
    #     super().__init__(*args,**kwargs)



# class for the substitution

class SubstitutionForm(forms.ModelForm):
    class Meta:
        model = Substitution
        fields = ['match', 'player_out', 'player_in', 'time', 'is_emergency_substitution']
        widgets = {
            'time': forms.TimeInput(attrs={'type': 'time'}),
        }
        


    def clean(self):
        cleaned_data = super().clean()
        match = cleaned_data.get('match')
        player_out = cleaned_data.get('player_out')
        player_in = cleaned_data.get('player_in')

        if match and player_out and player_in:
            if Substitution.objects.filter(match=match, player_out=player_out, player_in=player_in).exists():
                raise forms.ValidationError(
                    f"A substitution for Player Out '{player_out}' and Player In '{player_in}' has already occurred in match {match}."
                )
            if player_out.team != player_in.team:
                raise forms.ValidationError("Player Out and Player In must belong to the same team.")
            
            if player_out.team != match.team1.team and player_out.team != match.team2.team:
                raise forms.ValidationError("Players must be from one of the teams in the selected match.")
        
        return cleaned_data



class MatchPauseResumeForm(forms.ModelForm):
    class Meta:
        model = MatchPauseResume
        fields = ['match', 'paused_at', 'resumed_at', 'is_before_half']
        
        widgets = {
            'paused_at': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'resumed_at': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
        
        help_texts = {
            'paused_at': 'The time when the match was paused.',
            'resumed_at': 'The time when the match resumed.',
        }

    def clean(self):
        cleaned_data = super().clean()
        match = cleaned_data.get('match')

        if match:
            # Get the related MatchTimeManager from the match
            match_time_manager = match.time_manager # Assuming related name is 'match_time_manager'
            
            if match_time_manager:
                first_half_start_time = match_time_manager.first_half_start_time
                second_half_start_time = match_time_manager.second_half_start_time
                
                if first_half_start_time and second_half_start_time:
                    cleaned_data['is_before_half'] = False  # Both are present, so set to False
                elif first_half_start_time and not second_half_start_time:
                    cleaned_data['is_before_half'] = True  # Only first half start time present, so set to True
                else:
                    raise ValidationError({
                        'is_before_half': 'Both first_half_start_time and second_half_start_time are missing.'
                    })
            else:
                raise ValidationError({
                    'match': 'Match Time Manager is not linked to this match.'
                })
        else:
            raise ValidationError({
                'match': 'Match is required.'
            })

        paused_at = cleaned_data.get('paused_at')
        resumed_at = cleaned_data.get('resumed_at')
        
        if resumed_at and resumed_at <= paused_at:
            self.add_error('resumed_at', 'Resume time must be after the pause time.')
        
        return cleaned_data
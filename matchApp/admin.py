from django.contrib import admin
from .models import Guest,Goal,Fall,Substitution,PlayerMatchEvents, Match,MatchTimeManager,MatchPauseResume

# Register your models here.



class GoalInline(admin.TabularInline):
    model = Goal
    extra = 1

@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
    
    list_display = ('id','player','match','goal_time','goal_type')

@admin.register(Fall)
class FoulAdmin(admin.ModelAdmin):
    list_display = ('id','player','match','fall_time','fall_type','fall_category')


class FallInline(admin.TabularInline):
    model = Fall
    extra = 1

class SubstitutionInline(admin.TabularInline):
    model = Substitution
    extra = 1

class PlayerEventsInline(admin.TabularInline):
    model = PlayerMatchEvents
    extra = 1



@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    inlines = [GoalInline,FallInline,SubstitutionInline,PlayerEventsInline]
    list_display = ('team_vs','match_date','place','match_complete')


    def team_vs(self,obj):
        return f'{obj.team1} vs {obj.team2}'


@admin.register(Guest)
class GuestAdmin(admin.ModelAdmin):
    list_display = ('name','designation','is_event_guest','match')


@admin.register(MatchTimeManager)
class MatchTimeManagerAdmin(admin.ModelAdmin):
    list_display = (
        'match',
        'start_time',
        'extra_time_first_half',    
        'extra_time_full_time', 
        'match_ended', 
        # 'match_status'
    )
    search_fields = ('match__id',)  # Search by match id
    list_filter = ('match_ended',)  # Filter by match end status and start time
    readonly_fields = ('match_status',)  # Make match status read-only as it's calculated

    # Optionally, you can add inlines for related models, if there are any like `pause_resume_sessions`
    # inlines = [PauseResumeSessionInline]

# Register the model and admin class
@admin.register(Substitution)
class SubstitutionAdmin(admin.ModelAdmin):
    list_display = ('match', 'player_out', 'player_in', 'time', 'is_emergency_substitution', 'created_at', 'updated_at')
    # list_filter = ('is_emergency_substitution', 'created_at', 'updated_at')
    search_fields = ('match__team1__name', 'match__team2__name', 'player_out__name', 'player_in__name')
    ordering = ('-created_at',)


@admin.register(MatchPauseResume)
class MatchPauseResumeAdmin(admin.ModelAdmin):
    list_display = ('match', 'paused_at', 'resumed_at', 'duration_display')
    list_filter = ('paused_at', 'resumed_at')
    search_fields = ('match__team1__name', 'match__team2__name')
    ordering = ('-paused_at',)
    
    def duration_display(self, obj):
        """
        Display the duration in a human-readable format (HH:MM:SS).
        """
        duration = obj.duration()
        total_seconds = duration.total_seconds()
        hours = int(total_seconds // 3600)
        minutes = int((total_seconds % 3600) // 60)
        seconds = int(total_seconds % 60)
        return f'{hours:02d}:{minutes:02d}:{seconds:02d}'
    
    duration_display.short_description = 'Duration (HH:MM:SS)'
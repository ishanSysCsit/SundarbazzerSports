from django.db import models
from datetime import datetime
# Create your models here.

class TeamRequest(models.Model):
    SPORT_TYPES = (
        ('FOOTBALL','Football'),
    )
    name = models.CharField(max_length=255)
    total_players = models.PositiveIntegerField(default=10)
    sports_genere = models.CharField(max_length=25,choices=SPORT_TYPES,default='FOOTBALL')
    email = models.EmailField(max_length=100,unique=True,null=True,blank=True)
    address=models.CharField(max_length=255,blank=True,null=True)
    created_at = models.DateField(auto_now_add=True)


    def __str__(self) -> str:
        return f'{self.name}'
    
class Team(models.Model):
    name = models.CharField(max_length=255, blank=True)
    total_players = models.PositiveIntegerField(blank=True, null=True)
    sports_genere = models.CharField(max_length=25, blank=True)
    email = models.EmailField(max_length=100,unique=True,null=True,blank=True)
    address = models.CharField(max_length=255,blank=True,null=True)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateField(blank=True, null=True)

    def __str__(self) -> str:
        return f'{self.name}'


    


class PointTable(models.Model):
    PENDING = 'Pending'
    STATUS_CHOICES = (
        ('PENDING','Pending'),
        ('IN_MATCH','In Match'),
        ('ELIMINATED','Eliminated')
    )
    team = models.ForeignKey(Team,on_delete=models.CASCADE)
    points = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=20,choices = STATUS_CHOICES,default='PENDING')



class TieSheet(models.Model):
    team1 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team1')
    team2 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team2')
    match_date = models.DateField()
    place = models.CharField(max_length=255)
    match_complete = models.BooleanField(default=False)

    def match_day(self):
        day_of_week = self.match_date.strftime('%A')
        return day_of_week
    
    def __str__(self) -> str:
        return f"{self.team1.team_code} vs {self.team2.team_code}"
    

class MatchStatus(models.Model):
    game = models.ForeignKey(TieSheet,on_delete=models.CASCADE,null=True,blank=True)
    team1_point = models.PositiveIntegerField(default=0)
    team2_point = models.PositiveIntegerField(default=0)
    winner = models.ForeignKey(Team,on_delete=models.SET_NULL,null=True,blank=True,related_name='won_match')

    
    def calc_winner(self):
        team1_score = self.team1_point
        team2_score = self.team2_point

        if team1_score > team2_score:
            self.winner = self.game.team1
        elif team2_score > team1_score:
            self.winner = self.game.team2
        else:
            self.winner = None

        return self.winner
    

    def save(self, *args, **kwargs):
        self.calc_winner()  # Calculate the winner before saving
        super().save(*args, **kwargs)  # Call the original save method to save the object

    def __str__(self) -> str:
        return f"{self.winner} is the Winner of the Match of date:{self.game.match_date}"




# Recent Events

class RecentEvents(models.Model):
    SPORT_TYPES = (
        ('NATIONAL','National'),
        ('FOOTBALL','Football'),
        ('VOLLEYBALL','Volleyball'),
        ('TENNIS','Tennis'),
        ('GLOBAL','Global'),
        ('CIRCKET','Circket')
    )
    date = models.DateField()
    event_title= models.CharField(max_length=255)
    event_description = models.TextField()
    sport_type = models.CharField(max_length=25,choices=SPORT_TYPES,default='NATIONAL')


    def __str__(self) -> str:
        return self.event_title
    


class LatestNews(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    is_active = models.BooleanField()
    image = models.ImageField(upload_to="images/")
    text = models.TextField()
    created_at= models.DateField(auto_now_add=True,blank=True,null=True)

    def __str__(self) -> str:
        return ' '.join(self.text.split()[:10])
    
    def sm_text(self):
        return " ".join(self.text.split()[:10])
    

class Player(models.Model):
    BLOOD_GROUPS = (
    ('A+', 'A+'),
    ('A-', 'A-'),
    ('B+', 'B+'),
    ('B-', 'B-'),
    ('AB+', 'AB+'),
    ('AB-', 'AB-'),
    ('O+', 'O+'),
    ('O-', 'O-')
    )
    team = models.ForeignKey(Team,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    jersey_no = models.PositiveIntegerField()
    age = models.PositiveIntegerField()
    weight = models.PositiveIntegerField()
    # height stored in cm
    height = models.PositiveIntegerField()
    blood_group = models.CharField(max_length=25,choices=BLOOD_GROUPS)
    address = models.TextField()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['team', 'jersey_no'], name='unique_jersey_no_per_team')
        ]
    def __str__(self):
        return f"{self.name} ({self.jersey_no}) - {self.team}"
from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelTests(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Test Team')
        self.user = User.objects.create(email='test@example.com', name='Test User', team=self.team)
        self.activity = Activity.objects.create(user=self.user, type='run', duration=30)
        self.workout = Workout.objects.create(user=self.user, description='Test Workout', duration=45)
        self.leaderboard = Leaderboard.objects.create(user=self.user, score=100)

    def test_user_creation(self):
        self.assertEqual(self.user.email, 'test@example.com')
        self.assertEqual(self.user.team.name, 'Test Team')

    def test_activity_creation(self):
        self.assertEqual(self.activity.type, 'run')
        self.assertEqual(self.activity.duration, 30)

    def test_workout_creation(self):
        self.assertEqual(self.workout.description, 'Test Workout')
        self.assertEqual(self.workout.duration, 45)

    def test_leaderboard_creation(self):
        self.assertEqual(self.leaderboard.score, 100)

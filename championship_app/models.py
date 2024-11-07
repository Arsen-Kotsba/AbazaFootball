from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()


# Модель для команд
class Team(db.Model):
    __tablename__ = 'teams'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    logo = db.Column(db.String(200), nullable=True)  # Путь к логотипу команды
    matches_played = db.Column(db.Integer, default=0)
    wins = db.Column(db.Integer, default=0)
    draws = db.Column(db.Integer, default=0)
    losses = db.Column(db.Integer, default=0)
    goals_scored = db.Column(db.Integer, default=0)
    goals_conceded = db.Column(db.Integer, default=0)
    points = db.Column(db.Integer, default=0)

    players = db.relationship('Player', backref='team', lazy=True)
    home_matches = db.relationship('Match', foreign_keys='Match.home_team_id', backref='home_team', lazy=True)
    away_matches = db.relationship('Match', foreign_keys='Match.away_team_id', backref='away_team', lazy=True)


# Модель для игроков
class Player(db.Model):
    __tablename__ = 'players'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    position = db.Column(db.String(50))
    goals_scored = db.Column(db.Integer, default=0)
    team_id = db.Column(db.Integer, db.ForeignKey('teams.id'), nullable=False)


# Модель для матчей
class Match(db.Model):
    __tablename__ = 'matches'

    id = db.Column(db.Integer, primary_key=True)
    home_team_id = db.Column(db.Integer, db.ForeignKey('teams.id'), nullable=False)
    away_team_id = db.Column(db.Integer, db.ForeignKey('teams.id'), nullable=False)
    home_team_score = db.Column(db.Integer, default=0)
    away_team_score = db.Column(db.Integer, default=0)
    match_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    scorers = db.relationship('Goal', backref='match', lazy=True)
    fouls = db.relationship('Foul', backref='match', lazy=True)


# Модель для голов
class Goal(db.Model):
    __tablename__ = 'goals'

    id = db.Column(db.Integer, primary_key=True)
    player_id = db.Column(db.Integer, db.ForeignKey('players.id'), nullable=False)
    match_id = db.Column(db.Integer, db.ForeignKey('matches.id'), nullable=False)
    time_scored = db.Column(db.String(5))  # Минуты или часы, когда был забит гол


# Модель для нарушений
class Foul(db.Model):
    __tablename__ = 'fouls'

    id = db.Column(db.Integer, primary_key=True)
    player_id = db.Column(db.Integer, db.ForeignKey('players.id'), nullable=False)
    match_id = db.Column(db.Integer, db.ForeignKey('matches.id'), nullable=False)
    card = db.Column(db.String(10))  # "Yellow" или "Red" для типа карточки


# Модель для пользователей
class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)  # Флаг, определяющий, является ли пользователь администратором


# Модель для комментариев
class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    match_id = db.Column(db.Integer, db.ForeignKey('matches.id'), nullable=False)

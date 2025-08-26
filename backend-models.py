from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

db = SQLAlchemy()

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    senha_hash = db.Column(db.String(255), nullable=False)
    cargo = db.Column(db.String(100))
    departamento = db.Column(db.String(100))
    role = db.Column(db.String(20), default='user')
    data_criacao = db.Column(db.DateTime, default=datetime.utcnow)
    ativo = db.Column(db.Boolean, default=True)
    
    def set_password(self, senha):
        self.senha_hash = generate_password_hash(senha)
    
    def check_password(self, senha):
        return check_password_hash(self.senha_hash, senha)
    
    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'email': self.email,
            'cargo': self.cargo,
            'departamento': self.departamento,
            'role': self.role,
            'data_criacao': self.data_criacao.isoformat(),
            'ativo': self.ativo
        }

class Pergunta(db.Model):
    __tablename__ = 'perguntas'
    
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    texto = db.Column(db.Text, nullable=False)
    contexto = db.Column(db.Text)
    categoria = db.Column(db.String(50))
    data_criacao = db.Column(db.DateTime, default=datetime.utcnow)
    
    usuario = db.relationship('Usuario', backref='perguntas')
    respostas = db.relationship('Resposta', backref='pergunta', cascade='all, delete-orphan')

class Resposta(db.Model):
    __tablename__ = 'respostas'
    
    id = db.Column(db.Integer, primary_key=True)
    pergunta_id = db.Column(db.Integer, db.ForeignKey('perguntas.id'), nullable=False)
    texto = db.Column(db.Text, nullable=False)
    modelo_usado = db.Column(db.String(50))
    tempo_resposta = db.Column(db.Float)
    avaliacao = db.Column(db.Integer)
    feedback = db.Column(db.Text)
    data_criacao = db.Column(db.DateTime, default=datetime.utcnow)

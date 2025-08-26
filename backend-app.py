from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flask_migrate import Migrate
import os
from datetime import datetime

# Inicializar extensões
db = SQLAlchemy( )
jwt = JWTManager()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    
    # Configurações
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
        'DATABASE_URL', 
        'postgresql://provai_user:provai_pass_2024@localhost:5432/provai_db'
    )
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'sua-chave-secreta')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = False
    
    # Inicializar extensões
    db.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db)
    CORS(app, origins=["http://localhost:3000"] )
    
    # Importar modelos
    from models import Usuario, Pergunta, Resposta
    
    # Registrar blueprints
    from routes.auth import auth_bp
    from routes.chatbot import chatbot_bp
    from routes.admin import admin_bp
    
    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(chatbot_bp, url_prefix='/api/chatbot')
    app.register_blueprint(admin_bp, url_prefix='/api/admin')
    
    # Rota de health check
    @app.route('/api/health')
    def health_check():
        return jsonify({
            'status': 'healthy',
            'timestamp': datetime.utcnow().isoformat(),
            'version': '1.0.0'
        })
    
    # Criar tabelas
    with app.app_context():
        db.create_all()
        
        # Criar usuário admin padrão
        admin = Usuario.query.filter_by(email='provai.admin@provider-it.com.br').first()
        if not admin:
            admin = Usuario(
                nome='Administrador ProvAI',
                email='provai.admin@provider-it.com.br',
                cargo='Administrador do Sistema',
                departamento='TI',
                role='admin'
            )
            admin.set_password('admin123')
            db.session.add(admin)
            db.session.commit()
            print("✅ Usuário admin criado: provai.admin@provider-it.com.br / admin123")
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=5000)

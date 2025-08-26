.PHONY: help setup dev build up down logs clean install-models

help:
	@echo "ProvAI - Comandos Disponíveis:"
	@echo "  setup          - Configura o ambiente"
	@echo "  dev            - Inicia desenvolvimento"
	@echo "  build          - Constrói as imagens"
	@echo "  up             - Inicia os serviços"
	@echo "  down           - Para os serviços"
	@echo "  logs           - Mostra logs"
	@echo "  install-models - Instala modelos SLM"
	@echo "  clean          - Limpa o ambiente"

setup:
	@echo "🚀 Configurando ProvAI..."
	@mkdir -p backups logs
	@echo "✅ Ambiente configurado!"

dev:
	@echo "🚀 Iniciando desenvolvimento..."
	@docker-compose up -d --build
	@echo "✅ Serviços iniciados!"
	@echo "Frontend: http://localhost:3000"
	@echo "Backend: http://localhost:5000"
	@echo "Ollama: http://localhost:11434"

build:
	@echo "🔨 Construindo imagens..."
	@docker-compose build

up:
	@echo "▶️ Iniciando serviços..."
	@docker-compose up -d

down:
	@echo "⏹️ Parando serviços..."
	@docker-compose down

logs:
	@docker-compose logs -f

install-models:
	@echo "📦 Instalando modelos SLM..."
	@docker-compose exec provai_ollama ollama pull codellama:7b
	@docker-compose exec provai_ollama ollama pull mistral:7b
	@docker-compose exec provai_ollama ollama pull llama3.1:8b
	@docker-compose exec provai_ollama ollama pull phi3:mini
	@echo "✅ Modelos instalados!"

clean:
	@echo "🧹 Limpando ambiente..."
	@docker-compose down -v --remove-orphans
	@docker system prune -f
	@echo "✅ Limpeza concluída!"

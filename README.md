# ProvAI - Assistente Técnico Inteligente

![ProvAI](https://img.shields.io/badge/ProvAI-v1.0.0-blue )
![License](https://img.shields.io/badge/license-MIT-green )
![Docker](https://img.shields.io/badge/docker-ready-blue )

**Sua IA especializada em desenvolvimento, construída com Small Language Models (SLMs) para garantir privacidade, performance e controle total.**

## 🚀 Características Principais

- 🧠 **4 Modelos SLM Especializados** - CodeLlama, Mistral, Llama 3.1, Phi-3
- 🔒 **100% Privado** - Processamento local, dados nunca saem da sua infraestrutura
- 💰 **Custo Zero de API** - Sem custos recorrentes após investimento inicial
- ⚡ **Alta Performance** - Respostas rápidas com cache inteligente
- 🎨 **Interface Moderna** - React com temas claro/escuro
- 👑 **Painel Admin** - Gestão completa de usuários e estatísticas

## 🛠️ Stack Tecnológico

| Componente | Tecnologia |
|------------|------------|
| **Frontend** | React, Vite, Tailwind CSS |
| **Backend** | Flask, Python, SQLAlchemy |
| **Banco de Dados** | PostgreSQL |
| **IA** | Ollama, SLMs |
| **Cache** | Redis |
| **Containerização** | Docker, Docker Compose |

## 🚀 Instalação Rápida

### Pré-requisitos
- Docker e Docker Compose
- Git

### Passos
```bash
# 1. Clonar o repositório
git clone https://github.com/Cesar-Salema/ProvAI.git
cd ProvAI

# 2. Configurar ambiente
make setup

# 3. Iniciar serviços
make dev

# 4. Instalar modelos IA
make install-models

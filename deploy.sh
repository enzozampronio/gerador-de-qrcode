#!/bin/bash

# Script de Deploy Automático para VPS
# Este script deve ser executado na sua VPS do Digital Ocean

set -e  # Parar em caso de erro

PROJECT_NAME="gerador-de-qrcode"
PROJECT_PATH="/var/www/gerador-qrcode"  # Ajuste conforme necessário
REPO_URL="https://github.com/enzozampronio/gerador-de-qrcode.git"
PYTHON_VERSION="python3"

echo "🚀 Iniciando deploy do $PROJECT_NAME..."

# 1. Criar diretório do projeto se não existir
if [ ! -d "$PROJECT_PATH" ]; then
    echo "📁 Criando diretório do projeto..."
    sudo mkdir -p $PROJECT_PATH
    sudo chown -R $USER:$USER $PROJECT_PATH
fi

# 2. Clonar ou atualizar repositório
if [ -d "$PROJECT_PATH/.git" ]; then
    echo "📥 Atualizando código..."
    cd $PROJECT_PATH
    git pull origin main
else
    echo "📥 Clonando repositório..."
    git clone $REPO_URL $PROJECT_PATH
    cd $PROJECT_PATH
fi

# 3. Configurar ambiente virtual Python
if [ ! -d "venv" ]; then
    echo "🐍 Criando ambiente virtual Python..."
    $PYTHON_VERSION -m venv venv
fi

echo "📦 Instalando dependências..."
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

# 4. Configurar permissões
echo "🔐 Configurando permissões..."
sudo chown -R www-data:www-data $PROJECT_PATH 2>/dev/null || true
sudo chmod -R 755 $PROJECT_PATH

echo "✅ Deploy concluído com sucesso!"
echo "📍 Projeto instalado em: $PROJECT_PATH"

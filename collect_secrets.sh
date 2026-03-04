#!/bin/bash
# Script para coletar informações para GitHub Secrets
# Execute este script na sua VPS do Digital Ocean

echo "======================================"
echo "📋 COLETANDO INFORMAÇÕES PARA GITHUB"
echo "======================================"
echo ""

# 1. VPS_HOST (IP da VPS)
echo "1️⃣ VPS_HOST (IP da sua VPS):"
echo "-----------------------------------"
# Tentar obter IP público
IP=$(curl -s ifconfig.me 2>/dev/null || curl -s ipinfo.io/ip 2>/dev/null || hostname -I | awk '{print $1}')
echo "   $IP"
echo ""
echo "   👉 Copie este IP para o secret VPS_HOST"
echo ""

# 2. VPS_USERNAME (usuário atual)
echo "2️⃣ VPS_USERNAME (usuário SSH):"
echo "-----------------------------------"
USERNAME=$(whoami)
echo "   $USERNAME"
echo ""
echo "   👉 Copie este usuário para o secret VPS_USERNAME"
echo ""

# 3. VPS_PORT (porta SSH)
echo "3️⃣ VPS_PORT (porta SSH):"
echo "-----------------------------------"
SSH_PORT=$(sudo grep -E "^Port " /etc/ssh/sshd_config 2>/dev/null | awk '{print $2}')
if [ -z "$SSH_PORT" ]; then
    SSH_PORT="22"
fi
echo "   $SSH_PORT"
echo ""
echo "   👉 Copie esta porta para o secret VPS_PORT"
echo ""

# 4. VPS_PROJECT_PATH (caminho do projeto)
echo "4️⃣ VPS_PROJECT_PATH (caminho do projeto):"
echo "-----------------------------------"
PROJECT_PATH="/var/www/gerador-qrcode"
echo "   $PROJECT_PATH"
echo ""
echo "   👉 Copie este caminho para o secret VPS_PROJECT_PATH"
echo ""

# 5. VPS_SSH_KEY (chave privada SSH)
echo "5️⃣ VPS_SSH_KEY (chave privada SSH):"
echo "-----------------------------------"
echo ""

# Verificar se já existe chave SSH
if [ -f ~/.ssh/id_rsa ]; then
    echo "   ✅ Chave SSH encontrada!"
    echo ""
    echo "   Executando: cat ~/.ssh/id_rsa"
    echo ""
    echo "   ⚠️  ATENÇÃO: Esta chave é PRIVADA e CONFIDENCIAL!"
    echo "   Copie TODO o conteúdo (incluindo BEGIN e END)"
    echo ""
    echo "------- INÍCIO DA CHAVE (copie daqui) -------"
    cat ~/.ssh/id_rsa
    echo "------- FIM DA CHAVE (até aqui) -------"
else
    echo "   ⚠️  Nenhuma chave SSH encontrada!"
    echo ""
    echo "   Gerando nova chave SSH..."
    ssh-keygen -t rsa -b 4096 -f ~/.ssh/id_rsa -N "" -C "github-actions@deploy"
    echo ""
    echo "   ✅ Chave gerada com sucesso!"
    echo ""
    echo "------- INÍCIO DA CHAVE (copie daqui) -------"
    cat ~/.ssh/id_rsa
    echo "------- FIM DA CHAVE (até aqui) -------"
fi

echo ""
echo ""
echo "======================================"
echo "📝 RESUMO DOS SECRETS"
echo "======================================"
echo ""
echo "Adicione estes valores no GitHub em:"
echo "https://github.com/enzozampronio/gerador-de-qrcode/settings/secrets/actions"
echo ""
echo "Secret Name         | Value"
echo "------------------- | --------------------------------"
echo "VPS_HOST            | $IP"
echo "VPS_USERNAME        | $USERNAME"
echo "VPS_PORT            | $SSH_PORT"
echo "VPS_PROJECT_PATH    | $PROJECT_PATH"
echo "VPS_SSH_KEY         | (chave privada mostrada acima)"
echo ""
echo "======================================"
echo "✅ Coleta concluída!"
echo "======================================"

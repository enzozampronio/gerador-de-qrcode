# 🚀 GUIA RÁPIDO - Deploy no seu VPS
## IP: 129.212.190.91

---

## PASSO 1: Conectar na VPS

No seu computador, execute:
```powershell
ssh root@129.212.190.91
```

**Se pedir senha:** Digite a senha do root que você definiu no Digital Ocean

**Se der erro "connection refused":** Aguarde alguns minutos, a VPS pode estar iniciando

---

## PASSO 2: Copiar e Executar (NA VPS)

Depois de conectado na VPS, **copie e cole este comando completo**:

```bash
curl -sSL https://raw.githubusercontent.com/enzozampronio/gerador-de-qrcode/master/collect_secrets.sh -o /tmp/setup.sh 2>/dev/null || cat > /tmp/setup.sh << 'SCRIPTEND'
#!/bin/bash
clear
echo "======================================"
echo "🚀 SETUP AUTOMÁTICO - VPS"
echo "======================================"
echo ""
echo "Este script vai:"
echo "1. Coletar informações para GitHub"
echo "2. Instalar dependências necessárias"
echo "3. Preparar ambiente"
echo ""
read -p "Pressione ENTER para continuar..."

# Atualizar sistema
echo ""
echo "📦 Atualizando sistema..."
apt-get update -qq

# Instalar dependências básicas
echo "📦 Instalando dependências..."
apt-get install -y git python3 python3-pip python3-venv nginx curl wget -qq

echo ""
echo "======================================"
echo "📋 INFORMAÇÕES PARA GITHUB SECRETS"
echo "======================================"
echo ""

echo "✅ 1. VPS_HOST (copie este IP):"
echo "   129.212.190.91"
echo ""

echo "✅ 2. VPS_USERNAME (copie este usuário):"
echo "   $(whoami)"
echo ""

echo "✅ 3. VPS_PORT (copie esta porta):"
SSH_PORT=$(grep -E "^Port " /etc/ssh/sshd_config 2>/dev/null | awk '{print $2}')
if [ -z "$SSH_PORT" ]; then
    echo "   22"
else
    echo "   $SSH_PORT"
fi
echo ""

echo "✅ 4. VPS_PROJECT_PATH (copie este caminho):"
echo "   /var/www/gerador-qrcode"
echo ""

echo "✅ 5. VPS_SSH_KEY (copie TUDO entre as linhas):"
echo ""
echo "========== INÍCIO DA CHAVE (copie daqui) =========="

# Gerar chave se não existir
if [ ! -f ~/.ssh/id_rsa ]; then
    echo "Gerando chave SSH..."
    ssh-keygen -t rsa -b 4096 -f ~/.ssh/id_rsa -N "" -C "github-actions@deploy" -q
fi

cat ~/.ssh/id_rsa

echo "========== FIM DA CHAVE (até aqui) =========="
echo ""
echo ""

# Criar diretório do projeto
echo "📁 Criando diretório do projeto..."
mkdir -p /var/www/gerador-qrcode
cd /var/www/gerador-qrcode

echo ""
echo "======================================"
echo "✅ SETUP CONCLUÍDO!"
echo "======================================"
echo ""
echo "📝 PRÓXIMOS PASSOS:"
echo ""
echo "1. Copie as 5 informações acima"
echo "2. Vá em: https://github.com/enzozampronio/gerador-de-qrcode/settings/secrets/actions"
echo "3. Adicione cada secret (VPS_HOST, VPS_USERNAME, etc)"
echo "4. Faça um push no GitHub para testar o deploy"
echo ""
echo "💡 DICA: A chave SSH é a mais importante!"
echo "   Copie desde -----BEGIN até -----END"
echo ""
SCRIPTEND

chmod +x /tmp/setup.sh && bash /tmp/setup.sh
```

**⚠️ IMPORTANTE:** Copie e cole o comando COMPLETO de uma vez só!

---

## PASSO 3: Copiar as Informações

Após executar, você verá algo assim:

```
✅ 1. VPS_HOST: 129.212.190.91
✅ 2. VPS_USERNAME: root  
✅ 3. VPS_PORT: 22
✅ 4. VPS_PROJECT_PATH: /var/www/gerador-qrcode
✅ 5. VPS_SSH_KEY:
========== INÍCIO DA CHAVE ==========
-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEA... (várias linhas)
-----END RSA PRIVATE KEY-----
========== FIM DA CHAVE ==========
```

**COPIE** essas 5 informações!

---

## PASSO 4: Adicionar Secrets no GitHub

1. Abra no navegador: https://github.com/enzozampronio/gerador-de-qrcode/settings/secrets/actions

2. Clique em **"New repository secret"** para cada um:

### Secret 1:
- **Name:** `VPS_HOST`
- **Value:** `129.212.190.91`

### Secret 2:
- **Name:** `VPS_USERNAME`  
- **Value:** `root` (ou o que aparecer)

### Secret 3:
- **Name:** `VPS_PORT`
- **Value:** `22`

### Secret 4:
- **Name:** `VPS_PROJECT_PATH`
- **Value:** `/var/www/gerador-qrcode`

### Secret 5 (MAIS IMPORTANTE):
- **Name:** `VPS_SSH_KEY`
- **Value:** Cole a chave COMPLETA, incluindo:
  ```
  -----BEGIN RSA PRIVATE KEY-----
  ... todo o conteúdo ...
  -----END RSA PRIVATE KEY-----
  ```

---

## PASSO 5: Testar Deploy

Depois de adicionar os secrets, faça um push:

```powershell
cd "G:\Meu Drive\VS_code_github\gerador de qrcode"
git add .
git commit -m "test: testando deploy automático" --allow-empty
git push
```

Acompanhe em: https://github.com/enzozampronio/gerador-de-qrcode/actions

---

## 🆘 Problemas Comuns

### Não consigo conectar no SSH
```powershell
# Tente com -v para ver detalhes
ssh -v root@129.212.190.91
```

### "Permission denied"
- Verifique se está usando a senha correta
- Ou use chave SSH do Digital Ocean

### Script não executa
- Copie linha por linha
- Ou salve num arquivo .sh e execute

---

## ✅ Checklist

- [ ] Conectei na VPS via SSH
- [ ] Executei o script de setup
- [ ] Copiei as 5 informações
- [ ] Adicionei os 5 secrets no GitHub
- [ ] Fiz o push de teste

---

**Qualquer dúvida, me avise em qual passo está travado!** 🚀

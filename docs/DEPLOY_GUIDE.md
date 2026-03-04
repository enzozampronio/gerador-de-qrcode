# 🚀 Guia Completo: Deploy Automático no Digital Ocean

Este guia mostra como configurar deploy automático da sua aplicação QR Code para uma VPS do Digital Ocean usando GitHub Actions.

---

## 📋 Pré-requisitos

- ✅ VPS do Digital Ocean ativa
- ✅ Domínio apontando para a VPS (opcional, mas recomendado)
- ✅ SSH configurado na VPS
- ✅ Git instalado na VPS
- ✅ Python 3.7+ instalado na VPS
- ✅ Nginx ou Apache instalado na VPS

---

## 🔧 Parte 1: Configurar VPS (Digital Ocean)

### 1. Conectar na VPS via SSH

```bash
ssh root@seu-ip-da-vps
```

### 2. Instalar Dependências

```bash
# Atualizar sistema
sudo apt update && sudo apt upgrade -y

# Instalar Python, pip, git, nginx
sudo apt install python3 python3-pip python3-venv git nginx curl -y

# Verificar instalações
python3 --version
git --version
nginx -v
```

### 3. Criar Usuário para Deploy (Recomendado)

```bash
# Criar usuário
sudo adduser deploy
sudo usermod -aG sudo deploy

# Configurar SSH para usuário
sudo mkdir -p /home/deploy/.ssh
sudo cp ~/.ssh/authorized_keys /home/deploy/.ssh/ 2>/dev/null || true
sudo chown -R deploy:deploy /home/deploy/.ssh
sudo chmod 700 /home/deploy/.ssh
sudo chmod 600 /home/deploy/.ssh/authorized_keys 2>/dev/null || true
```

### 4. Executar Setup Inicial

```bash
# Logar como usuário deploy
su - deploy

# Criar diretório do projeto
sudo mkdir -p /var/www/gerador-qrcode
sudo chown -R deploy:deploy /var/www/gerador-qrcode

# Clonar repositório
git clone https://github.com/enzozampronio/gerador-de-qrcode.git /var/www/gerador-qrcode

# Configurar ambiente Python
cd /var/www/gerador-qrcode
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 5. Configurar Nginx

```bash
# Copiar configuração do Nginx
sudo cp nginx.conf /etc/nginx/sites-available/qrcode

# Editar arquivo (ajustar domínio)
sudo nano /etc/nginx/sites-available/qrcode
# Altere: server_name seu-dominio.com www.seu-dominio.com;

# Ativar site
sudo ln -s /etc/nginx/sites-available/qrcode /etc/nginx/sites-enabled/

# Testar configuração
sudo nginx -t

# Reiniciar Nginx
sudo systemctl restart nginx
```

### 6. Configurar Firewall

```bash
# Permitir HTTP e HTTPS
sudo ufw allow 'Nginx Full'
sudo ufw allow OpenSSH
sudo ufw enable
```

### 7. (Opcional) Configurar SSL com Let's Encrypt

```bash
# Instalar Certbot
sudo apt install certbot python3-certbot-nginx -y

# Obter certificado SSL
sudo certbot --nginx -d seu-dominio.com -d www.seu-dominio.com

# Renovação automática já está configurada
```

---

## 🔑 Parte 2: Configurar GitHub Secrets

### 1. Gerar Chave SSH (se necessário)

Na sua VPS:

```bash
# Ver chave pública existente
cat ~/.ssh/id_rsa 2>/dev/null || ssh-keygen -t rsa -b 4096 -C "deploy@seu-dominio.com" -N ""

# Copiar chave privada (para GitHub Secret)
cat ~/.ssh/id_rsa
```

### 2. Adicionar Secrets no GitHub

Acesse: https://github.com/enzozampronio/gerador-de-qrcode/settings/secrets/actions

Clique em "New repository secret" e adicione:

| Nome | Valor | Descrição |
|------|-------|-----------|
| `VPS_HOST` | `123.456.789.012` | IP da sua VPS |
| `VPS_USERNAME` | `deploy` | Usuário SSH (deploy ou root) |
| `VPS_SSH_KEY` | `-----BEGIN RSA...` | Chave privada SSH (conteúdo completo do id_rsa) |
| `VPS_PORT` | `22` | Porta SSH (geralmente 22) |
| `VPS_PROJECT_PATH` | `/var/www/gerador-qrcode` | Caminho do projeto na VPS |

**⚠️ IMPORTANTE:** A chave SSH deve incluir as linhas completas, incluindo:
```
-----BEGIN RSA PRIVATE KEY-----
... conteúdo ...
-----END RSA PRIVATE KEY-----
```

---

## 🚀 Parte 3: Testar Deploy

### 1. Fazer Commit e Push

```powershell
# No seu computador local
cd "G:\Meu Drive\VS_code_github\gerador de qrcode"

git add .
git commit -m "feat: adiciona GitHub Actions para deploy automático"
git push origin main
```

### 2. Acompanhar Deploy

1. Acesse: https://github.com/enzozampronio/gerador-de-qrcode/actions
2. Clique no workflow "Deploy to DigitalOcean VPS"
3. Acompanhe os logs em tempo real

### 3. Verificar Deploy na VPS

```bash
# Conectar na VPS
ssh deploy@seu-ip-da-vps

# Verificar arquivos
cd /var/www/gerador-qrcode
ls -la
git log -1
```

### 4. Acessar Site

Abra no navegador:
- `http://seu-ip-da-vps` ou
- `http://seu-dominio.com`

Você deve ver a interface web do gerador de QR Code!

---

## 🔄 Fluxo de Deploy Automático

Agora, toda vez que você fizer push:

```powershell
# Fazer alterações
git add .
git commit -m "feat: nova funcionalidade"
git push
```

O GitHub Actions automaticamente:
1. ✅ Detecta o push
2. ✅ Conecta na VPS via SSH
3. ✅ Faz git pull
4. ✅ Atualiza dependências
5. ✅ Reinicia serviços
6. ✅ Aplicação atualizada em produção!

---

## 🛡️ Segurança

### Recomendações Importantes:

1. **SSH Key-based Authentication**
   ```bash
   # Na VPS, desabilitar senha SSH
   sudo nano /etc/ssh/sshd_config
   # PasswordAuthentication no
   sudo systemctl restart sshd
   ```

2. **Fail2Ban (Proteção contra ataques)**
   ```bash
   sudo apt install fail2ban -y
   sudo systemctl enable fail2ban
   sudo systemctl start fail2ban
   ```

3. **Firewall Restritivo**
   ```bash
   sudo ufw default deny incoming
   sudo ufw default allow outgoing
   sudo ufw allow 22/tcp   # SSH
   sudo ufw allow 80/tcp   # HTTP
   sudo ufw allow 443/tcp  # HTTPS
   sudo ufw enable
   ```

4. **Manter Sistema Atualizado**
   ```bash
   # Criar cron job para atualizações automáticas
   sudo apt install unattended-upgrades -y
   sudo dpkg-reconfigure --priority=low unattended-upgrades
   ```

---

## 🐛 Solução de Problemas

### Deploy falha com "Permission denied"
```bash
# Na VPS, ajustar permissões
sudo chown -R deploy:deploy /var/www/gerador-qrcode
chmod +x deploy.sh
```

### Erro "Host key verification failed"
Adicione o host conhecido:
```bash
ssh-keyscan -H seu-ip-da-vps >> ~/.ssh/known_hosts
```

### Nginx retorna 403 Forbidden
```bash
# Verificar permissões dos arquivos
sudo chmod -R 755 /var/www/gerador-qrcode
sudo chown -R www-data:www-data /var/www/gerador-qrcode
```

### Site não carrega
```bash
# Verificar status do Nginx
sudo systemctl status nginx

# Ver logs de erro
sudo tail -f /var/log/nginx/error.log

# Testar configuração
sudo nginx -t
```

---

## 📊 Monitoramento

### Verificar Logs da Aplicação

```bash
# Logs do Nginx
sudo tail -f /var/log/nginx/qrcode-access.log
sudo tail -f /var/log/nginx/qrcode-error.log

# Logs do sistema
journalctl -u nginx -f
```

### Verificar Uso de Recursos

```bash
# Ver uso de CPU/Memória
htop

# Ver espaço em disco
df -h

# Ver processos Python
ps aux | grep python
```

---

## 🔧 Configurações Avançadas

### Deploy com Ambiente Staging

Crie branch `staging` e adicione workflow separado em `.github/workflows/deploy-staging.yml`

### Notificações no Discord/Slack

Adicione ao workflow:
```yaml
- name: Notify Slack
  if: always()
  uses: 8398a7/action-slack@v3
  with:
    status: ${{ job.status }}
    webhook_url: ${{ secrets.SLACK_WEBHOOK }}
```

### Rollback Automático

Configure tags Git para versões e script de rollback na VPS.

---

## ✅ Checklist de Deploy

Antes de fazer deploy em produção:

- [ ] Secrets configurados no GitHub
- [ ] SSH funcionando na VPS
- [ ] Nginx configurado
- [ ] Firewall configurado
- [ ] SSL configurado (Let's Encrypt)
- [ ] Domínio apontando para VPS
- [ ] Backup da VPS ativo
- [ ] Monitoramento configurado
- [ ] Substituir `[Seu Nome/Empresa]` nos arquivos

---

## 🆘 Suporte

Se encontrar problemas:

1. Verifique os logs do GitHub Actions
2. Conecte na VPS e verifique logs do Nginx
3. Teste comandos manualmente na VPS
4. Verifique firewall e permissões

---

## 🎉 Pronto!

Seu gerador de QR Code está agora com deploy automático configurado!

**Próximos passos:**
- Configurar domínio personalizado
- Adicionar Google Analytics
- Configurar backup automático
- Escalar para múltiplos servidores (se necessário)

**Seu site:** http://seu-dominio.com

**Bom negócio! 🚀💰**

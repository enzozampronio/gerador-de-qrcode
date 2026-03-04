# 🎨 Gerador de QR Code Profissional

Sistema completo para geração de QR Codes personalizados com três interfaces: Desktop (GUI), Web (HTML) e Terminal (CLI).

![License](https://img.shields.io/badge/License-MIT-blue.svg)
![Python](https://img.shields.io/badge/Python-3.7%2B-blue)

---

## 🚀 Demonstração

**🌐 Versão Web:** http://129.212.190.91

---

## ✨ Funcionalidades

- **Interface Web (HTML)**: Design profissional e responsivo, pronto para uso em qualquer navegador
- **Interface Desktop (Tkinter)**: Aplicativo standalone para Windows/Linux/Mac
- **Interface Terminal (CLI)**: Ferramenta interativa para linha de comando
- **Personalização Completa**: Cores, tamanhos, bordas e níveis de correção de erro
- **Exportação PNG**: Download direto das imagens geradas

---

## 📦 Instalação

### Requisitos

- Python 3.7 ou superior
- pip (gerenciador de pacotes Python)

### Instalação das Dependências

```bash
pip install -r requirements.txt
```

---

## 💻 Como Usar

### Versão Web

Abra o arquivo `index.html` diretamente no navegador. Não requer servidor.

### Versão Desktop (GUI)

```bash
python gerar_qrcode_gui.py
```

### Versão Terminal (CLI)

```bash
python gerar_qrcode.py
```

---

## 🚀 Deploy Automático

Este projeto inclui deploy automático via GitHub Actions para VPS do Digital Ocean.

**Guia completo:** [docs/DEPLOY_GUIDE.md](docs/DEPLOY_GUIDE.md)

---

## 💼 Licenciamento e Comercialização

### ✅ Você PODE comercializar este software

Este projeto usa licenças permissivas que **PERMITEM uso comercial**:

| Biblioteca | Licença | Uso Comercial |
|------------|---------|---------------|
| python-qrcode | BSD-3-Clause | ✅ Permitido |
| QRCode.js | MIT | ✅ Permitido |
| Pillow | HPND | ✅ Permitido |

**Documentação completa:** [docs/THIRD_PARTY_LICENSES.txt](docs/THIRD_PARTY_LICENSES.txt)

### 📋 Obrigações Legais

Para comercializar, você deve:
1. Manter os arquivos LICENSE e docs/THIRD_PARTY_LICENSES.txt
2. Não remover avisos de copyright das bibliotecas
3. Substituir `[Seu Nome/Empresa]` no LICENSE pelos seus dados

---

## 📁 Estrutura do Projeto

```
.
├── index.html              # Interface web
├── gerar_qrcode.py         # Interface CLI
├── gerar_qrcode_gui.py     # Interface desktop (GUI)
├── requirements.txt        # Dependências Python
├── LICENSE                 # Licença MIT
├── README.md               # Este arquivo
│
├── docs/                   # Documentação
│   ├── DEPLOY_GUIDE.md     # Guia de deploy completo
│   ├── THIRD_PARTY_LICENSES.txt
│   └── SETUP_VPS_RAPIDO.md
│
├── scripts/                # Scripts auxiliares
│   ├── deploy.sh           # Script de deploy
│   └── collect_secrets.sh  # Coletar secrets da VPS
│
├── config/                 # Arquivos de configuração
│   └── nginx.conf          # Configuração do Nginx
│
└── .github/                # GitHub Actions
    └── workflows/
        └── deploy.yml      # Workflow de deploy automático
```

---

## 🛠️ Tecnologias Utilizadas

- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Backend**: Python 3.7+
- **Bibliotecas**: qrcode, Pillow, Tkinter
- **Deploy**: GitHub Actions, Nginx
- **Hospedagem**: Digital Ocean VPS

---

## 📝 Configurações do QR Code

- **Version**: Tamanho da matriz (1-40, ou automático)
- **Error Correction**: 
  - L: ~7% de recuperação
  - M: ~15% de recuperação (padrão)
  - Q: ~25% de recuperação
  - H: ~30% de recuperação
- **Box Size**: Tamanho de cada módulo em pixels
- **Border**: Espessura da borda em módulos
- **Cores**: Personalizáveis (QR Code e fundo)

---

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para:

1. Fazer fork do projeto
2. Criar uma branch para sua feature (`git checkout -b feature/NovaFuncionalidade`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova funcionalidade'`)
4. Push para a branch (`git push origin feature/NovaFuncionalidade`)
5. Abrir um Pull Request

---

## 📄 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

As bibliotecas de terceiros possuem suas próprias licenças - veja [docs/THIRD_PARTY_LICENSES.txt](docs/THIRD_PARTY_LICENSES.txt).

---

## 👤 Autor

**Enzo Zampronio**

- GitHub: [@enzozampronio](https://github.com/enzozampronio)
- Projeto: [gerador-de-qrcode](https://github.com/enzozampronio/gerador-de-qrcode)

---

## 🙏 Agradecimentos

- [python-qrcode](https://github.com/lincolnloop/python-qrcode) - Biblioteca Python para geração de QR codes
- [QRCode.js](https://github.com/davidshimjs/qrcodejs) - Biblioteca JavaScript para QR codes
- [Pillow](https://github.com/python-pillow/Pillow) - Biblioteca Python para processamento de imagens

---

## 📞 Suporte

Para dúvidas ou problemas:

- Abra uma [Issue](https://github.com/enzozampronio/gerador-de-qrcode/issues)
- Consulte a [Documentação de Deploy](docs/DEPLOY_GUIDE.md)

---

**⭐ Se este projeto foi útil, considere dar uma estrela!**

---

*Desenvolvido com profissionalismo para uso comercial.* 🚀💰

# Gerador de QR Code Profissional

Sistema completo para geração de QR Codes personalizados com interface desktop (GUI) e web (HTML).

## 📋 Funcionalidades

- **Interface Desktop (Tkinter)**: Aplicativo standalone para Windows/Linux/Mac
- **Interface Web (HTML)**: Versão moderna e responsiva para navegadores
- **Personalização Completa**: Cores, tamanhos, bordas e níveis de correção de erro
- **Design Profissional**: Interface limpa e moderna, mobile-friendly
- **Exportação PNG**: Download direto das imagens geradas

## 🚀 Como Usar

### Versão Desktop (GUI)

```bash
# Ativar ambiente virtual
.\venv\Scripts\Activate.ps1

# Executar aplicativo
python gerar_qrcode_gui.py
```

### Versão Web

Abra o arquivo `index.html` diretamente no navegador. Não requer servidor.

### Versão Terminal (CLI)

```bash
python gerar_qrcode.py
```

## 📦 Instalação

### Requisitos

- Python 3.7 ou superior
- pip (gerenciador de pacotes Python)

### Dependências Python

```bash
pip install qrcode[pil] pillow
```

## 💼 Comercialização e Licenciamento

### ✅ VOCÊ PODE COMERCIALIZAR ESTE SOFTWARE

Este software foi desenvolvido para uso comercial e está **100% livre para venda**.

### Licenças Utilizadas

Este projeto usa as seguintes bibliotecas open-source:

| Biblioteca | Licença | Uso Comercial |
|------------|---------|---------------|
| **python-qrcode** | BSD-3-Clause | ✅ Permitido |
| **QRCode.js** | MIT | ✅ Permitido |
| **Pillow** | HPND | ✅ Permitido |

**Todas as licenças permitem:**
- ✅ Uso comercial
- ✅ Modificação
- ✅ Distribuição
- ✅ Venda do software
- ✅ Uso em produtos proprietários

### 📄 Obrigações Legais

Para comercializar este software, você DEVE:

1. **Incluir os avisos de licença**: Mantenha os arquivos `LICENSE` e `THIRD_PARTY_LICENSES.txt` junto com seu software

2. **Dar créditos apropriados**: As bibliotecas usadas devem ser creditadas (já incluído nos arquivos)

3. **Não usar nomes para endosso**: Não use "Lincoln Loop", "davidshimjs" ou nomes dos autores originais para promover seu produto

### ❌ O que você NÃO pode fazer

- ❌ Remover os avisos de copyright das bibliotecas de terceiros
- ❌ Afirmar que você criou as bibliotecas python-qrcode ou QRCode.js
- ❌ Usar nomes dos autores originais para marketing sem permissão

### 💰 Modelos de Negócio Sugeridos

Você pode comercializar este software de várias formas:

1. **Software como Serviço (SaaS)**: Hospedar a versão web e cobrar por uso
2. **Licença Comercial**: Vender licenças do software desktop
3. **White Label**: Personalizar e revender com sua marca
4. **Integração**: Incorporar em outros produtos/serviços
5. **Freemium**: Versão básica grátis, recursos avançados pagos

### 📞 Recomendações Adicionais

Para máxima proteção legal:

1. **Adicione seu próprio copyright**: Substitua `[Seu Nome/Empresa]` no arquivo `LICENSE`
2. **Termos de Uso**: Crie termos de serviço para seus clientes finais
3. **Consulte um advogado**: Para operações de grande escala, consulte um profissional legal

## 🛡️ Garantias

Este software é fornecido "como está", sem garantias. As bibliotecas de terceiros também possuem suas próprias limitações de garantia (ver `THIRD_PARTY_LICENSES.txt`).

## 📚 Documentação Técnica

### Configurações do QR Code

- **Version**: Tamanho da matriz (1-40, ou automático)
- **Error Correction**: 
  - L: ~7% de recuperação
  - M: ~15% de recuperação (padrão)
  - Q: ~25% de recuperação
  - H: ~30% de recuperação
- **Box Size**: Tamanho de cada módulo em pixels
- **Border**: Espessura da borda em módulos

## 🤝 Contribuindo

Este é um projeto proprietário, mas sugestões são bem-vindas.

## 📞 Suporte

Para dúvidas sobre licenciamento, consulte `THIRD_PARTY_LICENSES.txt` ou os repositórios originais:

- python-qrcode: https://github.com/lincolnloop/python-qrcode
- QRCode.js: https://github.com/davidshimjs/qrcodejs

## 📜 Histórico de Versões

### v1.0.0 (2026-03-04)
- Interface desktop (Tkinter)
- Interface web (HTML/CSS/JS)
- Interface terminal (CLI)
- Documentação completa de licenciamento

---

**Nota Legal**: Este README fornece informações gerais sobre licenciamento. Para decisões comerciais importantes, consulte um advogado especializado em propriedade intelectual.

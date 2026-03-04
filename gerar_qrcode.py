#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Gerador de QR Code - Interface Terminal (CLI)

Copyright (c) 2026 [Seu Nome/Empresa]
Licença: MIT (veja LICENSE para detalhes)

Este software utiliza as seguintes bibliotecas de terceiros:
- python-qrcode (BSD-3-Clause) - https://github.com/lincolnloop/python-qrcode

Para informações completas sobre licenciamento, veja THIRD_PARTY_LICENSES.txt
"""

import qrcode
import qrcode.constants
import os


def obter_input_inteiro(mensagem, padrao, minimo=None, maximo=None):
    """Solicita input de número inteiro com validação"""
    while True:
        valor = input(f"{mensagem} (padrão: {padrao}): ").strip()
        if not valor:
            return padrao
        try:
            valor_int = int(valor)
            if minimo is not None and valor_int < minimo:
                print(f"❌ Valor deve ser maior ou igual a {minimo}")
                continue
            if maximo is not None and valor_int > maximo:
                print(f"❌ Valor deve ser menor ou igual a {maximo}")
                continue
            return valor_int
        except ValueError:
            print("❌ Por favor, digite um número válido")


def obter_cor(mensagem, padrao):
    """Solicita input de cor (RGB ou nome)"""
    print(f"\n{mensagem}")
    print("  - Digite uma cor em formato RGB: 255,0,0")
    print("  - Ou nome da cor em inglês: black, white, blue, red, etc.")
    cor = input(f"  (padrão: {padrao}): ").strip()
    
    if not cor:
        return padrao
    
    # Tentar interpretar como RGB
    if "," in cor:
        try:
            r, g, b = map(int, cor.split(","))
            if all(0 <= c <= 255 for c in [r, g, b]):
                return (r, g, b)
            else:
                print("❌ Valores RGB devem estar entre 0 e 255. Usando padrão.")
                return padrao
        except ValueError:
            print("❌ Formato RGB inválido. Usando padrão.")
            return padrao
    
    return cor


def selecionar_correcao_erro():
    """Menu para selecionar nível de correção de erro"""
    print("\n=== Nível de Correção de Erro ===")
    print("1. L - ~7% de correção (QR code menor)")
    print("2. M - ~15% de correção (padrão)")
    print("3. Q - ~25% de correção")
    print("4. H - ~30% de correção (QR code maior)")
    
    opcoes = {
        "1": qrcode.constants.ERROR_CORRECT_L,
        "2": qrcode.constants.ERROR_CORRECT_M,
        "3": qrcode.constants.ERROR_CORRECT_Q,
        "4": qrcode.constants.ERROR_CORRECT_H,
    }
    
    while True:
        escolha = input("Escolha (1-4, padrão: 2): ").strip() or "2"
        if escolha in opcoes:
            return opcoes[escolha]
        print("❌ Opção inválida. Digite um número de 1 a 4.")


def main():
    print("=" * 50)
    print("🎨 GERADOR DE QR CODE PERSONALIZADO 🎨")
    print("=" * 50)
    
    # 1. Obter dados para o QR Code
    dados = input("\n📝 Digite o link ou texto para o QR Code: ").strip()
    if not dados:
        print("❌ Nenhum dado fornecido. Encerrando.")
        return
    
    # 2. Configurações do QR Code
    print("\n" + "=" * 50)
    print("⚙️  CONFIGURAÇÕES DO QR CODE")
    print("=" * 50)
    
    # Version (tamanho da matriz)
    print("\n📏 Version: controla o tamanho do QR Code")
    print("   - 1 = 21x21 (menor)")
    print("   - 40 = 177x177 (maior)")
    print("   - None/0 = automático (recomendado)")
    version_input = obter_input_inteiro("   Digite o version", "auto", 0, 40)
    version = None if version_input == 0 or version_input == "auto" else version_input
    
    # Correção de erro
    error_correction = selecionar_correcao_erro()
    
    # Box size (tamanho de cada quadrado em pixels)
    print("\n📦 Box Size: tamanho de cada quadrado do QR em pixels")
    box_size = obter_input_inteiro("   Digite o box_size", 10, 1, 50)
    
    # Border (espessura da borda)
    print("\n🖼️  Border: espessura da borda (mínimo recomendado: 4)")
    border = obter_input_inteiro("   Digite o border", 4, 0, 20)
    
    # Cores
    print("\n" + "=" * 50)
    print("🎨 CORES DO QR CODE")
    print("=" * 50)
    
    fill_color = obter_cor("🖌️  Cor do QR Code (fill_color)", "black")
    back_color = obter_cor("🎨 Cor de fundo (back_color)", "white")
    
    # Nome do arquivo
    print("\n" + "=" * 50)
    nome_arquivo = input("💾 Nome do arquivo PNG (sem extensão, padrão: qrcode): ").strip()
    if not nome_arquivo:
        nome_arquivo = "qrcode"
    nome_arquivo_completo = f"{nome_arquivo}.png"
    
    # 3. Gerar QR Code
    print("\n" + "=" * 50)
    print("⏳ Gerando QR Code...")
    print("=" * 50)
    
    try:
        qr = qrcode.QRCode(
            version=version,
            error_correction=error_correction,
            box_size=box_size,
            border=border,
        )
        qr.add_data(dados)
        qr.make(fit=True)
        
        img = qr.make_image(fill_color=fill_color, back_color=back_color)
        
        # Caminho absoluto do arquivo gerado
        caminho_completo = os.path.abspath(nome_arquivo_completo)
        img.save(caminho_completo)  # type: ignore[arg-type]
        
        print("\n✅ QR Code gerado com sucesso!")
        print(f"📁 Arquivo: {caminho_completo}")
        print(f"📊 Dados codificados: {dados[:50]}{'...' if len(dados) > 50 else ''}")
        print(f"📏 Version: {qr.version}")
        print(f"📦 Box Size: {box_size}px")
        print(f"🖼️  Border: {border}")
        print(f"🎨 Cores: {fill_color} em fundo {back_color}")
        
    except Exception as e:
        print(f"\n❌ Erro ao gerar QR Code: {e}")


if __name__ == "__main__":
    main()

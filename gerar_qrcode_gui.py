#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Gerador de QR Code - Interface Gráfica (GUI)

Copyright (c) 2026 [Seu Nome/Empresa]
Licença: MIT (veja LICENSE para detalhes)

Este software utiliza as seguintes bibliotecas de terceiros:
- python-qrcode (BSD-3-Clause) - https://github.com/lincolnloop/python-qrcode
- Pillow/PIL (HPND) - https://github.com/python-pillow/Pillow

Para informações completas sobre licenciamento, veja THIRD_PARTY_LICENSES.txt
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox, colorchooser
import qrcode
import qrcode.constants
from PIL import Image, ImageTk
import os


class QRCodeGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerador de QR Code")
        self.root.geometry("900x700")
        self.root.resizable(False, False)
        
        # Configurar cores modernas
        self.bg_color = "#f5f6fa"
        self.primary_color = "#3E4065"
        self.secondary_color = "#3B324C"
        self.accent_color = "#484E4B"
        self.text_color = "#2b2f36"
        
        self.root.configure(bg=self.bg_color)
        
        # Variáveis
        self.qr_image = None
        self.qr_photo = None
        self.fill_color = "#000000"
        self.back_color = "#FFFFFF"
        
        self.setup_ui()
        
    def setup_ui(self):
        """Configura a interface do usuário"""
        
        # Título
        title_frame = tk.Frame(self.root, bg=self.primary_color, height=80)
        title_frame.pack(fill=tk.X)
        title_frame.pack_propagate(False)
        
        title_label = tk.Label(
            title_frame,
            text="Gerador de QR Code",
            font=("Segoe UI", 24, "bold"),
            bg=self.primary_color,
            fg="white"
        )
        title_label.pack(pady=20)
        
        # Container principal
        main_container = tk.Frame(self.root, bg=self.bg_color)
        main_container.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Frame esquerdo - Configurações
        left_frame = tk.Frame(main_container, bg=self.bg_color)
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))
        
        # Frame direito - Preview
        right_frame = tk.Frame(main_container, bg="white", relief=tk.RAISED, bd=2)
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(10, 0))
        
        self.setup_left_panel(left_frame)
        self.setup_right_panel(right_frame)
        
    def create_section(self, parent, title):
        """Cria uma seção com título"""
        section = tk.LabelFrame(
            parent,
            text=title,
            font=("Segoe UI", 11, "bold"),
            bg=self.bg_color,
            fg=self.text_color,
            padx=15,
            pady=10
        )
        section.pack(fill=tk.X, pady=(0, 15))
        return section
        
    def setup_left_panel(self, parent):
        """Configura o painel esquerdo com controles"""
        
        # Seção 1: Dados
        data_section = self.create_section(parent, "Dados do QR Code")
        
        tk.Label(
            data_section,
            text="Link ou Texto:",
            font=("Segoe UI", 10),
            bg=self.bg_color,
            fg=self.text_color
        ).pack(anchor=tk.W)
        
        self.data_entry = tk.Text(
            data_section,
            height=3,
            font=("Segoe UI", 10),
            relief=tk.FLAT,
            bd=1,
            highlightthickness=1,
            highlightbackground="#dfe4ea",
            highlightcolor=self.primary_color
        )
        self.data_entry.pack(fill=tk.X, pady=(5, 0))
        
        # Seção 2: Configurações
        config_section = self.create_section(parent, "Configurações")
        
        # Version
        version_frame = tk.Frame(config_section, bg=self.bg_color)
        version_frame.pack(fill=tk.X, pady=5)
        
        tk.Label(
            version_frame,
            text="Version (1-40, Auto):",
            font=("Segoe UI", 9),
            bg=self.bg_color
        ).pack(side=tk.LEFT)
        
        self.version_var = tk.StringVar(value="Auto")
        version_spinbox = ttk.Spinbox(
            version_frame,
            from_=1,
            to=40,
            textvariable=self.version_var,
            width=10,
            font=("Segoe UI", 9)
        )
        version_spinbox.pack(side=tk.RIGHT)
        version_spinbox.set("Auto")
        
        # Error Correction
        error_frame = tk.Frame(config_section, bg=self.bg_color)
        error_frame.pack(fill=tk.X, pady=5)
        
        tk.Label(
            error_frame,
            text="Correção de Erro:",
            font=("Segoe UI", 9),
            bg=self.bg_color
        ).pack(side=tk.LEFT)
        
        self.error_var = tk.StringVar(value="M (~15%)")
        error_combo = ttk.Combobox(
            error_frame,
            textvariable=self.error_var,
            values=["L (~7%)", "M (~15%)", "Q (~25%)", "H (~30%)"],
            state="readonly",
            width=12,
            font=("Segoe UI", 9)
        )
        error_combo.pack(side=tk.RIGHT)
        
        # Box Size
        box_frame = tk.Frame(config_section, bg=self.bg_color)
        box_frame.pack(fill=tk.X, pady=5)
        
        tk.Label(
            box_frame,
            text="Tamanho do Box:",
            font=("Segoe UI", 9),
            bg=self.bg_color
        ).pack(side=tk.LEFT)
        
        self.box_var = tk.IntVar(value=10)
        box_scale = ttk.Scale(
            box_frame,
            from_=5,
            to=30,
            variable=self.box_var,
            orient=tk.HORIZONTAL,
            length=100
        )
        box_scale.pack(side=tk.RIGHT, padx=(5, 0))
        
        self.box_label = tk.Label(
            box_frame,
            text="10px",
            font=("Segoe UI", 9, "bold"),
            bg=self.bg_color,
            fg=self.primary_color,
            width=5
        )
        self.box_label.pack(side=tk.RIGHT)
        
        self.box_var.trace("w", self.update_box_label)
        
        # Border
        border_frame = tk.Frame(config_section, bg=self.bg_color)
        border_frame.pack(fill=tk.X, pady=5)
        
        tk.Label(
            border_frame,
            text="Borda:",
            font=("Segoe UI", 9),
            bg=self.bg_color
        ).pack(side=tk.LEFT)
        
        self.border_var = tk.IntVar(value=4)
        border_scale = ttk.Scale(
            border_frame,
            from_=0,
            to=10,
            variable=self.border_var,
            orient=tk.HORIZONTAL,
            length=100
        )
        border_scale.pack(side=tk.RIGHT, padx=(5, 0))
        
        self.border_label = tk.Label(
            border_frame,
            text="4",
            font=("Segoe UI", 9, "bold"),
            bg=self.bg_color,
            fg=self.primary_color,
            width=5
        )
        self.border_label.pack(side=tk.RIGHT)
        
        self.border_var.trace("w", self.update_border_label)
        
        # Seção 3: Cores
        color_section = self.create_section(parent, "Cores")
        
        # Fill Color
        fill_frame = tk.Frame(color_section, bg=self.bg_color)
        fill_frame.pack(fill=tk.X, pady=5)
        
        tk.Label(
            fill_frame,
            text="Cor do QR:",
            font=("Segoe UI", 9),
            bg=self.bg_color
        ).pack(side=tk.LEFT)
        
        self.fill_color_display = tk.Label(
            fill_frame,
            text="      ",
            bg=self.fill_color,
            relief=tk.RAISED,
            bd=2,
            cursor="hand2"
        )
        self.fill_color_display.pack(side=tk.RIGHT, padx=5)
        self.fill_color_display.bind("<Button-1>", self.choose_fill_color)
        
        tk.Button(
            fill_frame,
            text="Escolher",
            command=self.choose_fill_color,
            bg=self.primary_color,
            fg="white",
            relief=tk.FLAT,
            cursor="hand2",
            font=("Segoe UI", 9)
        ).pack(side=tk.RIGHT)
        
        # Back Color
        back_frame = tk.Frame(color_section, bg=self.bg_color)
        back_frame.pack(fill=tk.X, pady=5)
        
        tk.Label(
            back_frame,
            text="Cor de Fundo:",
            font=("Segoe UI", 9),
            bg=self.bg_color
        ).pack(side=tk.LEFT)
        
        self.back_color_display = tk.Label(
            back_frame,
            text="      ",
            bg=self.back_color,
            relief=tk.RAISED,
            bd=2,
            cursor="hand2"
        )
        self.back_color_display.pack(side=tk.RIGHT, padx=5)
        self.back_color_display.bind("<Button-1>", self.choose_back_color)
        
        tk.Button(
            back_frame,
            text="Escolher",
            command=self.choose_back_color,
            bg=self.primary_color,
            fg="white",
            relief=tk.FLAT,
            cursor="hand2",
            font=("Segoe UI", 9)
        ).pack(side=tk.RIGHT)
        
        # Botões de ação
        button_frame = tk.Frame(parent, bg=self.bg_color)
        button_frame.pack(fill=tk.X, pady=(10, 0))
        
        tk.Button(
            button_frame,
            text="Gerar QR Code",
            command=self.generate_qrcode,
            bg=self.primary_color,
            fg="white",
            font=("Segoe UI", 12, "bold"),
            relief=tk.FLAT,
            cursor="hand2",
            height=2
        ).pack(fill=tk.X, pady=(0, 10))
        
        tk.Button(
            button_frame,
            text="Salvar Imagem",
            command=self.save_image,
            bg=self.accent_color,
            fg="white",
            font=("Segoe UI", 11, "bold"),
            relief=tk.FLAT,
            cursor="hand2",
            height=2
        ).pack(fill=tk.X)
        
    def setup_right_panel(self, parent):
        """Configura o painel direito com preview"""
        
        tk.Label(
            parent,
            text="Preview",
            font=("Segoe UI", 14, "bold"),
            bg="white",
            fg=self.text_color
        ).pack(pady=(15, 10))
        
        # Canvas para o QR code
        self.canvas = tk.Canvas(
            parent,
            width=350,
            height=350,
            bg="white",
            highlightthickness=1,
            highlightbackground="#dfe4ea"
        )
        self.canvas.pack(pady=10, padx=15)
        
        # Texto placeholder
        self.placeholder_text = self.canvas.create_text(
            175, 175,
            text="Seu QR Code\naparecerá aqui",
            font=("Segoe UI", 14),
            fill="#dfe4ea",
            justify=tk.CENTER
        )
        
        # Info label
        self.info_label = tk.Label(
            parent,
            text="",
            font=("Segoe UI", 9),
            bg="white",
            fg=self.text_color,
            justify=tk.LEFT,
            wraplength=350
        )
        self.info_label.pack(pady=10, padx=15)
        
    def update_box_label(self, *args):
        """Atualiza o label do box size"""
        self.box_label.config(text=f"{self.box_var.get()}px")
        
    def update_border_label(self, *args):
        """Atualiza o label da borda"""
        self.border_label.config(text=str(self.border_var.get()))
        
    def choose_fill_color(self, event=None):
        """Abre o seletor de cor para fill_color"""
        color = colorchooser.askcolor(initialcolor=self.fill_color, title="Escolha a cor do QR Code")
        if color[1]:
            self.fill_color = color[1]
            self.fill_color_display.config(bg=self.fill_color)
            
    def choose_back_color(self, event=None):
        """Abre o seletor de cor para back_color"""
        color = colorchooser.askcolor(initialcolor=self.back_color, title="Escolha a cor de fundo")
        if color[1]:
            self.back_color = color[1]
            self.back_color_display.config(bg=self.back_color)
            
    def get_error_correction(self):
        """Retorna o nível de correção de erro baseado na seleção"""
        error_map = {
            "L (~7%)": qrcode.constants.ERROR_CORRECT_L,
            "M (~15%)": qrcode.constants.ERROR_CORRECT_M,
            "Q (~25%)": qrcode.constants.ERROR_CORRECT_Q,
            "H (~30%)": qrcode.constants.ERROR_CORRECT_H,
        }
        return error_map[self.error_var.get()]
        
    def generate_qrcode(self):
        """Gera o QR Code com as configurações atuais"""
        data = self.data_entry.get("1.0", tk.END).strip()
        
        if not data:
            messagebox.showwarning("Aviso", "Por favor, insira um link ou texto para gerar o QR Code.")
            return
        
        try:
            # Obter version
            version_str = self.version_var.get()
            if version_str == "Auto" or version_str == "":
                version = None
            else:
                version = int(version_str)
            
            # Criar QR Code
            qr = qrcode.QRCode(
                version=version,
                error_correction=self.get_error_correction(),
                box_size=self.box_var.get(),
                border=self.border_var.get(),
            )
            qr.add_data(data)
            qr.make(fit=True)
            
            # Gerar imagem
            self.qr_image = qr.make_image(fill_color=self.fill_color, back_color=self.back_color)
            
            # Redimensionar para caber no canvas
            img_copy = self.qr_image.copy()
            img_copy.thumbnail((350, 350), Image.Resampling.LANCZOS)
            
            # Converter para PhotoImage
            self.qr_photo = ImageTk.PhotoImage(img_copy)
            
            # Limpar canvas e mostrar imagem
            self.canvas.delete("all")
            self.canvas.create_image(175, 175, image=self.qr_photo)
            
            # Atualizar info
            data_preview = data[:30] + "..." if len(data) > 30 else data
            info_text = f"QR Code gerado!\n"
            info_text += f"Dados: {data_preview}\n"
            info_text += f"Version: {qr.version}\n"
            info_text += f"Box: {self.box_var.get()}px | Borda: {self.border_var.get()}"
            self.info_label.config(text=info_text)
            
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao gerar QR Code:\n{str(e)}")
            
    def save_image(self):
        """Salva o QR Code gerado"""
        if not self.qr_image:
            messagebox.showwarning("Aviso", "Por favor, gere um QR Code primeiro!")
            return
        
        filename = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[
                ("PNG files", "*.png"),
                ("JPEG files", "*.jpg"),
                ("All files", "*.*")
            ],
            initialfile="qrcode.png"
        )
        
        if filename:
            try:
                self.qr_image.save(filename)
                messagebox.showinfo("Sucesso", f"QR Code salvo com sucesso em:\n{filename}")
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao salvar arquivo:\n{str(e)}")


def main():
    root = tk.Tk()
    app = QRCodeGeneratorApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()

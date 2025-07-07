import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class AgendaEstudos(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Agenda de Estudos - Musical dia a dia")
        self.geometry("1200x700")
        self.configure(bg="#ECECEC")  # Fundo geral cinza claro

        # Estilos
        style = ttk.Style()
        style.configure("Topo.TFrame", background="#ECECEC")
        style.configure("Fundo.TFrame", background="#ECECEC")
        style.configure("TLabel", background="#ECECEC", font=("Arial", 12))
        style.configure("Titulo.TLabel", background="#ECECEC", font=("Arial", 20, "bold"))
        style.configure("Cabecalho.TLabel", background="#ECECEC", font=("Arial", 12, "bold"))

        # Topo
        topo = ttk.Frame(self, style="Topo.TFrame")
        topo.pack(pady=10)

        # Logo
        imagem = Image.open("violino.png")  # Substitua pelo nome correto da sua imagem
        imagem = imagem.resize((150, 150))
        self.logo = ImageTk.PhotoImage(imagem)
        label_logo = tk.Label(topo, image=self.logo, bg="#ECECEC")
        label_logo.pack()

        # Título
        titulo = ttk.Label(topo, text="Horário de Estudos", style="Titulo.TLabel")
        titulo.pack()

        # Scroll horizontal
        canvas = tk.Canvas(self, bg="#ECECEC", highlightthickness=0)
        canvas.pack(side="top", fill="both", expand=True)

        scrollbar_x = ttk.Scrollbar(self, orient="horizontal", command=canvas.xview)
        scrollbar_x.pack(side="bottom", fill="x")
        canvas.configure(xscrollcommand=scrollbar_x.set)

        frame_externo = ttk.Frame(canvas, style="Fundo.TFrame")
        canvas.create_window((0, 0), window=frame_externo, anchor="nw")

        # Atualiza tamanho do scroll
        def on_configure(event):
            canvas.configure(scrollregion=canvas.bbox("all"))

        frame_externo.bind("<Configure>", on_configure)

        # Horários e dias
        horarios = [
            "08:00 - 09:30",
            "09:30 - 11:00",
            "11:00 - 11:30",
            "14:00 - 15:30",
            "15:30 - 17:00",
            "17:00 - 17:30"
        ]

        dias = ["Horário", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado"]

        for coluna, dia in enumerate(dias):
            label = ttk.Label(frame_externo, text=dia, style="Cabecalho.TLabel")
            label.grid(row=0, column=coluna, padx=10, pady=5)

        self.entradas = []
        for linha, horario in enumerate(horarios, start=1):
            linha_entries = []
            for coluna in range(len(dias)):
                if coluna == 0:
                    label = ttk.Label(frame_externo, text=horario)
                    label.grid(row=linha, column=coluna, padx=5, pady=5)
                else:
                    entry = ttk.Entry(frame_externo, width=20)
                    entry.grid(row=linha, column=coluna, padx=5, pady=5)
                    linha_entries.append(entry)
            self.entradas.append(linha_entries)

        # Observações
        obs_frame = tk.Frame(self, bg="#ECECEC")
        obs_frame.pack(pady=10, fill="x")

        obs_label = tk.Label(obs_frame, text="Observações:", bg="#ECECEC", font=("Arial", 12))
        obs_label.pack(anchor="w", padx=10)

        self.obs_text = tk.Text(obs_frame, width=150, height=5, bg="#ECECEC", font=("Arial", 11))
        self.obs_text.pack(padx=10, pady=5)

if __name__ == "__main__":
    app = AgendaEstudos()
    app.mainloop()

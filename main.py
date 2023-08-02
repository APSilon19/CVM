import tkinter
from tkinter import messagebox
from PIL import ImageTk, Image

root = tkinter.Tk()
root.title("CVM for MANIT")
c1votes = 0
c2votes = 0
c3votes = 0
c4votes = 0
c5votes = 0
c6votes = 0
nota_votes = 0


def candi1voted():
    tkinter.messagebox.showinfo("VVPAT", "You voted for Candidate1")
    global c1votes
    c1votes = c1votes+1


def candi2voted():
    tkinter.messagebox.showinfo("VVPAT", "You voted for Candidate2")
    global c2votes
    c2votes = c2votes + 1


def candi3voted():
    tkinter.messagebox.showinfo("VVPAT", "You voted for Candidate3")
    global c3votes
    c3votes = c3votes + 1


def candi4voted():
    tkinter.messagebox.showinfo("VVPAT", "You voted for Candidate4")
    global c4votes
    c4votes = c4votes + 1


def candi5voted():
    tkinter.messagebox.showinfo("VVPAT", "You voted for Candidate5")
    global c5votes
    c5votes = c5votes + 1


def candi6voted():
    tkinter.messagebox.showinfo("VVPAT", "You voted for Candidate6")
    global c6votes
    c6votes = c6votes + 1


def notavoted():
    tkinter.messagebox.showinfo("VVPAT", "You voted for NOTA")
    global nota_votes
    nota_votes = nota_votes + 1


def progress():
    nwin = tkinter.Toplevel()
    nwin.title("Results")
    titlelabel = tkinter.Label(nwin, text="Candidate wise Voting Figures are: ").pack(padx=10)
    c1rlabel = tkinter.Label(nwin, text="Candidate1 has " + str(c1votes) + " votes").pack(pady=5)
    c2rlabel = tkinter.Label(nwin, text="Candidate2 has " + str(c2votes) + " votes").pack(pady=5)
    c3rlabel = tkinter.Label(nwin, text="Candidate3 has " + str(c3votes) + " votes").pack(pady=5)
    c4rlabel = tkinter.Label(nwin, text="Candidate4 has " + str(c4votes) + " votes").pack(pady=5)
    c5rlabel = tkinter.Label(nwin, text="Candidate5 has " + str(c5votes) + " votes").pack(pady=5)
    c6rlabel = tkinter.Label(nwin, text="Candidate6 has " + str(c6votes) + " votes").pack(pady=5)
    notalabel = tkinter.Label(nwin, text="NOTA has " + str(nota_votes) + " votes").pack(pady=5)
    conclbutton = tkinter.Button(nwin, text="Conclude Elections", command=lambda: conclude()).pack()

    def conclude():
        def c1win():
            return "CANDIDATE1"

        def c2win():
            return "CANDIDATE2"

        def c3win():
            return "CANDIDATE3"

        def c4win():
            return "CANDIDATE4"

        def c5win():
            return "CANDIDATE5"

        def c6win():
            return "CANDIDATE6"

        def notawin():
            return "NOTA"

        def default():
            return "NOBODY"

        switcher = {
            c1votes: c1win,
            c2votes: c2win,
            c3votes: c3win,
            c4votes: c4win,
            c5votes: c5win,
            c6votes: c6win,
            nota_votes: notawin,
        }

        def switch(cnames):
            return switcher.get(cnames, default)()

        winner = max(c1votes, c2votes, c3votes, c4votes, c5votes, c6votes, nota_votes)
        tkinter.messagebox.showinfo("Winner", str(switch(winner))+" IS THE WINNER!!!")
        reslabel = tkinter.Label(nwin, text="Election process has been concluded").pack(pady=5)


HideButton = tkinter.Button(root, text="Maulana Azad National Institute of Technology", command=progress)
HideButton.grid(row=0, column=1, columnspan=5)
Label1 = tkinter.Label(root, text="Class Representative Elections").grid(row=1, column=2)
Candi1Image = ImageTk.PhotoImage(Image.open("c1.jpg"))
Candi2Image = ImageTk.PhotoImage(Image.open("c2.jpg"))
Candi3Image = ImageTk.PhotoImage(Image.open("c3.jpg"))
Candi4Image = ImageTk.PhotoImage(Image.open("c4.jpg"))
Candi5Image = ImageTk.PhotoImage(Image.open("c5.jpg"))
Candi6Image = ImageTk.PhotoImage(Image.open("c6.jpg"))
Candi1ImageLabel = tkinter.Label(root, image=Candi1Image).grid(row=2, column=1, pady=20, padx=20)
Candi2ImageLabel = tkinter.Label(root, image=Candi2Image).grid(row=2, column=2, padx=20)
Candi3ImageLabel = tkinter.Label(root, image=Candi3Image).grid(row=2, column=3, padx=20)
Candi4ImageLabel = tkinter.Label(root, image=Candi4Image).grid(row=5, column=1, pady=20)
Candi5ImageLabel = tkinter.Label(root, image=Candi5Image).grid(row=5, column=2)
Candi6ImageLabel = tkinter.Label(root, image=Candi6Image).grid(row=5, column=3)
Candi1Label = tkinter.Label(root, text="Candidate1 Name").grid(row=3, column=1)
Candi2Label = tkinter.Label(root, text="Candidate2 Name").grid(row=3, column=2)
Candi3Label = tkinter.Label(root, text="Candidate3 Name").grid(row=3, column=3)
Candi4Label = tkinter.Label(root, text="Candidate4 Name").grid(row=6, column=1)
Candi5Label = tkinter.Label(root, text="Candidate5 Name",).grid(row=6, column=2)
Candi6Label = tkinter.Label(root, text="Candidate6 Name",).grid(row=6, column=3)
Candi1Button = tkinter.Button(root, text="Vote", command=candi1voted).grid(row=4, column=1, ipadx=30)
Candi2Button = tkinter.Button(root, text="Vote", command=candi2voted).grid(row=4, column=2, ipadx=30)
Candi3Button = tkinter.Button(root, text="Vote", command=candi3voted).grid(row=4, column=3, ipadx=30)
Candi4Button = tkinter.Button(root, text="Vote", command=candi4voted).grid(row=7, column=1, ipadx=30)
Candi5Button = tkinter.Button(root, text="Vote", command=candi5voted).grid(row=7, column=2, ipadx=30)
Candi6Button = tkinter.Button(root, text="Vote", command=candi6voted).grid(row=7, column=3, ipadx=30)
NOTAButton = tkinter.Button(root, text="Vote for NOTA", command=notavoted)
NOTAButton.grid(row=10, column=2, ipadx=30, pady=10)
root.mainloop()

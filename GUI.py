import tkinter as tk 
from tkinter import ttk 

from RSA import *

def run_rsa():
    pA = int(entry_pA.get())
    qA = int(entry_qA.get())

    pB = int(entry_pB.get())
    qB = int(entry_qB.get())

    message = int(entry_msg.get())

    pubA, privA = generateKey(pA, qA)
    pubB, privB = generateKey(pB, qB)

    cipher = encrypt(message, pubB)

    auth = addAuth(cipher, privA)

    checked = checkAuth(auth, pubA)

    decrypted = decrypt(checked, privB)

    lbl_pubA.config(text=f"Public Key A : {pubA}")
    lbl_privA.config(text=f"Private Key A : {privA}")

    lbl_pubB.config(text=f"Public Key B : {pubB}")
    lbl_privB.config(text=f"Private Key B : {privB}")

    lbl_cipher.config(text=f"Ciphertext : {cipher}")
    lbl_auth.config(text=f"Authenticated : {auth}")
    lbl_checked.config(text=f"Auth Checked : {checked}")
    lbl_decrypted.config(text=f"Decrypted : {decrypted}")

root = tk.Tk()
root.title("RSA encryptor")
root.geometry("500x400")

tk.Label(root, text="Peer A prime 1").pack()
entry_pA = tk.Entry(root)
entry_pA.pack()
tk.Label(root, text="Peer A prime 2").pack()
entry_qA = tk.Entry(root)
entry_qA.pack()

tk.Label(root, text="Peer B prime 1").pack()
entry_pB = tk.Entry(root)
entry_pB.pack()
tk.Label(root, text="Peer B prime 2").pack()
entry_qB = tk.Entry(root)
entry_qB.pack()
tk.Label(root, text="Message to encrypt").pack()
entry_msg = tk.Entry(root)
entry_msg.pack()


entry_pA.insert(0,"17")
entry_qA.insert(0,"19")

entry_pB.insert(0,"5")
entry_qB.insert(0,"7")

entry_msg.insert(0,"9")



tk.Button(root,
          text="Run RSA",
          command=run_rsa).pack()

lbl_pubA = tk.Label(root)
lbl_privA = tk.Label(root)

lbl_pubB = tk.Label(root)
lbl_privB = tk.Label(root)

lbl_cipher = tk.Label(root)
lbl_auth = tk.Label(root)
lbl_checked = tk.Label(root)
lbl_decrypted = tk.Label(root)


for l in [lbl_pubA,lbl_privA,lbl_pubB,lbl_privB,
          lbl_cipher,lbl_auth,lbl_checked,lbl_decrypted]:
    l.pack()


root.mainloop()
    

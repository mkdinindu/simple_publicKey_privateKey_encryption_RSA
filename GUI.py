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


def run_rsa_real():

    pA = int(entry_pA.get())
    qA = int(entry_qA.get())
    
    pB = int(entry_pB.get())
    qB = int(entry_qB.get())

    ciphered_message = int(entry_msg.get())

    pubA, privA = generateKey(pA, qA)
    #pubB, privB = generateKey(pB, qB)
    pubB = pB, qB 
    checked = checkAuth(ciphered_message, pubB)

    decrypted = decrypt(checked, privA)

    lbl_pubA.config(text=f"Public Key A : {pubA}")
    lbl_privA.config(text=f"Private Key A : {privA}")


    lbl_cipher.config(text=f"Ciphertext : {ciphered_message}")
    lbl_checked.config(text=f"Auth Checked : {checked}")
    lbl_decrypted.config(text=f"Decrypted : {decrypted}")

def toggle_mode():
    if checkbox_var.get():
        # Checkbox is checked: Change labels and unlock the decrypt button
        lbl_title_pA.config(text="Your prime 1")
        lbl_title_qA.config(text="Your prime 2")
        lbl_title_pB.config(text="Reciever's public key 'e' value")
        lbl_title_qB.config(text="Reciever's public key 'n' value")
        
        btn_decrypt.config(state=tk.NORMAL)  # Unlock button
    else:
        # Checkbox is unchecked: Revert labels and lock the decrypt button
        lbl_title_pA.config(text="Peer A prime 1")
        lbl_title_qA.config(text="Peer A prime 2")
        lbl_title_pB.config(text="Peer B prime 1")
        lbl_title_qB.config(text="Peer B prime 2")
        
        btn_decrypt.config(state=tk.DISABLED)  # Lock button

root = tk.Tk()
root.title("RSA encryptor")
root.geometry("500x400")

checkbox_var = tk.BooleanVar()
chk_toggle = tk.Checkbutton(
    root, 
    text="Start an encrypted chat with one of ur bitches, enter their public key pair to belowmost 2 textboxes", 
    variable=checkbox_var, 
    command=toggle_mode
)
chk_toggle.pack(pady=5)


lbl_title_pA = tk.Label(root, text="Peer A prime 1")
lbl_title_pA.pack()
entry_pA = tk.Entry(root)
entry_pA.pack()

lbl_title_qA = tk.Label(root, text="Peer A prime 2")
lbl_title_qA.pack()
entry_qA = tk.Entry(root)
entry_qA.pack()

lbl_title_pB = tk.Label(root, text="Peer B prime 1")
lbl_title_pB.pack()
entry_pB = tk.Entry(root)
entry_pB.pack()

lbl_title_qB = tk.Label(root, text="Peer B prime 2")
lbl_title_qB.pack()
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



# 3. Action Buttons
btn_run = tk.Button(root, text="Run RSA", command=run_rsa)
btn_run.pack(pady=2)

# Decrypt button starts locked (DISABLED)
btn_decrypt = tk.Button(root, text="decrypt", command=run_rsa_real, state=tk.DISABLED)
btn_decrypt.pack(pady=2)

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
    

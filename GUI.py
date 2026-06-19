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
        lbl_title_pA.config(text="Your prime 1")
        lbl_title_qA.config(text="Your prime 2")
        lbl_title_pB.config(text="Reciever's public key 'e' value")
        lbl_title_qB.config(text="Reciever's public key 'n' value")
        
        btn_decrypt.config(state=tk.NORMAL)
    else:
        lbl_title_pA.config(text="Peer A prime 1")
        lbl_title_qA.config(text="Peer A prime 2")
        lbl_title_pB.config(text="Peer B prime 1")
        lbl_title_qB.config(text="Peer B prime 2")
        
        btn_decrypt.config(state=tk.DISABLED)


root = tk.Tk()
root.title("RSA Encryption & Authentication")
root.geometry("560x620")
root.resizable(False, False)

style = ttk.Style()
style.configure("Title.TLabel", font=("Segoe UI", 12, "bold"))
style.configure("Section.TLabelframe", font=("Segoe UI", 10, "bold"))
style.configure("Result.TLabel", font=("Segoe UI", 9))
style.configure("Action.TButton", font=("Segoe UI", 10, "bold"), padding=6)

header = ttk.Label(root, text="RSA Encryption & Authentication Tool", style="Title.TLabel")
header.pack(pady=(12, 4))

sep = ttk.Separator(root, orient="horizontal")
sep.pack(fill="x", padx=10, pady=(0, 8))

main_frame = ttk.Frame(root)
main_frame.pack(fill="both", expand=True, padx=12, pady=0)

input_frame = ttk.LabelFrame(main_frame, text="Keys & Message Input", style="Section.TLabelframe")
input_frame.pack(fill="x", pady=(0, 8))

frameA = ttk.LabelFrame(input_frame, text="Sender (Peer A) — Your Keys", padding=8)
frameA.grid(row=0, column=0, padx=6, pady=6, sticky="nsew")

lbl_title_pA = ttk.Label(frameA, text="Prime 1 (p)")
lbl_title_pA.grid(row=0, column=0, sticky="w", padx=(0, 4))
entry_pA = ttk.Entry(frameA, width=18)
entry_pA.grid(row=0, column=1)

lbl_title_qA = ttk.Label(frameA, text="Prime 2 (q)")
lbl_title_qA.grid(row=1, column=0, sticky="w", padx=(0, 4), pady=(4, 0))
entry_qA = ttk.Entry(frameA, width=18)
entry_qA.grid(row=1, column=1, pady=(4, 0))

frameB = ttk.LabelFrame(input_frame, text="Recipient (Peer B)", padding=8)
frameB.grid(row=0, column=1, padx=6, pady=6, sticky="nsew")

lbl_title_pB = ttk.Label(frameB, text="Prime 1 (p)")
lbl_title_pB.grid(row=0, column=0, sticky="w", padx=(0, 4))
entry_pB = ttk.Entry(frameB, width=18)
entry_pB.grid(row=0, column=1)

lbl_title_qB = ttk.Label(frameB, text="Prime 2 (q)")
lbl_title_qB.grid(row=1, column=0, sticky="w", padx=(0, 4), pady=(4, 0))
entry_qB = ttk.Entry(frameB, width=18)
entry_qB.grid(row=1, column=1, pady=(4, 0))

input_frame.columnconfigure(0, weight=1)
input_frame.columnconfigure(1, weight=1)

msg_frame = ttk.LabelFrame(main_frame, text="Message", padding=6)
msg_frame.pack(fill="x", pady=(0, 6))

lbl_msg = ttk.Label(msg_frame, text="Plaintext (numeric):")
lbl_msg.pack(side="left", padx=(0, 6))
entry_msg = ttk.Entry(msg_frame, width=30)
entry_msg.pack(side="left")

entry_pA.insert(0, "17")
entry_qA.insert(0, "19")
entry_pB.insert(0, "5")
entry_qB.insert(0, "7")
entry_msg.insert(0, "9")

mode_frame = ttk.LabelFrame(main_frame, text="Mode", padding=6)
mode_frame.pack(fill="x", pady=(0, 8))

checkbox_var = tk.BooleanVar()
chk_toggle = ttk.Checkbutton(
    mode_frame,
    text="Decryption mode — use Recipient's public key (e, n) instead of generating from primes",
    variable=checkbox_var,
    command=toggle_mode
)
chk_toggle.pack(anchor="w")

action_frame = ttk.Frame(main_frame)
action_frame.pack(fill="x", pady=(0, 8))

btn_run = ttk.Button(action_frame, text="Encrypt & Sign", command=run_rsa, style="Action.TButton")
btn_run.pack(side="left", padx=(0, 8))

btn_decrypt = ttk.Button(action_frame, text="Decrypt", command=run_rsa_real, state=tk.DISABLED, style="Action.TButton")
btn_decrypt.pack(side="left")

sep2 = ttk.Separator(main_frame, orient="horizontal")
sep2.pack(fill="x", pady=(0, 6))

result_frame = ttk.LabelFrame(main_frame, text="Results", padding=8)
result_frame.pack(fill="both", expand=True)

lbl_pubA = ttk.Label(result_frame, style="Result.TLabel")
lbl_privA = ttk.Label(result_frame, style="Result.TLabel")

lbl_pubB = ttk.Label(result_frame, style="Result.TLabel")
lbl_privB = ttk.Label(result_frame, style="Result.TLabel")

lbl_cipher = ttk.Label(result_frame, style="Result.TLabel")
lbl_auth = ttk.Label(result_frame, style="Result.TLabel")
lbl_checked = ttk.Label(result_frame, style="Result.TLabel")
lbl_decrypted = ttk.Label(result_frame, style="Result.TLabel")

for l in [lbl_pubA, lbl_privA, lbl_pubB, lbl_privB,
          lbl_cipher, lbl_auth, lbl_checked, lbl_decrypted]:
    l.pack(anchor="w", pady=1)


root.mainloop()

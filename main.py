import tkinter as tk
import asymcrypt
import pyperclip
from Crypto.PublicKey import RSA


# Кодировка
def encode():
    data = textE.get("1.0", "end")
    encrypted = asymcrypt.encrypt_data(
        data, 'public.pem', out_format='base64')
    print(encrypted)
    textE.delete("1.0", "end")
    textE.insert(tk.INSERT, encrypted)
    encrypted = textE.get("1.0", "end")
    pyperclip.copy(encrypted)


# Декодирование
def decode():
    my_bytes = textE.get("1.0", "end")
    encrypted = my_bytes.encode('ascii')
    original_message = asymcrypt.decrypt_data(
        encrypted, 'private.pem', in_format='base64')
    textE.delete("1.0", "end")
    textE.insert(tk.INSERT, original_message)


# Генерация открытого ключа
def key_gen():
    key = RSA.generate(2048)
    private_key = key.exportKey()
    file = open("private.pem", "wb")
    file.write(private_key)
    file.close()
    public_key = key.public_key().export_key()
    file = open("public.pem", "wb")
    file.write(public_key)
    file.close()


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("600x300")
    root.resizable(0, 0)
    top = tk.Frame(root)
    bottom = tk.Frame(root)
    top.pack(side=tk.TOP, anchor=tk.W)
    bottom.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
    textE = tk.Text(root, width=35, height=15,
                    background="#303030", foreground="white")
    encodeOp = tk.Button(root, height=1, width=25, text="Encode",
                         command=encode, activebackground="green")
    encodeOp.pack(in_=top, side=tk.LEFT)
    decodeOp = tk.Button(root, height=1, width=25, text="Decode",
                         command=decode, activebackground="green")
    decodeOp.pack(in_=top, side=tk.LEFT)
    genOp = tk.Button(root, height=1, width=25, text="Key gen",
                      command=key_gen, activebackground="green")
    genOp.pack(in_=top, side=tk.TOP)
    scroll = tk.Scrollbar(root)
    scroll.config(command=textE.yview)
    textE.config(yscrollcommand=scroll.set)
    scroll.pack(in_=bottom, side=tk.RIGHT, fill=tk.Y)
    textE.pack(in_=bottom, side=tk.LEFT, fill=tk.BOTH, expand=True)
    root.title("Капралов ПИ19-3")
    key_gen()
    root.mainloop()

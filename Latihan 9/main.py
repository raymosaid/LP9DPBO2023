from apartemen import Apartemen
from rumah import Rumah
from indekos import Indekos
from tkinter import *
from PIL import ImageTk, Image
import requests
import io

# Input data
hunians = []
hunians.append(Apartemen("Nelly Joy", 3, 3, "https://www.essexapartmenthomes.com/-/media/Project/EssexPropertyTrust/Sites/EssexApartmentHomes/Blog/2021/2021-02-26-Renting-an-Apartment-in-Seattle/Renting-an-Apartment-in-Seattle-BellCentre-1.jpg"))
hunians.append(Rumah("Sekar MK", 5, 2, "https://thumbor.forbes.com/thumbor/fit-in/900x510/https://www.forbes.com/home-improvement/wp-content/uploads/2022/07/download-23.jpg"))
hunians.append(Indekos("Bp. Romi", "Cahya", "https://www.tokohkita.co/uploads/berita/thumbs/750x400/20190910_tip-kantongi-uang-lebih-jadi-juragan-indekos.jpg"))
hunians.append(Rumah("Satria", 1, 4, "https://thumbor.forbes.com/thumbor/fit-in/900x510/https://www.forbes.com/home-improvement/wp-content/uploads/2022/07/download-23.jpg"))

# Make root page/main page
root = Tk()
root.title("Praktikum DPBO Python")
photo_image = []

# Make details page
def details(index):
    top = Toplevel()
    top.title("Detail " + hunians[index].get_jenis())

    # Set details page attribute
    d_frame = LabelFrame(top, text="Data Residen", padx=10, pady=10)
    d_frame.pack(padx=10, pady=10)

    # Get index image
    image_url = hunians[index].get_image()
    show = requests.get(image_url)
    image = show.content
    img = Image.open(io.BytesIO(image))
    img = img.resize((500, 250))
    photo_img = ImageTk.PhotoImage(img)
    photo_image.append(photo_img)
    landing_page = Frame(top, padx=5, pady=5)
    landing_page.pack(padx=5, pady=5)
    label_img_landing = Label(landing_page, image=photo_img)
    label_img_landing.pack()

    # Get summary form each class and it's child
    # d_summary = Label(d_frame, text="Summary: " + hunians[index].get_summary(), anchor="w").grid(row=0, column=0, sticky="w")
    d_summary = Label(d_frame, text="Summary\n" + hunians[index].get_detail() + hunians[index].get_summary() + "\n" + hunians[index].get_dokumen(), anchor="w", justify=LEFT).grid(row=0, column=0, sticky="w")

    # Create Exit button
    btn = LabelFrame(top, padx=0, pady=0)
    btn.pack(padx=10, pady=10)
    b_close = Button(btn, text="Close", command=top.destroy)
    b_close.grid(row=0, column=0)

# Make enter page after landing page
def enter():
    # Destroy landing page
    landing_page.destroy()
    label_img_landing.destroy()
    landing_label.destroy()
    b_enter.destroy()
    b_enter_opts.destroy()

    # Create Enter page
    frame = LabelFrame(root, text="Data Seluruh Residen", padx=10, pady=10)
    frame.pack(padx=10, pady=10)

    opts = LabelFrame(root, padx=10, pady=10)
    opts.pack(padx=10, pady=10)

    b_add = Button(opts, text="Add Data", state="disabled")
    b_add.grid(row=0, column=0)

    b_exit = Button(opts, text="Exit", command=root.quit)
    b_exit.grid(row=0, column=1)

    # Get all data and put it on tabel
    for index, h in enumerate(hunians):
        # Set tabel appereance
        idx = Label(frame, text=str(index+1), width=5, borderwidth=1, relief="solid")
        idx.grid(row=index, column=0)

        type = Label(frame, text=h.get_jenis(), width=15, borderwidth=1, relief="solid")
        type.grid(row=index, column=1)

        # Get the index data and put it on table
        if h.get_jenis() != "Indekos": 
            name = Label(frame, text=" " + h.get_nama_pemilik(), width=40, borderwidth=1, relief="solid", anchor="w")
            name.grid(row=index, column=2)
        else:
            name = Label(frame, text=" " + h.get_nama_penghuni(), width=40, borderwidth=1, relief="solid", anchor="w")
            name.grid(row=index, column=2)

        b_detail = Button(frame, text="Details ", command=lambda index=index: details(index))
        b_detail.grid(row=index, column=3)

# Set Landing Page
# Get landing page image
image_url = "https://previews.123rf.com/images/virinka/virinka1412/virinka141200060/34367543-cartoon-town.jpg"
response = requests.get(image_url)
image = response.content
img = Image.open(io.BytesIO(image))
img = img.resize((500, 250))
photo_img = ImageTk.PhotoImage(img)
photo_image.append(photo_img)
landing_page = Frame(root, padx=5, pady=5)
landing_page.pack(padx=5, pady=5)
label_img_landing = Label(landing_page, image=photo_img)
label_img_landing.pack()

# Set label in landing page
landing_label = Label(root, text="Welcome, press enter to see 'Data Seluruh Residen'", padx=10, pady=10)
landing_label.pack()

# Create enter table to go to enter page
b_enter_opts = LabelFrame(root, padx=10, pady=10)
b_enter_opts.pack(padx=10, pady=10)
b_enter = Button(b_enter_opts, text="Enter", command=enter)
b_enter.pack()

root.mainloop()

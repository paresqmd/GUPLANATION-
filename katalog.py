import tkinter
from tkinter import * #memanggil semua fungsi di tkinter
import coreProgram #menghubungkan ke module coreprogram sehingga bolak-balik halaman

def catalogy(): #mempermudah pemanggilan halaman katalog
    global root, catalogCanvas, backcatalog, closecatalog
    root=tkinter.Tk() #menampilkan kotak tampilan
    root.title("Guplation CATALOGY ") #memberi judul pada kotak
    root.geometry('500x500')# memberi ukuran pada kotak
    #load image
    catalogyz=PhotoImage(file='sidecatalog.png') #ambil gambar di komputer penyimpanan

    information=PhotoImage(file='information.png') #ambil gambar untukgambar di tengah
    backcatalog=PhotoImage(file='backcatalog.png') #ambil gambar untuktombol back
    closecatalog=PhotoImage(file='closecatalog.png') #ambil gambar untuktombol close
    #layout
    catalogCanvas=Canvas(root, width=500, height=500, bg='white')
    #template untuk mempurmudah pengaturan objek (alas)
    catalogCanvas.create_image(28,250, image=catalogyz) #di canvas aturgambar, 28 px dri sumbu x, 250 px dri sumbu y, gambar yang diatur adalah catalogyz='gambar yang di simpen komputer'
    catalogCanvas.create_image(625, 250, image=catalogyz) #gambar yangbiru donker, atur posisi gambarnya
    catalogCanvas.create_image(253,220, image=information)#atur 253 px dri sumbu x, 220 px dri sumbu y,, gambar yang diatur adalah judulnya information
    catalogCanvas.pack() #taruh /dilem/ ditempel ke GUI nya

def callback():
    root.destroy() #menghilangkan/menghancurkan gui nya klo mau balik ke halaman selanjutnya
    coreProgram.mainProgram() #menghubungkan ke halaman sebelumnya (memunculkan halaman selanjutnya)

def closing():
    root.destroy() #meghancurkan GUI nya ketika hendak keluar aplikasi/selesai pakai aplikasi
    #button
    back=Button(root, image=backcatalog, borderwidth=0, bg='white',
    width=60, height=60, relief='flat', activebackground='white',
    command=callback)
    catalogCanvas.create_window(90,480, window=back)
    close=Button(root, image=closecatalog, borderwidth=0, bg='white',
    width=100, height=60, relief='flat', activebackground='white',
    command=closing)
    catalogCanvas.create_window(420,480, window=close)
    root.mainloop()

# jika belum ada modul , install dulu
# pip install mysql-connector-python
# --------------------------------------

import mysql.connector
from mysql.connector import Error

def koneksi():
    try:
        # Koneksi ke database
        connection = mysql.connector.connect(
            host='localhost',       
            database='futsal',
            user='root',      
            password='' 
        )
        return connection

    except Error as e:
        print("Error saat mencoba menghubungkan ke MySQL", e)

from tkinter import *
from tkinter import ttk, messagebox
from datetime import datetime, timedelta

class AppOrder:
    def __init__(self, root) -> None:
        self.root = root
        self.root.title('Manajemen Booking Lapangan Futsal')
        self.root.geometry('1000x800+300+10')
        self.root.configure(bg='gray')

        # Frame utama
        self.frame_top = Frame(self.root, bg='white', relief=RIDGE, bd=2)
        self.frame_top.pack(side=TOP, fill=X, padx=10, pady=5)

        self.frame_middle = Frame(self.root, bg='white', relief=RIDGE, bd=2)
        self.frame_middle.pack(fill=BOTH, expand=True, padx=10, pady=5)

        self.frame_bottom = Frame(self.root, bg='white', relief=RIDGE, bd=2)
        self.frame_bottom.pack(side=BOTTOM, fill=X, padx=10, pady=5)

        # Bagian Atas: Pencarian
        self.create_search_section() 

        # Bagian Tengah: Tabel Data
        self.create_table_section()

        # Bagian Bawah: Form Input
        self.create_form_section()

    def create_search_section(self):
        # cari berdasarkan tanggal
        Label(self.frame_top, text="Cari Tanggal (YYYY-MM-DD):", bg='white').grid(row=0, column=0, padx=10, pady=10, sticky=W)
        self.ent_search_date = Entry(self.frame_top, width=20)
        self.ent_search_date.grid(row=0, column=1, padx=10, pady=10) 
        self.btn_search = Button(self.frame_top, text="Cari Data", command=self.search_booking)
        self.btn_search.grid(row=0, column=2, padx=10, pady=10)  
        self.btn_search["state"] = DISABLED 
        self.ent_search_date.bind("<KeyRelease>", self.validate_date)
       
        # cari berdasarkan nama pembooking
        Label(self.frame_top, text="Cari Nama Pembooking: ", bg='white').grid(row=0, column=3, padx=10, pady=10, sticky=W)
        self.ent_search_name = Entry(self.frame_top, width=20)
        self.ent_search_name.grid(row=0, column=4, padx=10, pady=10)
        self.btn_search2 = Button(self.frame_top, text="Cari Nama", command=self.search_booking2)
        self.btn_search2.grid(row=0, column=5, padx=10, pady=10)

    def create_table_section(self):
        # Tabel Data
        self.tree = ttk.Treeview(
            self.frame_middle,
            columns=("ID Booking", "Nama Pembooking" ,"No Telepon", "ID Lapangan", "Waktu Mulai", "Durasi", "Waktu Selesai", "Total Bayar"),
            show="headings",
        )
        self.tree.heading("ID Booking", text="ID Booking") 
        self.tree.heading("Nama Pembooking", text="Nama Pembooking")
        self.tree.heading("No Telepon", text="No Telepon")
        self.tree.heading("ID Lapangan", text="ID Lapangan")
        self.tree.heading("Waktu Mulai", text="Waktu Mulai")
        self.tree.heading("Durasi", text="Durasi")
        self.tree.heading("Waktu Selesai", text="Waktu Selesai")
        self.tree.heading("Total Bayar", text="Total Bayar")

        self.tree.column("ID Booking", anchor='center')
        self.tree.column("Nama Pembooking", anchor='center')
        self.tree.column("No Telepon", anchor='center')
        self.tree.column("ID Lapangan", anchor='center')
        self.tree.column("Waktu Mulai", anchor='center')
        self.tree.column("Durasi", anchor='center')
        self.tree.column("Waktu Selesai", anchor='center')
        self.tree.column("Total Bayar", anchor='center')
        self.tree.pack(fill=BOTH, expand=True, padx=10, pady=10)

        # Scrollbar Vertikal
        scroll_y = Scrollbar(self.frame_middle, orient=VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)

        # scrollbar horizontal
        scroll_x = Scrollbar(self.frame_middle, orient=HORIZONTAL, command=self.tree.xview)
        self.tree.configure(xscrollcommand=scroll_x.set)
        scroll_x.pack(side=BOTTOM, fill=X)

        # Tombol Hapus Data
        self.btn_delete = Button(self.frame_middle, text="Hapus Data", command=self.delete_booking)
        self.btn_delete.pack(side=BOTTOM, pady=10)
        self.btn_delete["state"] = DISABLED 
        self.tree.bind("<<TreeviewSelect>>", self.activate_delete_button) 
        

    def create_form_section(self):
        # Input Data
        Label(self.frame_bottom, text="Nama Pembooking:", bg='white').grid(row=0, column=0, padx=10, pady=10, sticky=W)
        self.ent_nama = Entry(self.frame_bottom, width=25)
        self.ent_nama.grid(row=0, column=1, padx=10, pady=10, sticky=W)

        Label(self.frame_bottom, text="No Telepon:", bg='white').grid(row=1, column=0, padx=10, pady=10, sticky=W)
        self.ent_telepon = Entry(self.frame_bottom, width=25)
        self.ent_telepon.grid(row=1, column=1, padx=10, pady=10, sticky=W)

        Label(self.frame_bottom, text="Waktu Booking (YYYY-MM-DD hh):", bg='white').grid(row=2, column=0, padx=10, pady=10, sticky=W)
        self.ent_date = Entry(self.frame_bottom, width=15)
        self.ent_date.grid(row=2, column=1, padx=5, pady=10, sticky=W)
        self.ent_hour = Entry(self.frame_bottom, width=5)
        self.ent_hour.grid(row=2, column=2, padx=5, pady=10, sticky=W)

        Label(self.frame_bottom, text="Durasi Booking (jam):", bg='white').grid(row=3, column=0, padx=10, pady=10, sticky=W)
        self.ent_durasi = Entry(self.frame_bottom, width=10)
        self.ent_durasi.grid(row=3, column=1, padx=10, pady=10, sticky=W)

        Label(self.frame_bottom, text="Pilih Lapangan:", bg='white').grid(row=4, column=0, padx=10, pady=10, sticky=W)
        self.combo_lapangan = ttk.Combobox(self.frame_bottom, state="readonly", width=23)
        self.combo_lapangan.grid(row=4, column=1, padx=10, pady=10, sticky=W)
        self.load_lapangan()

        # Tombol Form
        Button(self.frame_bottom, text="Hapus Inputan", command=self.clear_form).grid(row=5, column=0, padx=10, pady=20)
        Button(self.frame_bottom, text="Konfirmasi", command=self.confirm_booking).grid(row=5, column=1, padx=10, pady=20)

    def load_lapangan(self):
        try:
            conn = koneksi()
            cursor = conn.cursor()
            cursor.execute("SELECT nama_lapangan FROM Ms_Lapangan")
            rows = cursor.fetchall()
            self.combo_lapangan["values"] = [f"{row[0]}" for row in rows]
            cursor.close()
            conn.close()
        except Exception as e:
            messagebox.showerror("Error", f"Gagal memuat data lapangan: {e}")

    def validate_date(self, event):
        date_text = self.ent_search_date.get()
        try:
            datetime.strptime(date_text, "%Y-%m-%d")
            self.btn_search["state"] = NORMAL
        except ValueError:
            self.btn_search["state"] = DISABLED

    def search_booking(self):
        date_text = self.ent_search_date.get()
        try:
            conn = koneksi()
            cursor = conn.cursor()
            query = """
                    SELECT tr.id_booking, 
                    mp.nama_pembooking,
                    tr.no_telepon,
                    tr.id_lapangan,
                    tr.waktu_mulai_booking,
                    tr.durasi_booking,
                    tr.waktu_selesai_booking,
                    tr.total_bayar
                    FROM Tr_Daftar_booking AS tr JOIN Ms_pembooking AS mp ON tr.no_telepon = mp.no_telepon WHERE DATE(tr.waktu_mulai_booking) = %s
            """
            cursor.execute(query, (date_text,))
            rows = cursor.fetchall()

            for i in self.tree.get_children():
                self.tree.delete(i)

            for row in rows:
                self.tree.insert("", "end", values=row)
            cursor.close()
            conn.close()
        except Exception as e:
            messagebox.showerror("Error", f"Gagal memuat data booking: {e}")

    def search_booking2(self):
        date_text = self.ent_search_name.get()
        try:
            conn = koneksi()
            cursor = conn.cursor()
            query = """
                    SELECT tr.id_booking, 
                    mp.nama_pembooking,
                    tr.no_telepon,
                    tr.id_lapangan,
                    tr.waktu_mulai_booking,
                    tr.durasi_booking,
                    tr.waktu_selesai_booking,
                    tr.total_bayar
                    FROM Tr_Daftar_booking AS tr JOIN Ms_pembooking AS mp ON tr.no_telepon = mp.no_telepon WHERE mp.nama_pembooking = %s
            """
            cursor.execute(query, (date_text,))
            rows = cursor.fetchall()

            for i in self.tree.get_children():
                self.tree.delete(i)

            for row in rows:
                self.tree.insert("", "end", values=row)
            cursor.close()
            conn.close()
        except Exception as e:
            messagebox.showerror("Error", f"Gagal memuat data booking: {e}")

    def activate_delete_button(self, event):
        self.btn_delete["state"] = NORMAL

    def delete_booking(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Peringatan", "Pilih data terlebih dahulu!")
            return

        confirm = messagebox.askyesno("Konfirmasi", "Apakah Anda yakin ingin menghapus data yang dipilih?")
        if confirm:
            item = self.tree.item(selected_item)
            id_booking = item["values"][0]

            try:
                conn = koneksi()
                cursor = conn.cursor()
                query = "DELETE FROM Tr_Daftar_booking WHERE id_booking = %s"
                cursor.execute(query, (id_booking,))
                conn.commit()
                cursor.close()
                conn.close()
                self.tree.delete(selected_item)
                messagebox.showinfo("Sukses", "Data berhasil dihapus!")
            except Exception as e:
                messagebox.showerror("Error", f"Gagal menghapus data: {e}")

    def clear_form(self):
        self.ent_nama.delete(0, END)
        self.ent_telepon.delete(0, END)
        self.ent_date.delete(0, END)
        self.ent_hour.delete(0, END)
        self.ent_durasi.delete(0, END)
        self.combo_lapangan.set("")

    from datetime import timedelta

    def confirm_booking(self):
        # Mengambil data dari input form
        nama = self.ent_nama.get().strip()
        telepon = self.ent_telepon.get().strip()
        tanggal = self.ent_date.get().strip()
        jam = self.ent_hour.get().strip()
        durasi = self.ent_durasi.get().strip()
        lapangan = self.combo_lapangan.get().strip()

        # Validasi input kosong
        if not all([nama, telepon, tanggal, jam, durasi, lapangan]):
            messagebox.showerror("Error", "Semua field harus diisi.")
            return

        # Validasi format tanggal dan jam
        try:
            waktu_booking = datetime.strptime(f"{tanggal} {jam}:00:00", "%Y-%m-%d %H:%M:%S")
            if waktu_booking < datetime.now():
                raise ValueError("Waktu booking tidak boleh kurang dari waktu sekarang.")
        except ValueError as e:
            messagebox.showerror("Error", f"Format waktu tidak valid: {e}")
            return

        # Validasi durasi
        try:
            durasi = int(durasi)
            if durasi <= 0:
                raise ValueError("Durasi harus lebih besar dari 0.")
        except ValueError:
            messagebox.showerror("Error", "Durasi harus berupa angka positif.")
            return

        # Hitung waktu selesai booking
        waktu_selesai = waktu_booking + timedelta(hours=durasi) - timedelta(seconds=1)
        total_bayar = durasi * 10000 #SATU JAM 10 RIBU

        # Validasi lapangan tersedia
        try:
            conn = koneksi()
            cursor = conn.cursor()
            query = "SELECT id_lapangan FROM Ms_lapangan WHERE nama_lapangan = %s"
            cursor.execute(query,(lapangan,))
            data_lapangan = cursor.fetchone()
            id_lapangan = data_lapangan[0]
             
            query = """
                SELECT * FROM Tr_Daftar_booking
                WHERE id_lapangan = %s
                AND (
                    (%s BETWEEN waktu_mulai_booking AND waktu_selesai_booking) OR
                    (%s BETWEEN waktu_mulai_booking AND waktu_selesai_booking) OR
                    (waktu_mulai_booking BETWEEN %s AND %s)
                )
            """
            cursor.execute(query, (id_lapangan, waktu_booking, waktu_selesai, waktu_booking, waktu_selesai))
            existing_bookings = cursor.fetchall()
            if existing_bookings:
                messagebox.showerror("Error", "Lapangan sudah dibooking pada rentang waktu yang dipilih.")
                cursor.close()
                conn.close()
                return
        except Exception as e:
            messagebox.showerror("Error", f"Gagal memvalidasi lapangan: {e}")
            return

        # Validasi pembooking di database
        try:
            # JIKA NAMA PEMBOOKING SUDAH ADA DALAM DATABASE MAKA AKAN DIUPDATE NO_TELEPONNYA MENJADI NO TELEPON PEMBOOKING TERBARU
            cursor.execute("SELECT no_telepon FROM Ms_Pembooking WHERE nama_pembooking = %s", (nama,))
            pembooking_data = cursor.fetchone()
            if pembooking_data:
                cursor.execute("UPDATE Ms_Pembooking SET no_telepon = %s WHERE nama_pembooking = %s", (telepon,nama)) 
                cursor.execute("UPDATE Tr_Daftar_booking SET no_telepon = %s WHERE no_telepon = %s", (telepon, pembooking_data[0])) 
                no_telepon = telepon 
            else:
                # Tambahkan pembooking baru ke tabel ms_pembooking, jika tidak ada atau pembooking belum pernah membooking.
                cursor.execute("INSERT INTO Ms_Pembooking (nama_pembooking, no_telepon) VALUES (%s, %s)", (nama, telepon))
                no_telepon = telepon  
            conn.commit()
        except Exception as e:
            conn.rollback()
            messagebox.showerror("Error", f"Gagal menyimpan data pembooking: {e}")
            return

        # Konfirmasi transaksi
        confirm = messagebox.askyesno("Konfirmasi", f"Apakah Anda yakin ingin menambahkan transaksi booking? TOTAL BAYAR : {total_bayar}")
        if not confirm:
            return

        # Simpan data booking ke database
        try:
            query = """
                INSERT INTO Tr_Daftar_booking (no_telepon, id_lapangan, waktu_mulai_booking, durasi_booking, waktu_selesai_booking, total_bayar)
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            cursor.execute(query, (no_telepon, id_lapangan, waktu_booking, durasi, waktu_selesai, total_bayar))
            conn.commit()
            messagebox.showinfo("Sukses", "Transaksi berhasil ditambahkan!")
            self.clear_form()  # Bersihkan form input
        except Exception as e:
            conn.rollback()
            messagebox.showerror("Error", f"Gagal menyimpan transaksi booking: {e}")
        finally:
            cursor.close()
            conn.close()



if __name__ == '__main__':
    root = Tk()
    app = AppOrder(root)
    root.mainloop()

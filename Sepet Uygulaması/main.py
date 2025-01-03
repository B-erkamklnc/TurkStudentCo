import tkinter as tk
from tkinter import ttk, messagebox

# Yeni ürün eklemek için sınıf
class AddProductDialog:
    def __init__(self, parent):
        # Modal pencere oluştur
        self.window = tk.Toplevel(parent)
        self.window.title("Yeni Ürün Ekle")
        self.window.grab_set()  # Diğer pencereleri bloke et
        
        # Pencere boyutu ve konumu
        window_width = 300
        window_height = 200
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        self.window.geometry(f"{window_width}x{window_height}+{x}+{y}")
        
        # Arayüz elemanlarını oluştur
        self.create_widgets()
        
    def create_widgets(self):
        # Form alanları
        labels = ['Ürün Adı:', 'Kategori:', 'Fiyat:', 'Stok:']
        self.entries = {}
        
        for i, label in enumerate(labels):
            tk.Label(self.window, text=label).grid(row=i, column=0, padx=5, pady=5, sticky="e")
            entry = tk.Entry(self.window)
            entry.grid(row=i, column=1, padx=5, pady=5, sticky="ew")
            self.entries[label] = entry
        
        # Butonlar
        button_frame = tk.Frame(self.window)
        button_frame.grid(row=len(labels), column=0, columnspan=2, pady=10)
        
        tk.Button(button_frame, text="Kaydet", command=self.save).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="İptal", command=self.cancel).pack(side=tk.LEFT, padx=5)
        
        # Grid yapılandırması
        self.window.columnconfigure(1, weight=1)
        
    def save(self):
        # Kullanıcıdan alınan bilgileri kaydet
        self.result = {
            'name': self.entries['Ürün Adı:'].get(),
            'category': self.entries['Kategori:'].get(),
            'price': self.entries['Fiyat:'].get(),
            'stock': self.entries['Stok:'].get()
        }
        self.window.destroy()
        
    def cancel(self):
        # İptal durumunda sonucu None yap
        self.result = None
        self.window.destroy()

# GUI sınıfı
class MarketGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Market Yönetim Sistemi")
        
        # Ana pencere boyutu ve konumu
        window_width = 800
        window_height = 600
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")
        
        # Arayüz elemanlarını oluştur
        self.create_widgets()
        self.load_products()
        
    def create_widgets(self):
        # Tablo
        columns = ('id', 'name', 'category', 'price', 'stock')
        self.tree = ttk.Treeview(self.root, columns=columns, show='headings')
        
        # Başlıklar
        self.tree.heading('id', text='ID')
        self.tree.heading('name', text='Ürün Adı')
        self.tree.heading('category', text='Kategori')
        self.tree.heading('price', text='Fiyat')
        self.tree.heading('stock', text='Stok')
        
        # Sütun genişlikleri
        self.tree.column('id', width=50)
        self.tree.column('name', width=200)
        self.tree.column('category', width=150)
        self.tree.column('price', width=100)
        self.tree.column('stock', width=100)
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(self.root, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        
        # Butonlar
        button_frame = tk.Frame(self.root)
        ttk.Button(button_frame, text="Ürün Ekle", command=self.add_product).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Ürün Sil", command=self.delete_product).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Yenile", command=self.load_products).pack(side=tk.LEFT, padx=5)
        
        # Layout
        button_frame.pack(pady=10)
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(10, 0), pady=(0, 10))
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y, pady=(0, 10), padx=(0, 10))
        
    def load_products(self):
        # Mevcut ürünleri temizle
        for item in self.tree.get_children():
            self.tree.delete(item)
            
        try:
            with open("product.txt", "r", encoding="utf-8") as file:
                for i, line in enumerate(file, 1):
                    name, category, price, stock = line.strip().split(",")
                    self.tree.insert('', tk.END, values=(i, name, category, f"{float(price):.2f}", stock))
        except FileNotFoundError:
            # Dosya yoksa oluştur
            with open("product.txt", "w", encoding="utf-8") as file:
                pass
        except Exception as e:
            messagebox.showerror("Hata", f"Ürünler yüklenirken hata oluştu: {e}")
            
    def add_product(self):
        dialog = AddProductDialog(self.root)
        self.root.wait_window(dialog.window)
        
        if hasattr(dialog, 'result') and dialog.result:
            try:
                # Veri doğrulama
                price = float(dialog.result['price'])
                stock = int(dialog.result['stock'])
                
                if not dialog.result['name'] or not dialog.result['category']:
                    raise ValueError("Ürün adı ve kategori boş olamaz!")
                
                # Ürünü dosyaya ekle
                with open("product.txt", "a", encoding="utf-8") as file:
                    file.write(f"{dialog.result['name']},{dialog.result['category']},{price},{stock}\n")
                
                self.load_products()
                messagebox.showinfo("Başarılı", "Ürün başarıyla eklendi.")
                
            except ValueError as e:
                messagebox.showwarning("Hata", str(e))
            except Exception as e:
                messagebox.showerror("Hata", f"Ürün eklenirken hata oluştu: {e}")
                
    def delete_product(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Uyarı", "Lütfen silinecek ürünü seçin!")
            return
            
        if messagebox.askyesno("Onay", "Bu ürünü silmek istediğinizden emin misiniz?"):
            try:
                with open("product.txt", "r", encoding="utf-8") as file:
                    lines = file.readlines()
                
                # Seçili ürünün indeksini bul ve sil
                index = self.tree.index(selected_item)
                lines.pop(index)
                
                with open("product.txt", "w", encoding="utf-8") as file:
                    file.writelines(lines)
                
                self.load_products()
                messagebox.showinfo("Başarılı", "Ürün başarıyla silindi.")
                
            except Exception as e:
                messagebox.showerror("Hata", f"Ürün silinirken hata oluştu: {e}")
                
    def __del__(self):
        """ 'product.txt', 'with' ile açıldığı için otomatik olarak kapatılacaktır"""
        print("Program kapatıldı!")


def main():
    root = tk.Tk()
    app = MarketGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()

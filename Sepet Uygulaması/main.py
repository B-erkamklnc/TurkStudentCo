import tkinter as tk
from tkinter import messagebox
import os

class Market:
    def __init__(self):
        self.file_name = "product.txt"
        if not os.path.exists(self.file_name):
            with open(self.file_name, 'w') as file:
                pass

    def __del__(self):
        pass  # Dosya işlemleri anlık yapıldığı için burada kapatma işlemi gerekmez

    def list_products(self):
        with open(self.file_name, 'r') as file:
            return [line.strip().split(',') for line in file.readlines()]

    def add_product(self, name, category, price, stock):
        with open(self.file_name, 'a') as file:
            file.write(f"{name},{category},{price},{stock}\n")

    def delete_product(self, name):
        products = self.list_products()
        products = [product for product in products if product[0] != name]
        with open(self.file_name, 'w') as file:
            for product in products:
                file.write(','.join(product) + "\n")

class MarketApp:
    def __init__(self, root):
        self.market = Market()
        self.cart = {}

        self.root = root
        self.root.title("Çevrimiçi Market Alışveriş Sepeti")

        self.main_frame = tk.Frame(root)
        self.main_frame.pack(pady=20)

        self.product_list = tk.Listbox(self.main_frame, width=50, height=15)
        self.product_list.pack(side=tk.LEFT, padx=10)

        self.scrollbar = tk.Scrollbar(self.main_frame, orient=tk.VERTICAL)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.product_list.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.product_list.yview)

        self.load_products()

        self.control_frame = tk.Frame(root)
        self.control_frame.pack(pady=20)

        self.add_button = tk.Button(self.control_frame, text="Ürün Ekle", command=self.open_add_product_window)
        self.add_button.grid(row=0, column=0, padx=10)

        self.delete_button = tk.Button(self.control_frame, text="Ürün Sil", command=self.delete_selected_product)
        self.delete_button.grid(row=0, column=1, padx=10)

        self.add_to_cart_button = tk.Button(self.control_frame, text="Sepete Ekle", command=self.add_to_cart)
        self.add_to_cart_button.grid(row=0, column=2, padx=10)

        self.cart_label = tk.Label(root, text="Sepet Toplamı: 0 TL")
        self.cart_label.pack(pady=10)

    def load_products(self):
        self.product_list.delete(0, tk.END)
        products = self.market.list_products()
        for product in products:
            self.product_list.insert(tk.END, f"{product[0]} - {product[1]} - {product[2]} TL - Stok: {product[3]}")

    def open_add_product_window(self):
        def save_product():
            name = name_entry.get()
            category = category_entry.get()
            price = price_entry.get()
            stock = stock_entry.get()

            if not all([name, category, price, stock]):
                messagebox.showerror("Hata", "Tüm alanları doldurmalısınız!")
                return

            try:
                float(price)
                int(stock)
            except ValueError:
                messagebox.showerror("Hata", "Fiyat ve stok uygun formatta olmalıdır!")
                return

            self.market.add_product(name, category, price, stock)
            self.load_products()
            add_product_window.destroy()

        add_product_window = tk.Toplevel(self.root)
        add_product_window.title("Yeni Ürün Ekle")

        tk.Label(add_product_window, text="Ürün Adı").grid(row=0, column=0, pady=5)
        tk.Label(add_product_window, text="Kategori").grid(row=1, column=0, pady=5)
        tk.Label(add_product_window, text="Fiyat").grid(row=2, column=0, pady=5)
        tk.Label(add_product_window, text="Stok").grid(row=3, column=0, pady=5)

        name_entry = tk.Entry(add_product_window)
        category_entry = tk.Entry(add_product_window)
        price_entry = tk.Entry(add_product_window)
        stock_entry = tk.Entry(add_product_window)

        name_entry.grid(row=0, column=1, pady=5)
        category_entry.grid(row=1, column=1, pady=5)
        price_entry.grid(row=2, column=1, pady=5)
        stock_entry.grid(row=3, column=1, pady=5)

        tk.Button(add_product_window, text="Kaydet", command=save_product).grid(row=4, column=0, columnspan=2, pady=10)

    def delete_selected_product(self):
        selected = self.product_list.curselection()
        if not selected:
            messagebox.showerror("Hata", "Silmek için bir ürün seçmelisiniz!")
            return

        product_info = self.product_list.get(selected[0])
        product_name = product_info.split(' - ')[0]

        self.market.delete_product(product_name)
        self.load_products()

    def add_to_cart(self):
        selected = self.product_list.curselection()
        if not selected:
            messagebox.showerror("Hata", "Sepete eklemek için bir ürün seçmelisiniz!")
            return

        product_info = self.product_list.get(selected[0])
        product_name, _, price, stock_info = product_info.split(' - ')
        stock = int(stock_info.split(': ')[1])
        price = float(price.split(' ')[0])

        if product_name not in self.cart:
            self.cart[product_name] = {'adet': 1, 'fiyat': price}
        else:
            if self.cart[product_name]['adet'] < stock:
                self.cart[product_name]['adet'] += 1
            else:
                messagebox.showerror("Hata", "Yeterli stok yok!")
                return

        total = sum(item['adet'] * item['fiyat'] for item in self.cart.values())
        self.cart_label.config(text=f"Sepet Toplamı: {total:.2f} TL")

if __name__ == "__main__":
    root = tk.Tk()
    app = MarketApp(root)
    root.mainloop()

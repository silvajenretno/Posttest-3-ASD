class Order:
    def __init__(self, order_id, nama_item, jumlah_item, harga, waktu_pemesanan):
        self.order_id = order_id
        self.nama_item = nama_item
        self.jumlah_item = jumlah_item
        self.harga = harga
        self.waktu_pemesanan = waktu_pemesanan
        self.next_order = None

class OrderHistory():
    def __init__(self):
        self.head = None

    def add_order(self, order_id, nama_item, jumlah_item, harga, waktu_pemesanan):
        new_order = Order(order_id, nama_item, jumlah_item, harga, waktu_pemesanan)
        if self.head is None:
            self.head = new_order
        else:
            pesanan_sekarang = self.head
            while pesanan_sekarang.next_order is not None:
                pesanan_sekarang = pesanan_sekarang.next_order
            pesanan_sekarang.next_order = new_order

    def show_orders(self):
        print(">>>>>>>>>>>>>>>>>>>>>>>>>PESAN-ANTAR MAKANAN<<<<<<<<<<<<<<<<<<<<<<<<<")
        if len(orders) == 0:
            print("Belum ada riwayat order ^.^")
        else:
            print("Riwayat order:")
            for order in orders:
                print(f"Order ID: {order.order_id}. Item yang dipesan {order.nama_item} jumlah pesanan {order.jumlah_item} seharga {order.harga} waktu pemesanan : {order.waktu_pemesanan}")

    def get_orders(self, size_halaman, nomor_halaman):
        orders = []
        pesanan_sekarang = self.head
        count = 1
        while pesanan_sekarang is not None:
            if count > (nomor_halaman - 1) * size_halaman and count <= nomor_halaman * size_halaman:
                orders.append(pesanan_sekarang)
            pesanan_sekarang = pesanan_sekarang.next_order
            count += 1
        return orders
    
order_history = OrderHistory()
# order_history.add_order(1, "Martabak", 2, 50000, "2023-02-16 18:30:00")
# order_history.add_order(2, "Nasi Uduk", 1, 10000, "2023-02-17 12:15:00")
# order_history.add_order(3, "Mie Ayam", 1, 12000, "2023-03-17 19:45:00")

# Menampilkan 2 pesanan dalam satu halaman 
orders = order_history.get_orders(2, 1) 
order_history.show_orders()
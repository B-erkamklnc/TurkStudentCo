# TO-Do List Uygulaması

Bu Python uygulaması, kullanıcılara basit bir yapılacaklar listesi oluşturup yönetmelerine olanak tanır. Uygulama, görevleri ekleme, tamamlama, silme ve listeleme gibi temel işlevleri sağlar. Ek olarak, görev verileri bir text dosyasında saklanır ve uygulama tekrar çalıştırıldığında geri yüklenir.

## Özellikler
- **Görev Ekleme**: Kullanıcı yeni bir görev tanımlayabilir.
- **Görevi Tamamlama**: Mevcut bir görev tamamlandı olarak işaretlenebilir.
- **Görev Silme**: Görevler listeden tamamen kaldırılabilir.
- **Görev Listeleme**: Tamamlanan ve tamamlanmayan görevler ayrı ayrı görüntülenir.
- **Veri Saklama**: Görevler, `tasks.txt` dosyasında saklanır ve uygulama yeniden çalıştırıldığında otomatik olarak geri yüklenir.

## Gereksinimler
- Python 3.x

## Kullanım
1. Uygulamaya ait dosyayı bilgisayarınıza indirin.
2. Terminal veya komut satırında şu komutla çalıştırın:
   ```bash
   python To-Do List.py
   ```
3. Aşağıdaki menü aracılığıyla işlemleri gerçekleştirin:
   - **1**: Görev Ekle
   - **2**: Görevi Tamamla
   - **3**: Görev Sil
   - **4**: Görevleri Listele
   - **5**: Çıkış

## Dosya Yapısı
- `To-Do List.py`: Ana uygulama dosyası.
- `tasks.txt`: Görevlerin saklandığı text dosyası. Uygulama tarafından otomatik olarak oluşturulur.

## Notlar
- `tasks.txt` dosyası, görev adları ve tamamlanma durumunu saklar. Dosyanın silinmesi durumunda mevcut görevler kaybolur.
- Dosya formatı:
  ```
  Görev Adı|Durum (True/False)
  ```


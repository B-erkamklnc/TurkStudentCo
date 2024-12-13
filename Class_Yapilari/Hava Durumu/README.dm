# Hava Durumu Kullanım Rehberi

Bu proje, belirttiğiniz şehirlerin hava durumu bilgilerini MGM (Meteoroloji Genel Müdürlüğü) web sitesinden çekmek ve hava koşullarına uygun öneriler sunmak için geliştirilmiştir. 

## Gereksinimler

1. **Python**: Bu projeyi çalıştırmak için Python'un yüklü olması gerekir. Python'u [python.org](https://www.python.org) adresinden indirebilirsiniz.
2. **Selenium**: Web tarayıcısını kontrol etmek için Selenium kullanılmaktadır.
3. **ChromeDriver**: Selenium'un Google Chrome ile çalışması için uygun sürücüye ihtiyacınız vardır.

## Kurulum

### Selenium Kurulumu

1. Terminal veya komut istemcisini açın.
2. Aşağıdaki komutu kullanarak Selenium'u yükleyin:
   ```bash
   pip install selenium
   ```

### ChromeDriver İndirme ve Kurulum

1. Google Chrome sürümünüzü öğrenin:
   - Chrome tarayıcısını açın.
   - Sağ üst köşedeki üç nokta menüsüne tıklayın.
   - "Yardım > Google Chrome Hakkında" seçeneğine tıklayın.
   - Chrome sürüm numarasını not edin.

2. ChromeDriver'ı indirin:
   - [ChromeDriver indirme sayfasına](https://sites.google.com/chromium.org/driver/) gidin.
   - Chrome sürümünüe uygun olan sürücüyü indirin.

3. İndirilen dosyayı bir klasöre çıkarın.
4. Çıkarılan dosyanın yolunu not edin ve bu yolu `PATH` ortam değişkenine ekleyin veya kodun içinde doğrudan belirtebilirsiniz.

## Çalıştırma

1. `main.py` dosyasını çalıştırmak için terminal veya komut istemcisinde şu komutu kullanın:
   ```bash
   python Hava Durumu.py
   ```

2. Program menüsü karşınıza çıkacaktır. Şehir ekleyebilir, bilgilerini güncelleyebilir veya hava durumu hakkında öneri alabilirsiniz.

### Örnek Kullanım

- **Şehir Ekleme**:
  - Bir şehir eklemek için "1" seçeneğini seçin.
  - Şehir adını (ve gerekirse ilçeyi) girin. Örneğin: `ankara` veya `ankara çankaya`.

- **Tüm Şehir Verilerini Görme**:
  - "4" seçeneği ile tüm şehirlerin hava durumu bilgilerini görebilirsiniz.

- **Tavsiye Alma**:
  - "5" seçeneğini seçin ve şehir adını girin.
  - Program, hava durumu ve sıcaklığa uygun kıyafet önerileri sunacaktır.

- **Şehir Silme**:
  - "3" seçeneği ile şehir verilerini silebilirsiniz.

- **Çıkış Yapma**:
  - "6" seçeneği ile programdan çıkabilirsiniz.

## Notlar

- Programda bir ilçeye ait bilgi almak istiyorsanız, il ve ilçe adını boşlukla ayırarak girin.
- MGM web sitesindeki yapısal değişiklikler veya sürücü uyumsuzlukları programın çalışmasını etkileyebilir.
- Eğer program veri çekemiyorsa, internet bağlantınızı veya ChromeDriver ayarlarını kontrol edin.
- Şu anlık şehir ismini yanlış yazarsanız MGM deault sayfa üzerinden değer döndürmektedir. (yakında yenilenecek)


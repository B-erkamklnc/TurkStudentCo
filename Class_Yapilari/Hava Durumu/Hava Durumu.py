from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time


class Location:
    def __init__(self, city, district=None):
        # MGM web sitesinin temel URL'si
        self.url = "https://www.mgm.gov.tr/?il="
        self.city = city
        self.district = district
        
        # Selenium tarayıcı ayarları (headless mod)
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        self.browser = webdriver.Chrome(options=chrome_options)
        
        # İlçe bilgisi var mı kontrol et
        if self.district is None:
            self.full_url = self.url + self.city
            self.location_name = city
        else:
            self.full_url = self.url + self.city + "&ilce=" + self.district
            self.location_name = city + " " + district


    def fetch_weather(self):
        # Web sitesinden hava durumu bilgilerini çek
        self.browser.get(self.full_url)
        time.sleep(2)
        try:
            info = self.browser.find_element(By.XPATH, '//*[@id="siteBody"]/section[1]/div/div[2]/div[2]/div/p').text
            temperature = self.browser.find_element(By.XPATH, '//*[@id="siteBody"]/section[1]/div/div[2]/div[2]/div/h3/span[1]/ziko').text
            return info, temperature
        except Exception as e:
            return "Veri alınamadı", "N/A", e # yanlış isim veya sayı girilirse site main adresini döndürüyor. Except şu an çalışmıyor.


class WeatherManager:
    def __init__(self):
        # Şehir ve hava durumu verilerinin saklandığı sözlük
        self.data = {}
 
    
    def add_location(self, location_name):
        if location_name in self.data:
            print(f"{location_name} zaten eklenmiş.")
        else:
            parts = location_name.split()
            if len(parts) == 2:
                location = Location(parts[0], parts[1])
            else:
                location = Location(location_name)
            weather_data = location.fetch_weather()
            self.data[location_name] = weather_data
            print(f"{location_name} eklendi.")


    def update_location(self, location_name):
        parts = location_name.split()
        if len(parts) == 2:
            location = Location(parts[0], parts[1])
        else:
            location = Location(location_name)
        weather_data = location.fetch_weather()
        self.data[location_name] = weather_data
        print(f"{location_name} verileri güncellendi.")


    def delete_location(self, location_name):
        if location_name in self.data:
            self.data.pop(location_name)
            print("Şehir verileri silindi.")
        else:
            print(f"{location_name} bulunamadı.")


    def list_all_locations(self):
        try:
            for location in self.data:
                print(f"{location} için beklenen hadise: {self.data[location][0]}  \nSıcaklık: {self.data[location][1]}°C \n")
        except:
            print("Lütfen önce şehir giriniz!")


    def get_weather_with_advice(self, location_name):
        if location_name in self.data:
            advice = self.get_advice(self.data[location_name][0], float(self.data[location_name][1].replace(",", ".")))
            print(f"{location_name} için beklenen hadise: {self.data[location_name][0]}  \nSıcaklık: {self.data[location_name][1]}°C \n{advice}")
        else:
            print(f"{location_name} bulunamadı.")


    def get_advice(self, condition, temperature):
        # Hava durumu için öneriler
        rain_conditions = ["Hafif Yağmurlu", "Yağmurlu", "Kuvvetli Yağmurlu", "Hafif Sağanak Yağışlı", 
                           "Sağanak Yağışlı", "Kuvvetli Sağanak Yağışlı", "Yer Yer Sağanak Yağışlı", 
                           "Gökgürültülü Sağanak Yağışlı", "Karla Karışık Yağmurlu"]
        snow_conditions = ["Hafif Kar Yağışlı", "Kar Yağışlı", "Yoğun Kar Yağışlı", "Dolu"]
        wind_conditions = ["Rüzgarlı", "Toz veya Kum Fırtınası", "Güneyli Kuvvetli Rüzgar", "Kuzeyli Kuvvetli Rüzgar"]
        fog_conditions = ["Duman", "Pus", "Sis"]
              
        if condition in rain_conditions:
            incident_advice = "Yağmurdan etkilenmeyecek kıyafetler tercih et."
        elif condition in snow_conditions:
            incident_advice = "Kardan etkilenmeyecek kıyafetler tercih et."
        elif condition in wind_conditions:
            incident_advice = "Rüzgardan etkilenmeyecek kıyafetler tercih et."
        elif condition in fog_conditions:
            incident_advice = "Reflektörlü kıyafetler tercih et."
        else:
            incident_advice = ""
        
        if temperature < -5:
            temp_advice = "Çok soğuk, aman diyim sıkı giyin üşütmen."
        elif -5 <= temperature < 5:
            temp_advice = "Soğuk, kalın giyin."
        elif 5 <= temperature < 15:
            temp_advice = "Serin, mont giyin."
        elif 15 <= temperature < 30:
            temp_advice = "İdeal hava, rahat ince şeyler giyin."
        else:
            temp_advice = "Çok sıcak, terlemeyi azaltacak şeyler giyin."

        return f"{temp_advice} {incident_advice}"

def main():
    weather_manager = WeatherManager()

    while True:
        print("\nNOT: Eğer bir ilçe ismi girecekseniz önce il sonra ilçe olmak üzere aralarına boşluk koyarak giriniz.")
        print("1. Şehir Ekle")
        print("2. Şehir Verilerini Güncelle")
        print("3. Şehir Sil")
        print("4. Tüm Şehir Verilerini Gör")
        print("5. Tavsiye Al")
        print("6. Programdan Çık")
        
        selection = input("Seçiminizi yapın: ")        
        if selection == "1":
            name = input("Şehir Adı: ").lower()
            weather_manager.add_location(name)
            time.sleep(3)
        elif selection == "2":
            name = input("Şehir Adı: ").lower()
            weather_manager.update_location(name)
            time.sleep(3)
        elif selection == "3":           
            name = input("Şehir Adı: ").lower()
            weather_manager.delete_location(name)
            time.sleep(3)
        elif selection == "4":           
            weather_manager.list_all_locations()
            time.sleep(5)
        elif selection == "5":
            name = input("Şehir Adı: ").lower()
            weather_manager.get_weather_with_advice(name)
            time.sleep(5)
        elif selection == "6":
            print("Programdan çıkılıyor.")
            break
        else:
            print("Geçersiz seçim. Tekrar deneyin.")

if __name__ == "__main__":
    main()

# SQL Komutları Açıklamaları

## A. Belirli Kolonları Seçme
```sql
SELECT FirstName, LastName, Salary FROM Employees;
```
- `FROM` ile hangi tabloda işlem yapacağımızı seçtik.  
- `SELECT` ile görmek istediğimiz kolonları seçtik.

## B. DISTINCT Komutu ile Tekrarları Önleme
```sql
SELECT DISTINCT DepartmentID FROM Employees;
```
- `DISTINCT` ile `Employees` tablosundaki `DepartmentID` değerlerini tekrar etmeden listeledik.

```sql
SELECT * FROM Departments;
```
- `ID`'lerin diğer tablodaki karşılık gelen departmanlarını öğrenebiliriz.

## C. Belirli Bir Departmana Ait Çalışanları Listeleme
```sql
SELECT * FROM Employees WHERE DepartmentID = 1;
```
- `WHERE` ile `DepartmentID` değeri **1** olan satırları filtreledik.

## D. Sıralama Yapma
```sql
SELECT * FROM Employees ORDER BY Salary, FirstName;
```
- `ORDER BY` ile önce **Salary** sonra **FirstName** kolonuna göre sıralama yaptık.
- Burada **FirstName** olmasa da olurdu fakat büyük verilerde sıralama işlemlerini daha anlamlı hale getirir.

## E. Kolonları Birleştirme ve Yeni İsimlendirme
```sql
SELECT LastName || ' ' || FirstName AS Name FROM Employees;
```
- `||` operatörü ile kolonları arasına boşluk koyarak birleştirdik.
- `AS` komutu ile oluşan yeni kolona **Name** adını verdik.


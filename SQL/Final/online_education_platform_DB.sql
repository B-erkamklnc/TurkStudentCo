-- Üyeler Tablosu
-- kullanıcı bilgilerini saklar (üye kimliği, kullanıcı adı, e-posta, şifre, vb.)
CREATE TABLE Members (
    member_id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY, 
    username VARCHAR(50) NOT NULL UNIQUE, 
    email VARCHAR(100) NOT NULL UNIQUE, 
    password VARCHAR(255) NOT NULL, -- Şifre (hash olarak saklanmalıdır)
    registration_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP, -
    first_name VARCHAR(50) NOT NULL, 
    last_name VARCHAR(50) NOT NULL 
);

-- Kategoriler Tablosu
-- eğitimlerin kategorilerini saklar (yapay zeka, blok zincir, siber güvenlik, vb.)
CREATE TABLE Categories (
    category_id SMALLINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY, 
    name VARCHAR(100) NOT NULL UNIQUE, 
    description TEXT 
);

-- Eğitimler Tablosu
-- Bu tablo platformdaki tüm eğitimlerin bilgilerini saklar
CREATE TABLE Courses (
    course_id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY, 
    title VARCHAR(200) NOT NULL, 
    description TEXT, 
    start_date DATE NOT NULL, 
    end_date DATE NOT NULL, 
    instructor VARCHAR(100) NOT NULL, 
    category_id SMALLINT NOT NULL, 
    FOREIGN KEY (category_id) REFERENCES Categories(category_id) ON DELETE RESTRICT -- Kategori silinirse eğitim silinmez, işlem engellenir
);

-- Katılımlar Tablosu
-- hangi kullanıcının hangi eğitime katıldığını takip eder (çok-çok ilişkisi)
CREATE TABLE Enrollments (
    enrollment_id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY, 
    member_id BIGINT NOT NULL, 
    course_id BIGINT NOT NULL, 
    enrollment_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP, -- Katılım tarihi, varsayılan olarak şu anki zaman
    FOREIGN KEY (member_id) REFERENCES Members(member_id) ON DELETE CASCADE, -- Üye silinirse katılım kaydı da silinir
    FOREIGN KEY (course_id) REFERENCES Courses(course_id) ON DELETE CASCADE, -- Eğitim silinirse katılım kaydı da silinir
    UNIQUE (member_id, course_id) -- Bir üye aynı eğitime yalnızca bir kez kaydolabilir
);

-- Sertifikalar Tablosu
-- tamamlanan eğitimler için verilen sertifikaların bilgilerini saklar
CREATE TABLE Certificates (
    certificate_id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY, 
    certificate_code VARCHAR(100) NOT NULL UNIQUE, 
    issue_date DATE NOT NULL, 
    course_id BIGINT NOT NULL, 
    FOREIGN KEY (course_id) REFERENCES Courses(course_id) ON DELETE RESTRICT -- Eğitim silinirse sertifika silinmez, işlem engellenir
);

-- Sertifika Atamaları Tablosu
-- hangi kullanıcının hangi sertifikayı aldığını ilişkilendirir (çok-çok ilişkisi)
CREATE TABLE CertificateAssignments (
    assignment_id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY, 
    member_id BIGINT NOT NULL, 
    certificate_id BIGINT NOT NULL,
    assignment_date DATE NOT NULL DEFAULT CURRENT_DATE, -- Sertifikanın atandığı tarih, varsayılan olarak bugün
    FOREIGN KEY (member_id) REFERENCES Members(member_id) ON DELETE CASCADE, -- Üye silinirse atamalar da silinir
    FOREIGN KEY (certificate_id) REFERENCES Certificates(certificate_id) ON DELETE CASCADE, -- Sertifika silinirse atamalar da silinir
    UNIQUE (member_id, certificate_id) -- Bir üye aynı sertifikayı yalnızca bir kez alabilir
);

-- Blog Gönderileri Tablosu
-- kullanıcıların platformda yayınladıkları blog yazılarını saklar
CREATE TABLE BlogPosts (
    post_id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY, 
    title VARCHAR(255) NOT NULL, 
    content TEXT NOT NULL, 
    publication_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP, -- Yayın tarihi, varsayılan olarak şu anki zaman
    author_id BIGINT NOT NULL, 
    FOREIGN KEY (author_id) REFERENCES Members(member_id) ON DELETE CASCADE -- Üye silinirse blog gönderileri de silinir
);

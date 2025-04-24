-- Üyeler tablosu
CREATE TABLE Members (
    member_id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    registration_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL
);

-- Eğitim Kategorileri tablosu
CREATE TABLE Categories (
    category_id SMALLINT PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

-- Eğitimler tablosu
CREATE TABLE Courses (
    course_id SERIAL PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    description TEXT,
    start_date DATE,
    end_date DATE,
    instructor VARCHAR(100),
    category_id SMALLINT REFERENCES Categories(category_id)
);

-- Katılımlar tablosu (Many-to-Many ilişki için ara tablo)
CREATE TABLE Enrollments (
    enrollment_id SERIAL PRIMARY KEY,
    member_id INTEGER NOT NULL REFERENCES Members(member_id),
    course_id INTEGER NOT NULL REFERENCES Courses(course_id),
    enrollment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Sertifikalar tablosu
CREATE TABLE Certificates (
    certificate_id SERIAL PRIMARY KEY,
    certificate_code VARCHAR(100) UNIQUE NOT NULL,
    issue_date DATE NOT NULL
);

-- Sertifika Atamaları tablosu
CREATE TABLE CertificateAssignments (
    assignment_id SERIAL PRIMARY KEY,
    member_id INTEGER NOT NULL REFERENCES Members(member_id),
    certificate_id INTEGER NOT NULL REFERENCES Certificates(certificate_id),
    received_date DATE DEFAULT CURRENT_DATE
);

-- Blog Gönderileri tablosu
CREATE TABLE BlogPosts (
    post_id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    content TEXT NOT NULL,
    publish_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    author_id INTEGER NOT NULL REFERENCES Members(member_id)
);

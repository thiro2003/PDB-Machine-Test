-- # 7. Create MySQL database named TrainingCenter with table Students:
-- # (id, name, email, marks, attendance, course)
-- # Tasks:
-- # • Insert at least 20 records
-- # • Write SQL queries to:
-- # o Find top 5 students based on marks
-- # o Find students with attendance less than 75%
-- # o Calculate average marks per course
-- # • Connect database with Python
-- # • Fetch and display results in formatted output

-- ANS:-

-- Create MySQL database named TrainingCenter

create database TrainingCenter;
use TrainingCenter;

show tables;

-- creating table table Students

create table Students (id int primary key, name varchar(40), email varchar(60), marks int , attendance_percentage int, course varchar(30));
-- # • Insert at least 20 records

insert into Students (id, name, email, marks, attendance_percentage, course) values 
(1, 'Amit Sharma', 'amit@gmail.com', 85, '90', 'BCA'),
(2, 'Sneha Patil', 'sneha@gmail.com', 78, '88', 'BBA'),
(3, 'Rahul Verma', 'rahul@gmail.com', 92, '95', 'BCA'),
(4, 'Priya Singh', 'priya@gmail.com', 67, '80', 'BCom'),
(5, 'Rohan Desai', 'rohan@gmail.com', 74, '85', 'BSc'),
(6, 'Neha Joshi', 'neha@gmail.com', 88, '92', 'BCA'),
(7, 'Karan Mehta', 'karan@gmail.com', 59, '70', 'BBA'),
(8, 'Pooja Kulkarni', 'pooja@gmail.com', 81, '89', 'BCom'),
(9, 'Arjun Nair', 'arjun@gmail.com', 76, '84', 'BSc'),
(10, 'Meera Iyer', 'meera@gmail.com', 91, '96', 'BCA'),
(11, 'Vikram Rao', 'vikram@gmail.com', 69, '75', 'BBA'),
(12, 'Anjali Gupta', 'anjali@gmail.com', 87, '93', 'BCom'),
(13, 'Sahil Khan', 'sahil@gmail.com', 72, '82', 'BSc'),
(14, 'Divya Reddy', 'divya@gmail.com', 95, '98', 'BCA'),
(15, 'Manish Yadav', 'manish@gmail.com', 64, '78', 'BBA'),
(16, 'Kavya Shetty', 'kavya@gmail.com', 83, '90', 'BCom'),
(17, 'Aditya Jain', 'aditya@gmail.com', 77, '86', 'BSc'),
(18, 'Nikita More', 'nikita@gmail.com', 89, '94', 'BCA'),
(19, 'Sandeep Chavan', 'sandeep@gmail.com', 71, '81', 'BBA'),
(20, 'Tanvi Shah', 'tanvi@gmail.com', 93, '97', 'BCom');

-- # o Find top 5 students based on marks

select name, marks from students  order by marks desc limit 5; 

-- # o Find students with attendance less than 75% 
select * from Students where attendance_percentage<75; 

-- # o Calculate average marks per course

select course, round(avg(marks),1) from Students group by course;

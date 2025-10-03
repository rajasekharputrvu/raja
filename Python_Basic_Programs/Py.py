# Python Fundamentals - Practice Workbook
# Hands-on exercises to reinforce learning from the 3-hour session
# Complete these exercises to master Python fundamentals

import json
import os
from datetime import datetime

print("="*60)
print("PYTHON FUNDAMENTALS - PRACTICE WORKBOOK")
print("Hands-on exercises to reinforce your learning")
print("="*60)

# =============================================================================
# EXERCISE SET 1: CONTROL STRUCTURES
# =============================================================================

def exercise_set_1():
    """
    Practice exercises for control structures
    """
    print("\n" + "="*50)
    print("EXERCISE SET 1: CONTROL STRUCTURES")
    print("="*50)
    
    print("\nEXERCISE 1.1: Grade Calculator")
    print("-" * 30)
    print("Write a function that takes a list of scores and returns grade statistics")
    
    def calculate_class_grades(scores):
        """
        TODO: Complete this function
        
        Requirements:
        - Calculate letter grades for each score (A≥90, B≥80, C≥70, D≥60, F<60)
        - Count how many students got each grade
        - Calculate class average
        - Return a dictionary with results
        """
        # TODO: Your code here
        grade_counts = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0}
        grades = []
        
        for score in scores:
            if score >= 90:
                grade = 'A'
            elif score >= 80:
                grade = 'B'
            elif score >= 70:
                grade = 'C'
            elif score >= 60:
                grade = 'D'
            else:
                grade = 'F'
            
            grades.append(grade)
            grade_counts[grade] += 1
        
        average = sum(scores) / len(scores) if scores else 0
        
        return {
            'grades': grades,
            'grade_counts': grade_counts,
            'class_average': average,
            'total_students': len(scores)
        }
    
    # Test your function
    test_scores = [95, 87, 78, 92, 65, 71, 88, 94, 82, 76]
    result = calculate_class_grades(test_scores)
    
    print("Test Results:")
    print(f"Class Average: {result['class_average']:.1f}")
    print("Grade Distribution:")
    for grade, count in result['grade_counts'].items():
        print(f"  {grade}: {count} students")
    
    print("\nEXERCISE 1.2: Number Pattern Generator")
    print("-" * 40)
    print("Create different number patterns using loops")
    
    def generate_fibonacci(n): # 0 1 1 2 3 .................................00
        """Generate first n Fibonacci numbers"""
        # TODO: Complete this function
        if n <= 0:
            return []
        elif n == 1:
            return [0]
        elif n == 2:
            return [0, 1]
        
        fib = [0, 1]
        for i in range(2, n):
            fib.append(fib[i-1] + fib[i-2])
        return fib
    
    def generate_prime_numbers(limit):
        """Generate prime numbers up to limit using Sieve of Eratosthenes"""
        # TODO: Complete this function
        if limit < 2:
            return []
        
        # Create a boolean array and initialize all entries as True
        primes = [True] * (limit + 1)
        primes[0] = primes[1] = False
        
        p = 2
        while p * p <= limit:
            if primes[p]:
                # Update all multiples of p
                for i in range(p * p, limit + 1, p):
                    primes[i] = False
            p += 1
        
        return [i for i in range(2, limit + 1) if primes[i]]
    
    # Test the functions
    print("First 10 Fibonacci numbers:", generate_fibonacci(10))
    print("Prime numbers up to 30:", generate_prime_numbers(30))
    
    print("\nEXERCISE 1.3: Conditional Logic Challenge")
    print("-" * 40)
    print("Build a smart recommendation system")
    
    def movie_recommender(age, genre_preference, time_available):
        """
        Recommend movies based on user preferences
        
        Args:
            age (int): User's age
            genre_preference (str): 'action', 'comedy', 'drama', 'horror', 'sci-fi'
            time_available (int): Minutes available to watch
        
        Returns:
            dict: Recommendation with movie title and reason
        """
        # TODO: Complete this recommendation logic
        recommendations = {
            'action': {
                'short': 'John Wick (101 min)',
                'medium': 'Mad Max: Fury Road (120 min)', 
                'long': 'The Dark Knight (152 min)'
            },
            'comedy': {
                'short': 'Superbad (113 min)',
                'medium': 'The Hangover (100 min)',
                'long': 'Anchorman (94 min)'
            },
            'drama': {
                'short': 'Whiplash (106 min)',
                'medium': 'The Pursuit of Happyness (117 min)',
                'long': 'The Godfather (175 min)'
            }
        }
        
        # Determine time category
        if time_available < 110:
            time_cat = 'short'
        elif time_available < 130:
            time_cat = 'medium'
        else:
            time_cat = 'long'
        
        # Age restrictions
        restricted_genres = []
        if age < 13:
            restricted_genres = ['horror', 'action']
        elif age < 17:
            restricted_genres = ['horror']
        
        # Get recommendation
        if genre_preference in restricted_genres:
            return {
                'movie': 'Age-appropriate alternative recommended',
                'reason': f'Selected genre not suitable for age {age}'
            }
        
        if genre_preference in recommendations:
            movie = recommendations[genre_preference][time_cat]
            return {
                'movie': movie,
                'reason': f'Perfect {genre_preference} movie for {time_available} minutes'
            }
        
        return {
            'movie': 'The Shawshank Redemption',
            'reason': 'Universal classic recommendation'
        }
    
    # Test the recommender
    test_cases = [
        (25, 'action', 120),
        (12, 'horror', 90),
        (30, 'comedy', 95)
    ]
    
    for age, genre, time in test_cases:
        rec = movie_recommender(age, genre, time)
        print(f"Age {age}, {genre}, {time}min: {rec['movie']} - {rec['reason']}")

# =============================================================================
# EXERCISE SET 2: FILE HANDLING
# =============================================================================

def exercise_set_2():
    """
    Practice exercises for file handling
    """
    print("\n" + "="*50)
    print("EXERCISE SET 2: FILE HANDLING")
    print("="*50)
    
    print("\nEXERCISE 2.1: Log File Analyzer")
    print("-" * 30)
    
    def create_sample_log():
        """Create a sample log file for analysis"""
        log_entries = [
            "2024-01-15 09:00:01 INFO User Alice logged in",
            "2024-01-15 09:05:23 INFO File uploaded: document.pdf",
            "2024-01-15 09:07:45 WARNING High memory usage detected",
            "2024-01-15 09:10:12 ERROR Database connection failed",
            "2024-01-15 09:15:33 INFO User Bob logged in",
            "2024-01-15 09:20:44 ERROR File not found: missing.txt",
            "2024-01-15 09:25:15 INFO Backup completed successfully",
            "2024-01-15 09:30:22 WARNING Disk space low",
            "2024-01-15 09:35:18 INFO User Alice logged out",
            "2024-01-15 09:40:55 ERROR Permission denied"
        ]
        
        with open('sample_system.log', 'w') as f:
            for entry in log_entries:
                f.write(entry + '\n')
        
        print("Created sample_system.log with 10 entries")
    
    def analyze_log_file(filename):
        """
        Analyze log file and generate statistics
        
        TODO: Complete this function to:
        - Count different log levels (INFO, WARNING, ERROR)
        - Find the most common error messages
        - Track user activities
        - Generate hourly activity distribution
        """
        try:
            with open(filename, 'r') as file:
                lines = file.readlines()
            
            log_levels = {'INFO': 0, 'WARNING': 0, 'ERROR': 0}
            user_activities = {}
            hourly_distribution = {}
            errors = []
            
            for line in lines:
                parts = line.strip().split(' ', 3)
                if len(parts) >= 4:
                    date, time, level, message = parts
                    hour = time.split(':')[0]
                    
                    # Count log levels
                    if level in log_levels:
                        log_levels[level] += 1
                    
                    # Track hourly distribution
                    hourly_distribution[hour] = hourly_distribution.get(hour, 0) + 1
                    
                    # Track user activities
                    if 'User' in message:
                        user_activities[message] = user_activities.get(message, 0) + 1
                    
                    # Collect errors
                    if level == 'ERROR':
                        errors.append(message)
            
            return {
                'total_entries': len(lines),
                'log_levels': log_levels,
                'hourly_distribution': hourly_distribution,
                'user_activities': user_activities,
                'errors': errors
            }
            
        except FileNotFoundError:
            return {'error': f'File {filename} not found'}
    
    # Create and analyze log file
    create_sample_log()
    analysis = analyze_log_file('sample_system.log')
    
    print("\nLog Analysis Results:")
    print(f"Total entries: {analysis['total_entries']}")
    print("Log level distribution:")
    for level, count in analysis['log_levels'].items():
        print(f"  {level}: {count}")
    
    print("\nEXERCISE 2.2: CSV Data Processor")
    print("-" * 30)
    
    def create_sales_csv():
        """Create sample sales data CSV"""
        sales_data = [
            "Date,Product,Quantity,Price,Salesperson,Region",
            "2024-01-01,Laptop,2,999.99,Alice,North",
            "2024-01-01,Mouse,5,25.50,Bob,South", 
            "2024-01-02,Keyboard,3,75.00,Charlie,East",
            "2024-01-02,Monitor,1,299.99,Alice,North",
            "2024-01-03,Laptop,1,999.99,Diana,West",
            "2024-01-03,Mouse,8,25.50,Bob,South",
            "2024-01-04,Tablet,2,499.99,Charlie,East",
            "2024-01-04,Headphones,4,150.00,Diana,West",
            "2024-01-05,Laptop,3,999.99,Alice,North"
        ]
        
        with open('sales_data.csv', 'w') as f:
            for line in sales_data:
                f.write(line + '\n')
        
        print("Created sales_data.csv")
    
    def process_sales_data(filename):
        """
        Process sales CSV and generate business insights
        
        TODO: Complete this function to:
        - Calculate total revenue by product
        - Find top performing salesperson
        - Analyze regional performance
        - Generate summary statistics
        """
        try:
            with open(filename, 'r') as file:
                lines = file.readlines()
            
            # Skip header
            data_lines = lines[1:]
            
            product_revenue = {}
            salesperson_revenue = {}
            region_revenue = {}
            total_revenue = 0
            
            for line in data_lines:
                parts = line.strip().split(',')
                if len(parts) >= 6:
                    date, product, quantity, price, salesperson, region = parts
                    
                    quantity = int(quantity)
                    price = float(price)
                    revenue = quantity * price
                    total_revenue += revenue
                    
                    # Aggregate by product
                    product_revenue[product] = product_revenue.get(product, 0) + revenue
                    
                    # Aggregate by salesperson
                    salesperson_revenue[salesperson] = salesperson_revenue.get(salesperson, 0) + revenue
                    
                    # Aggregate by region
                    region_revenue[region] = region_revenue.get(region, 0) + revenue
            
            return {
                'total_revenue': total_revenue,
                'product_revenue': product_revenue,
                'salesperson_revenue': salesperson_revenue,
                'region_revenue': region_revenue,
                'total_transactions': len(data_lines)
            }
            
        except FileNotFoundError:
            return {'error': f'File {filename} not found'}
    
    # Create and process sales data
    create_sales_csv()
    sales_analysis = process_sales_data('sales_data.csv')
    
    print("\nSales Analysis Results:")
    print(f"Total Revenue: ${sales_analysis['total_revenue']:,.2f}")
    print(f"Total Transactions: {sales_analysis['total_transactions']}")
    
    print("\nTop Products by Revenue:")
    sorted_products = sorted(sales_analysis['product_revenue'].items(), 
                           key=lambda x: x[1], reverse=True)
    for product, revenue in sorted_products[:3]:
        print(f"  {product}: ${revenue:,.2f}")

# =============================================================================
# EXERCISE SET 3: COMPREHENSIONS
# =============================================================================

def exercise_set_3():
    """
    Practice exercises for comprehensions
    """
    print("\n" + "="*50)
    print("EXERCISE SET 3: COMPREHENSIONS")
    print("="*50)
    
    print("\nEXERCISE 3.1: Data Filtering and Transformation")
    print("-" * 45)
    
    # Sample dataset
    employees = [
        {'name': 'Alice', 'department': 'Engineering', 'salary': 95000, 'years': 5},
        {'name': 'Bob', 'department': 'Sales', 'salary': 65000, 'years': 3},
        {'name': 'Charlie', 'department': 'Engineering', 'salary': 105000, 'years': 8},
        {'name': 'Diana', 'department': 'Marketing', 'salary': 70000, 'years': 4},
        {'name': 'Eve', 'department': 'Engineering', 'salary': 85000, 'years': 2},
        {'name': 'Frank', 'department': 'Sales', 'salary': 75000, 'years': 6}
    ]
    
    print("Employee dataset created with 6 employees")
    
    # TODO: Complete these comprehensions
    
    # 1. Get names of employees earning more than $80,000
    high_earners = [emp['name'] for emp in employees if emp['salary'] > 80000]
    print(f"High earners (>$80k): {high_earners}")
    
    # 2. Create salary dictionary by department
    dept_salaries = {dept: [emp['salary'] for emp in employees if emp['department'] == dept] 
                    for dept in set(emp['department'] for emp in employees)}
    print("Salaries by department:")
    for dept, salaries in dept_salaries.items():
        avg_salary = sum(salaries) / len(salaries)
        print(f"  {dept}: avg ${avg_salary:,.0f}")
    
    # 3. Senior employees (5+ years) with salary increase calculation
    senior_emp_bonuses = {emp['name']: emp['salary'] * 0.1 
                         for emp in employees if emp['years'] >= 5}
    print(f"Senior employee bonuses: {senior_emp_bonuses}")
    
    print("\nEXERCISE 3.2: Text Processing with Comprehensions")
    print("-" * 45)
    
    # Sample text data
    reviews = [
        "This product is amazing and works perfectly!",
        "Terrible quality, broke after one day.",
        "Good value for money, recommended.",
        "Excellent service and fast delivery.",
        "Poor packaging, item arrived damaged.",
        "Outstanding quality, will buy again!",
        "Not worth the price, very disappointed."
    ]
    
    # TODO: Complete these text processing tasks
    
    # 1. Extract positive and negative words
    positive_words = {'amazing', 'perfectly', 'good', 'excellent', 'recommended', 
                     'outstanding', 'fast', 'quality'}
    negative_words = {'terrible', 'broke', 'poor', 'damaged', 'disappointed', 'not'}
    
    # Analyze sentiment using comprehensions
    review_sentiments = []
    for review in reviews:
        words = review.lower().split()
        pos_count = sum(1 for word in words if word.rstrip('!.,') in positive_words)
        neg_count = sum(1 for word in words if word.rstrip('!.,') in negative_words)
        
        if pos_count > neg_count:
            sentiment = 'positive'
        elif neg_count > pos_count:
            sentiment = 'negative'
        else:
            sentiment = 'neutral'
        
        review_sentiments.append(sentiment)
    
    print("Review sentiment analysis:")
    for i, (review, sentiment) in enumerate(zip(reviews, review_sentiments)):
        print(f"  Review {i+1}: {sentiment}")
    
    # 2. Word frequency analysis
    all_words = [word.lower().rstrip('!.,') for review in reviews for word in review.split()]
    word_freq = {word: all_words.count(word) for word in set(all_words) if len(word) > 3}
    
    print("\nMost common words (length > 3):")
    sorted_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)[:5]
    for word, freq in sorted_words:
        print(f"  {word}: {freq}")

# =============================================================================
# EXERCISE SET 4: OBJECT-ORIENTED PROGRAMMING
# =============================================================================

def exercise_set_4():
    """
    Practice exercises for OOP
    """
    print("\n" + "="*50)
    print("EXERCISE SET 4: OBJECT-ORIENTED PROGRAMMING")
    print("="*50)
    
    print("\nEXERCISE 4.1: Library Management System")
    print("-" * 40)
    
    class Book:
        """Represents a book in the library"""
        
        def __init__(self, title, author, isbn, copies=1):
            # TODO: Complete the Book class
            self.title = title
            self.author = author
            self.isbn = isbn
            self.total_copies = copies
            self.available_copies = copies
            self.borrowed_by = []
        
        def borrow(self, borrower_name):
            """Borrow a book if available"""
            if self.available_copies > 0:
                self.available_copies -= 1
                self.borrowed_by.append(borrower_name)
                return f"Book '{self.title}' borrowed by {borrower_name}"
            return f"Sorry, '{self.title}' is not available"
        
        def return_book(self, borrower_name):
            """Return a borrowed book"""
            if borrower_name in self.borrowed_by:
                self.available_copies += 1
                self.borrowed_by.remove(borrower_name)
                return f"Book '{self.title}' returned by {borrower_name}"
            return f"{borrower_name} hasn't borrowed '{self.title}'"
        
        def __str__(self):
            return f"'{self.title}' by {self.author} (Available: {self.available_copies}/{self.total_copies})"
    
    class Library:
        """Manages a collection of books"""
        
        def __init__(self, name):
            # TODO: Complete the Library class
            self.name = name
            self.books = {}  # ISBN -> Book object
            self.members = set()
        
        def add_book(self, title, author, isbn, copies=1):
            """Add a book to the library"""
            if isbn in self.books:
                self.books[isbn].total_copies += copies
                self.books[isbn].available_copies += copies
                return f"Added {copies} more copies of '{title}'"
            else:
                self.books[isbn] = Book(title, author, isbn, copies)
                return f"Added new book: '{title}'"
        
        def register_member(self, name):
            """Register a new library member"""
            if name not in self.members:
                self.members.add(name)
                return f"Welcome, {name}! You are now a library member."
            return f"{name} is already a member"
        
        def borrow_book(self, isbn, borrower_name):
            """Allow member to borrow a book"""
            if borrower_name not in self.members:
                return f"{borrower_name} is not a library member"
            
            if isbn in self.books:
                return self.books[isbn].borrow(borrower_name)
            return "Book not found in library"
        
        def return_book(self, isbn, borrower_name):
            """Process book return"""
            if isbn in self.books:
                return self.books[isbn].return_book(borrower_name)
            return "Book not found in library"
        
        def search_books(self, keyword):
            """Search for books by title or author"""
            keyword = keyword.lower()
            results = []
            for book in self.books.values():
                if keyword in book.title.lower() or keyword in book.author.lower():
                    results.append(book)
            return results
        
        def get_statistics(self):
            """Get library statistics"""
            total_books = sum(book.total_copies for book in self.books.values())
            available_books = sum(book.available_copies for book in self.books.values())
            borrowed_books = total_books - available_books
            
            return {
                'total_titles': len(self.books),
                'total_books': total_books,
                'available_books': available_books,
                'borrowed_books': borrowed_books,
                'total_members': len(self.members)
            }
    
    # Test the library system
    library = Library("City Central Library")
    
    # Add books
    print(library.add_book("1984", "George Orwell", "978-0-452-28423-4", 3))
    print(library.add_book("To Kill a Mockingbird", "Harper Lee", "978-0-06-112008-4", 2))
    print(library.add_book("The Great Gatsby", "F. Scott Fitzgerald", "978-0-7432-7356-5", 1))
    
    # Register members
    print(library.register_member("Alice"))
    print(library.register_member("Bob"))
    
    # Borrow books
    print(library.borrow_book("978-0-452-28423-4", "Alice"))
    print(library.borrow_book("978-0-452-28423-4", "Bob"))
    
    # Show statistics
    stats = library.get_statistics()
    print(f"\nLibrary Statistics:")
    for key, value in stats.items():
        print(f"  {key.replace('_', ' ').title()}: {value}")
    
    print("\nEXERCISE 4.2: Banking System with Inheritance")
    print("-" * 45)
    
    class BankAccount:
        """Base bank account class"""
        
        def __init__(self, account_number, holder_name, initial_balance=0):
            # TODO: Complete the BankAccount class
            self.account_number = account_number
            self.holder_name = holder_name
            self.balance = initial_balance
            self.transaction_history = []
            self._add_transaction("Account opened", initial_balance)
        
        def _add_transaction(self, description, amount):
            """Private method to record transactions"""
            transaction = {
                'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'description': description,
                'amount': amount,
                'balance': self.balance
            }
            self.transaction_history.append(transaction)
        
        def deposit(self, amount):
            """Deposit money to account"""
            if amount > 0:
                self.balance += amount
                self._add_transaction(f"Deposit", amount)
                return f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}"
            return "Invalid deposit amount"
        
        def withdraw(self, amount):
            """Withdraw money from account"""
            if amount > 0 and amount <= self.balance:
                self.balance -= amount
                self._add_transaction(f"Withdrawal", -amount)
                return f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}"
            return "Insufficient funds or invalid amount"
        
        def get_balance(self):
            """Get current balance"""
            return self.balance
        
        def __str__(self):
            return f"Account {self.account_number}: {self.holder_name} - Balance: ${self.balance:.2f}"
    
    class SavingsAccount(BankAccount):
        """Savings account with interest"""
        
        def __init__(self, account_number, holder_name, initial_balance=0, interest_rate=0.02):
            # TODO: Complete SavingsAccount with inheritance
            super().__init__(account_number, holder_name, initial_balance)
            self.interest_rate = interest_rate
            self.minimum_balance = 100
        
        def withdraw(self, amount):
            """Override withdraw to enforce minimum balance"""
            if self.balance - amount < self.minimum_balance:
                return f"Cannot withdraw. Minimum balance of ${self.minimum_balance} required"
            return super().withdraw(amount)
        
        def calculate_interest(self):
            """Calculate and add monthly interest"""
            interest = self.balance * (self.interest_rate / 12)
            self.balance += interest
            self._add_transaction("Interest earned", interest)
            return f"Interest earned: ${interest:.2f}"
    
    class CheckingAccount(BankAccount):
        """Checking account with overdraft protection"""
        
        def __init__(self, account_number, holder_name, initial_balance=0, overdraft_limit=500):
            # TODO: Complete CheckingAccount
            super().__init__(account_number, holder_name, initial_balance)
            self.overdraft_limit = overdraft_limit
        
        def withdraw(self, amount):
            """Override withdraw to allow overdraft"""
            if amount <= self.balance + self.overdraft_limit:
                self.balance -= amount
                self._add_transaction("Withdrawal", -amount)
                if self.balance < 0:
                    return f"Withdrew ${amount:.2f}. Overdraft: ${-self.balance:.2f}"
                return f"Withdrew ${amount:.2f}. Balance: ${self.balance:.2f}"
            return "Exceeds overdraft limit"
    
    # Test the banking system
    savings = SavingsAccount("SAV001", "Alice Johnson", 1000, 0.03)
    checking = CheckingAccount("CHK001", "Bob Smith", 500, 1000)
    
    print(f"Created accounts:")
    print(f"  {savings}")
    print(f"  {checking}")
    
    # Test transactions
    print(f"\nTesting transactions:")
    print(savings.deposit(200))
    print(savings.calculate_interest())
    print(checking.withdraw(800))  # This should trigger overdraft

# =============================================================================
# EXERCISE SET 5: INTEGRATED CHALLENGE
# =============================================================================

def exercise_set_5():
    """
    Integrated challenge combining all concepts
    """
    print("\n" + "="*50)
    print("EXERCISE SET 5: INTEGRATED CHALLENGE")
    print("="*50)
    
    print("\nCHALLENGE: Build a Student Management System")
    print("-" * 45)
    print("This challenge combines all concepts learned:")
    print("- Classes and inheritance (OOP)")
    print("- File handling for data persistence")
    print("- Comprehensions for data processing")
    print("- Control structures for logic")
    print("- Error handling for robustness")
    
    class Student:
        """Student class with grades management"""
        
        def __init__(self, student_id, name, email):
            self.student_id = student_id
            self.name = name
            self.email = email
            self.grades = {}  # subject: [list of grades]
            self.enrollment_date = datetime.now().isoformat()
        
        def add_grade(self, subject, grade):
            """Add a grade for a subject"""
            if 0 <= grade <= 100:
                if subject not in self.grades:
                    self.grades[subject] = []
                self.grades[subject].append(grade)
                return True
            return False
        
        def get_average(self, subject=None):
            """Get average grade for a subject or overall"""
            if subject:
                if subject in self.grades and self.grades[subject]:
                    return sum(self.grades[subject]) / len(self.grades[subject])
                return 0
            
            # Overall average
            all_grades = [grade for grades_list in self.grades.values() for grade in grades_list]
            return sum(all_grades) / len(all_grades) if all_grades else 0
        
        def get_letter_grade(self, average):
            """Convert numerical average to letter grade"""
            if average >= 90:
                return 'A'
            elif average >= 80:
                return 'B'
            elif average >= 70:
                return 'C'
            elif average >= 60:
                return 'D'
            else:
                return 'F'
        
        def to_dict(self):
            """Convert student to dictionary for JSON serialization"""
            return {
                'student_id': self.student_id,
                'name': self.name,
                'email': self.email,
                'grades': self.grades,
                'enrollment_date': self.enrollment_date
            }
        
        @classmethod
        def from_dict(cls, data):
            """Create student from dictionary"""
            student = cls(data['student_id'], data['name'], data['email'])
            student.grades = data['grades']
            student.enrollment_date = data['enrollment_date']
            return student
    
    class StudentManagementSystem:
        """Complete student management system"""
        
        def __init__(self, filename="students.json"):
            self.filename = filename
            self.students = {}  # student_id: Student object
            self.load_students()
        
        def load_students(self):
            """Load students from file"""
            try:
                with open(self.filename, 'r') as file:
                    data = json.load(file)
                    for student_data in data.get('students', []):
                        student = Student.from_dict(student_data)
                        self.students[student.student_id] = student
                print(f"Loaded {len(self.students)} students from {self.filename}")
            except FileNotFoundError:
                print("No existing student file. Starting fresh.")
            except Exception as e:
                print(f"Error loading students: {e}")
        
        def save_students(self):
            """Save students to file"""
            try:
                data = {
                    'students': [student.to_dict() for student in self.students.values()],
                    'last_updated': datetime.now().isoformat()
                }
                with open(self.filename, 'w') as file:
                    json.dump(data, file, indent=2)
                return True
            except Exception as e:
                print(f"Error saving students: {e}")
                return False
        
        def add_student(self, student_id, name, email):
            """Add a new student"""
            if student_id in self.students:
                return f"Student ID {student_id} already exists"
            
            student = Student(student_id, name, email)
            self.students[student_id] = student
            self.save_students()
            return f"Added student: {name}"
        
        def add_grade(self, student_id, subject, grade):
            """Add grade for a student"""
            if student_id not in self.students:
                return f"Student ID {student_id} not found"
            
            if self.students[student_id].add_grade(subject, grade):
                self.save_students()
                return f"Added grade {grade} for {subject} to student {student_id}"
            return "Invalid grade (must be 0-100)"
        
        def get_student_report(self, student_id):
            """Generate comprehensive student report"""
            if student_id not in self.students:
                return f"Student ID {student_id} not found"
            
            student = self.students[student_id]
            report = f"\nSTUDENT REPORT\n"
            report += f"Name: {student.name}\n"
            report += f"ID: {student.student_id}\n"
            report += f"Email: {student.email}\n"
            report += f"Enrolled: {student.enrollment_date[:10]}\n\n"
            
            if student.grades:
                report += "GRADES BY SUBJECT:\n"
                for subject, grades in student.grades.items():
                    avg = student.get_average(subject)
                    letter = student.get_letter_grade(avg)
                    report += f"  {subject}: {grades} → Avg: {avg:.1f} ({letter})\n"
                
                overall_avg = student.get_average()
                overall_letter = student.get_letter_grade(overall_avg)
                report += f"\nOVERALL AVERAGE: {overall_avg:.1f} ({overall_letter})"
            else:
                report += "No grades recorded"
            
            return report
        
        def get_class_statistics(self):
            """Generate class-wide statistics using comprehensions"""
            if not self.students:
                return "No students enrolled"
            
            # Use comprehensions for analysis
            all_averages = [student.get_average() for student in self.students.values() 
                           if student.get_average() > 0]
            
            subject_averages = {}
            all_subjects = set()
            for student in self.students.values():
                all_subjects.update(student.grades.keys())
            
            for subject in all_subjects:
                subject_grades = [student.get_average(subject) for student in self.students.values() 
                                if student.get_average(subject) > 0]
                if subject_grades:
                    subject_averages[subject] = sum(subject_grades) / len(subject_grades)
            
            # Grade distribution
            grade_distribution = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0}
            for avg in all_averages:
                letter = self.students[list(self.students.keys())[0]].get_letter_grade(avg)
                grade_distribution[letter] += 1
            
            stats = f"\nCLASS STATISTICS\n"
            stats += f"Total Students: {len(self.students)}\n"
            
            if all_averages:
                stats += f"Class Average: {sum(all_averages)/len(all_averages):.1f}\n"
                stats += f"Highest Average: {max(all_averages):.1f}\n"
                stats += f"Lowest Average: {min(all_averages):.1f}\n\n"
                
                stats += "GRADE DISTRIBUTION:\n"
                for grade, count in grade_distribution.items():
                    percentage = (count / len(all_averages)) * 100
                    stats += f"  {grade}: {count} students ({percentage:.1f}%)\n"
                
                if subject_averages:
                    stats += "\nSUBJECT AVERAGES:\n"
                    for subject, avg in sorted(subject_averages.items()):
                        stats += f"  {subject}: {avg:.1f}\n"
            
            return stats
    
    # Demonstrate the integrated system
    print("\nCreating Student Management System...")
    sms = StudentManagementSystem("demo_students.json")
    
    # Add students
    print(sms.add_student("S001", "Alice Johnson", "alice@email.com"))
    print(sms.add_student("S002", "Bob Smith", "bob@email.com"))
    print(sms.add_student("S003", "Charlie Brown", "charlie@email.com"))
    
    # Add grades
    subjects = ["Math", "Science", "English", "History"]
    grades_data = [
        ("S001", [("Math", 95), ("Science", 88), ("English", 92), ("History", 90)]),
        ("S002", [("Math", 78), ("Science", 82), ("English", 85), ("History", 80)]),
        ("S003", [("Math", 88), ("Science", 91), ("English", 87), ("History", 89)])
    ]
    
    for student_id, subject_grades in grades_data:
        for subject, grade in subject_grades:
            print(sms.add_grade(student_id, subject, grade))
    
    # Generate reports
    print(sms.get_student_report("S001"))
    print(sms.get_class_statistics())
    
    print("\nIntegrated challenge completed successfully!")
    print("You've demonstrated mastery of all Python fundamentals!")

# =============================================================================
# MAIN WORKBOOK EXECUTION
# =============================================================================

def main():
    """
    Run all practice exercises
    """
    print("Welcome to the Python Fundamentals Practice Workbook!")
    print("Complete these exercises to reinforce your learning.")
    
    try:
        # Run all exercise sets
        exercise_set_1()  # Control Structures
        exercise_set_2()  # File Handling  
        exercise_set_3()  # Comprehensions
        exercise_set_4()  # Object-Oriented Programming
        exercise_set_5()  # Integrated Challenge
        
        print("\n" + "="*60)
        print("CONGRATULATIONS! WORKBOOK COMPLETED!")
        print("="*60)
        
        print("\nYou have successfully practiced:")
        skills = [
            "✓ Control structures and conditional logic",
            "✓ File handling and data persistence",
            "✓ List and dictionary comprehensions",
            "✓ Object-oriented programming concepts",
            "✓ Error handling and debugging",
            "✓ Integration of multiple Python concepts"
        ]
        
        for skill in skills:
            print(f"  {skill}")
        
        print("\nNext Steps:")
        print("• Apply these skills to real projects")
        print("• Explore advanced Python libraries")
        print("• Build more complex applications")
        print("• Continue with AI/ML specific modules")
        
    except Exception as e:
        print(f"Error in workbook execution: {e}")
        print("Please review the code and try again.")

if __name__ == "__main__":
    main()
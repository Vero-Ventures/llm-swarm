# Calculate Fibonacci sequence
def fibonacci(n):
    current, next_value = 0, 1
    for _ in range(n):
        current, next_value = next_value, current + next_value
    return current

# Merge two sorted lists
def merge(sorted_list1, sorted_list2):
    merged_list = []
    index1, index2 = 0, 0
    while index1 < len(sorted_list1) and index2 < len(sorted_list2):
        if sorted_list1[index1] < sorted_list2[index2]:
            merged_list.append(sorted_list1[index1])
            index1 += 1
        else:
            merged_list.append(sorted_list2[index2])
            index2 += 1
    merged_list.extend(sorted_list1[index1:])
    merged_list.extend(sorted_list2[index2:])
    return merged_list

# Find the greatest common divisor using Euclid's algorithm
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Find the maximum subarray sum (Kadane's algorithm)
def max_subarray_sum(array):
    max_sum, current_sum = float('-inf'), 0
    for number in array:
        current_sum = max(number, current_sum + number)
        max_sum = max(max_sum, current_sum)
    return max_sum

# Calculate factorial recursively
def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)


# Reading and processing a CSV file
import csv

def read_csv(filepath):
    with open(filepath, mode='r') as file:
        reader = csv.reader(file)
        headers = next(reader)
        data = [dict(zip(headers, row)) for row in reader]
    return data

# Connecting to a database and executing a query
import sqlite3

def execute_query(database, sql):
    with sqlite3.connect(database) as conn:
        cursor = conn.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
    return result

# Sending an email using SMTP
import smtplib

def send_email(user, password, to_address, message):
    server = smtplib.SMTP('smtp.example.com', 587)
    server.starttls()
    server.login(user, password)
    server.sendmail(user, to_address, message)
    server.quit()

# Fetching JSON data from a web API
import requests

def fetch_json(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {}

# Performing a file search with regex
import os
import re

def search_files(path, regex):
    pattern = re.compile(regex)
    matched_files = []
    for dirpath, _, filenames in os.walk(path):
        for filename in filenames:
            if pattern.search(filename):
                matched_files.append(os.path.join(dirpath, filename))
    return matched_files

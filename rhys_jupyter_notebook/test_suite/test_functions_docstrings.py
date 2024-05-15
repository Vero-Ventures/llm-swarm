import csv
import os
import re
import smtplib
import sqlite3

import requests


def fibonacci(n):
    """
    Calculate the nth Fibonacci number using an iterative approach.

    Parameters:
        n (int): The position in the Fibonacci sequence to compute.

    Returns:
        int: The nth Fibonacci number.
    """
    current, next_value = 0, 1
    for _ in range(n):
        current, next_value = next_value, current + next_value
    return current

def merge(sorted_list1, sorted_list2):
    """
    Merge two sorted lists into a single sorted list.

    Parameters:
        sorted_list1 (list): The first sorted list.
        sorted_list2 (list): The second sorted list.

    Returns:
        list: A merged and sorted list containing all elements from both input lists.
    """
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

def gcd(a, b):
    """
    Compute the greatest common divisor (GCD) of two numbers using Euclid's algorithm.

    Parameters:
        a (int): The first number.
        b (int): The second number.

    Returns:
        int: The greatest common divisor of a and b.
    """
    while b != 0:
        a, b = b, a % b
    return a

def max_subarray_sum(array):
    """
    Find the maximum sum of any contiguous subarray within the given array using Kadane's algorithm.

    Parameters:
        array (list of int): List of integers, possibly including negative numbers.

    Returns:
        int: The maximum sum of any contiguous subarray.
    """
    max_sum, current_sum = float('-inf'), 0
    for number in array:
        current_sum = max(number, current_sum + number)
        max_sum = max(max_sum, current_sum)
    return max_sum

def factorial(n):
    """
    Calculate the factorial of a non-negative integer recursively.

    Parameters:
        n (int): The number to calculate the factorial of.

    Returns:
        int: The factorial of n.
    """
    return 1 if n == 0 else n * factorial(n - 1)

def read_csv(filepath):
    """
    Read a CSV file and return a list of dictionaries, each representing a row.

    Parameters:
        filepath (str): The path to the CSV file.

    Returns:
        list of dict: A list of dictionaries keyed by the headers of the CSV with corresponding row values.
    """
    with open(filepath, mode='r') as file:
        reader = csv.reader(file)
        headers = next(reader)
        data = [dict(zip(headers, row)) for row in reader]
    return data

def execute_query(database, sql):
    """
    Execute a SQL query on a SQLite database and return the results.

    Parameters:
        database (str): The path to the SQLite database file.
        sql (str): The SQL query string.

    Returns:
        list of tuple: The results of the SQL query.
    """
    with sqlite3.connect(database) as conn:
        cursor = conn.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
    return result

def send_email(user, password, to_address, message):
    """
    Send an email using SMTP protocol.

    Parameters:
        user (str): The SMTP username (email address).
        password (str): The SMTP password.
        to_address (str): The recipient's email address.
        message (str): The email message to send.
    """
    server = smtplib.SMTP('smtp.example.com', 587)
    server.starttls()
    server.login(user, password)
    server.sendmail(user, to_address, message)
    server.quit()

def fetch_json(url):
    """
    Fetch JSON data from a URL using an HTTP GET request.

    Parameters:
        url (str): The URL to fetch data from.

    Returns:
        dict or list: The JSON parsed response, or an empty dictionary if the request fails.
    """
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {}

def search_files(path, regex):
    """
    Search for files in a given directory that match a regular expression.

    Parameters:
        path (str): The path to the directory where files are searched.
        regex (str): The regular expression pattern to match filenames against.

    Returns:
        list of str: A list of file paths that match the regex pattern.
    """
    pattern = re.compile(regex)
    matched_files = []
    for dirpath, _, filenames in os.walk(path):
        for filename in filenames:
            if pattern.search(filename):
                matched_files.append(os.path.join(dirpath, filename))
    return matched_files

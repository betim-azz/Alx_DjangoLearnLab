#!/usr/bin/env python
"""
Test script for Social Media API authentication endpoints
Run this after starting the development server
"""
import requests
import json
import sys

BASE_URL = "http://127.0.0.1:8000"

def test_register():
    """Test user registration"""
    print("\n1. Testing User Registration...")
    url = f"{BASE_URL}/api/accounts/register/"
    data = {
        "username": "testuser123",
        "email": "test123@example.com",
        "password": "testpass123",
        "bio": "Test user bio"
    }
    
    try:
        response = requests.post(url, json=data)
        if response.status_code == 201:
            print("✓ Registration successful!")
            print(f"  User: {response.json()['username']}")
            return True
        else:
            print(f"✗ Registration failed: {response.status_code}")
            print(f"  Error: {response.json()}")
            return False
    except Exception as e:
        print(f"✗ Error: {e}")
        return False

def test_login():
    """Test user login"""
    print("\n2. Testing User Login...")
    url = f"{BASE_URL}/api/accounts/login/"
    data = {
        "username": "testuser123",
        "password": "testpass123"
    }
    
    try:
        response = requests.post(url, json=data)
        if response.status_code == 200:
            token = response.json()['token']
            print("✓ Login successful!")
            print(f"  Token: {token[:20]}...")
            return token
        else:
            print(f"✗ Login failed: {response.status_code}")
            print(f"  Error: {response.json()}")
            return None
    except Exception as e:
        print(f"✗ Error: {e}")
        return None

def test_profile(token):
    """Test profile retrieval"""
    print("\n3. Testing Profile Retrieval...")
    url = f"{BASE_URL}/api/accounts/profile/"
    headers = {"Authorization": f"Token {token}"}
    
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            profile = response.json()
            print("✓ Profile retrieved successfully!")
            print(f"  Username: {profile['username']}")
            print(f"  Email: {profile['email']}")
            print(f"  Bio: {profile.get('bio', 'N/A')}")
            return True
        else:
            print(f"✗ Profile retrieval failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"✗ Error: {e}")
        return False

def test_profile_update(token):
    """Test profile update"""
    print("\n4. Testing Profile Update...")
    url = f"{BASE_URL}/api/accounts/profile/"
    headers = {"Authorization": f"Token {token}"}
    data = {
        "bio": "Updated bio from test script"
    }
    
    try:
        response = requests.put(url, json=data, headers=headers)
        if response.status_code == 200:
            print("✓ Profile updated successfully!")
            print(f"  New bio: {response.json()['bio']}")
            return True
        else:
            print(f"✗ Profile update failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"✗ Error: {e}")
        return False

def main():
    print("=" * 50)
    print("Social Media API - Authentication Tests")
    print("=" * 50)
    print("\nMake sure the development server is running:")
    print("  python manage.py runserver")
    print("\nStarting tests...")
    
    # Test registration
    if not test_register():
        print("\n⚠ Registration test failed. User might already exist.")
        print("  Continuing with login test...")
    
    # Test login
    token = test_login()
    if not token:
        print("\n✗ Cannot continue without valid token")
        sys.exit(1)
    
    # Test profile retrieval
    test_profile(token)
    
    # Test profile update
    test_profile_update(token)
    
    print("\n" + "=" * 50)
    print("Tests completed!")
    print("=" * 50)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nTests interrupted by user")
        sys.exit(0)
    except requests.exceptions.ConnectionError:
        print("\n✗ Error: Cannot connect to server")
        print("  Make sure the development server is running:")
        print("  python manage.py runserver")
        sys.exit(1)

#!/usr/bin/env python3
"""
Simple server test script
"""

import requests
import time

def test_server():
    """Test if the server is responding"""
    print("Testing server connection...")
    
    try:
        # Test root endpoint
        response = requests.get("http://127.0.0.1:8000/", timeout=5)
        print(f"✅ Server is running! Status: {response.status_code}")
        print(f"Response: {response.json()}")
        return True
    except requests.exceptions.ConnectionError:
        print("❌ Server is not running or not accessible")
        return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

if __name__ == "__main__":
    # Wait a bit for server to start
    print("Waiting 3 seconds for server to start...")
    time.sleep(3)
    test_server() 
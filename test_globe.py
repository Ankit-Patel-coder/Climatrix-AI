#!/usr/bin/env python3
"""
Test script for the 3D Weather Globe
Opens the globe visualization in a browser
"""

import webbrowser
import time
import os
from pathlib import Path

def test_globe():
    """Test the globe visualization"""
    print("🌍 Testing 3D Weather Globe...")
    
    # Get the path to the globe HTML file
    globe_path = Path("frontend/globe.html").absolute()
    
    if not globe_path.exists():
        print("❌ Globe HTML file not found!")
        return False
    
    print(f"📁 Globe file found: {globe_path}")
    
    # Check if required files exist
    required_files = [
        "frontend/js/weather-globe.js",
        "frontend/js/globe.js"
    ]
    
    for file_path in required_files:
        if not Path(file_path).exists():
            print(f"⚠️ Warning: {file_path} not found")
    
    # Open the globe in browser
    try:
        globe_url = f"file://{globe_path}"
        print(f"🌐 Opening globe at: {globe_url}")
        webbrowser.open(globe_url)
        
        print("✅ Globe opened successfully!")
        print("📋 Features to test:")
        print("   - 3D Earth rotation")
        print("   - Interactive controls (mouse/touch)")
        print("   - Rain particle effects")
        print("   - Cyclone markers (pulsing)")
        print("   - Drought area indicators")
        print("   - Toggle buttons for rain/clouds")
        print("   - Real-time data panel")
        print("   - Legend display")
        
        return True
        
    except Exception as e:
        print(f"❌ Failed to open globe: {e}")
        return False

def test_api_endpoints():
    """Test the weather API endpoints"""
    print("\n🔌 Testing Weather API Endpoints...")
    
    import requests
    import json
    
    base_url = "http://localhost:8000/api/v1/weather"
    
    endpoints = [
        "/current",
        "/cyclones", 
        "/drought",
        "/rainfall",
        "/stats",
        "/forecast/24"
    ]
    
    for endpoint in endpoints:
        try:
            url = f"{base_url}{endpoint}"
            print(f"📡 Testing: {url}")
            
            response = requests.get(url, timeout=5)
            
            if response.status_code == 200:
                data = response.json()
                print(f"   ✅ Success: {len(str(data))} bytes")
            else:
                print(f"   ❌ Failed: {response.status_code}")
                
        except requests.exceptions.RequestException as e:
            print(f"   ❌ Error: {e}")
        except Exception as e:
            print(f"   ❌ Unexpected error: {e}")

if __name__ == "__main__":
    print("=" * 60)
    print("🌍 3D WEATHER GLOBE TEST")
    print("=" * 60)
    
    # Test globe visualization
    globe_success = test_globe()
    
    # Test API endpoints
    test_api_endpoints()
    
    print("\n" + "=" * 60)
    if globe_success:
        print("🎉 Globe test completed successfully!")
        print("🌐 The globe should now be open in your browser")
    else:
        print("❌ Globe test failed")
    print("=" * 60) 
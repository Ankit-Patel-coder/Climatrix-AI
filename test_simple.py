#!/usr/bin/env python3
"""
Simple Test Script for AI Climate Resilience System
Tests basic functionality without complex dependencies
"""

import requests
import json
import time

def test_api():
    """Test the API endpoints"""
    base_url = "http://localhost:8000"
    
    print("🧪 Testing AI Climate Resilience API")
    print("=" * 40)
    
    # Test 1: Root endpoint
    print("\n1️⃣ Testing root endpoint...")
    try:
        response = requests.get(f"{base_url}/")
        if response.status_code == 200:
            data = response.json()
            print(f"   ✅ Root endpoint: {data.get('message', 'OK')}")
        else:
            print(f"   ❌ Root endpoint failed: {response.status_code}")
    except Exception as e:
        print(f"   ❌ Root endpoint error: {e}")
    
    # Test 2: System status
    print("\n2️⃣ Testing system status...")
    try:
        response = requests.get(f"{base_url}/api/v1/status")
        if response.status_code == 200:
            data = response.json()
            print(f"   ✅ System status: {data.get('status', 'Unknown')}")
            print(f"   📊 Models loaded: {data.get('models_loaded', False)}")
        else:
            print(f"   ❌ System status failed: {response.status_code}")
    except Exception as e:
        print(f"   ❌ System status error: {e}")
    
    # Test 3: Flood prediction
    print("\n3️⃣ Testing flood prediction...")
    try:
        payload = {
            "location": {
                "latitude": 25.7617,
                "longitude": -80.1918,
                "radius_km": 50.0
            },
            "disaster_type": "flood",
            "prediction_horizon_hours": 24
        }
        
        response = requests.post(f"{base_url}/api/v1/predict", json=payload)
        if response.status_code == 200:
            data = response.json()
            print(f"   ✅ Flood prediction: {data.get('risk_level', 'Unknown')} risk")
            print(f"   📊 Probability: {data.get('probability', 0):.1%}")
            print(f"   🎯 Confidence: {data.get('confidence', 0):.1%}")
        else:
            print(f"   ❌ Flood prediction failed: {response.status_code}")
            print(f"   📝 Error: {response.text}")
    except Exception as e:
        print(f"   ❌ Flood prediction error: {e}")
    
    # Test 4: Drought prediction
    print("\n4️⃣ Testing drought prediction...")
    try:
        payload = {
            "location": {
                "latitude": 29.7604,
                "longitude": -95.3698,
                "radius_km": 50.0
            },
            "disaster_type": "drought",
            "prediction_horizon_hours": 24
        }
        
        response = requests.post(f"{base_url}/api/v1/predict", json=payload)
        if response.status_code == 200:
            data = response.json()
            print(f"   ✅ Drought prediction: {data.get('risk_level', 'Unknown')} risk")
            print(f"   📊 Probability: {data.get('probability', 0):.1%}")
            print(f"   🎯 Confidence: {data.get('confidence', 0):.1%}")
        else:
            print(f"   ❌ Drought prediction failed: {response.status_code}")
    except Exception as e:
        print(f"   ❌ Drought prediction error: {e}")
    
    # Test 5: Cyclone prediction
    print("\n5️⃣ Testing cyclone prediction...")
    try:
        payload = {
            "location": {
                "latitude": 18.2208,
                "longitude": -66.5901,
                "radius_km": 50.0
            },
            "disaster_type": "cyclone",
            "prediction_horizon_hours": 24
        }
        
        response = requests.post(f"{base_url}/api/v1/predict", json=payload)
        if response.status_code == 200:
            data = response.json()
            print(f"   ✅ Cyclone prediction: {data.get('risk_level', 'Unknown')} risk")
            print(f"   📊 Probability: {data.get('probability', 0):.1%}")
            print(f"   🎯 Confidence: {data.get('confidence', 0):.1%}")
        else:
            print(f"   ❌ Cyclone prediction failed: {response.status_code}")
    except Exception as e:
        print(f"   ❌ Cyclone prediction error: {e}")
    
    print("\n" + "=" * 40)
    print("🎯 API Testing Completed!")
    print("=" * 40)
    print("\n📋 Next Steps:")
    print("   1. Open frontend: frontend/index.html")
    print("   2. View API docs: http://localhost:8000/docs")
    print("   3. Test more endpoints manually")

if __name__ == "__main__":
    # Wait a bit for server to start
    print("⏳ Waiting for server to start...")
    time.sleep(3)
    test_api() 
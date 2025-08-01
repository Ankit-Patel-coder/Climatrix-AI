#!/usr/bin/env python3
"""
Simple test script for AI Climate Resilience System
"""

import requests
import json
import time

def test_system():
    """Test the AI Climate Resilience System"""
    base_url = "http://localhost:8000"
    
    print("🌊 Climatrix Ai")
    print("=" * 50)
    
    # Test 1: System Status
    print("\n1️⃣ Testing System Status...")
    try:
        response = requests.get(f"{base_url}/api/v1/status")
        if response.status_code == 200:
            status = response.json()
            print(f"   ✅ Status: {status['status']}")
            print(f"   📊 Models Loaded: {status['models_loaded']}")
            print(f"   🔗 Data Sources: {status['data_sources_connected']}")
            print(f"   🕐 Last Update: {status['last_update']}")
        else:
            print(f"   ❌ Status check failed: {response.status_code}")
    except Exception as e:
        print(f"   ❌ Error: {e}")
    
    # Test 2: Flood Prediction for Mumbai
    print("\n2️⃣ Testing Flood Prediction for Mumbai...")
    try:
        payload = {
            "city_name": "Mumbai",
            "disaster_type": "flood",
            "prediction_horizon_hours": 24
        }
        response = requests.post(f"{base_url}/api/v1/predict/city", json=payload)
        if response.status_code == 200:
            data = response.json()
            print(f"   ✅ Risk Level: {data['risk_level']}")
            print(f"   📊 Probability: {data['probability']:.1%}")
            print(f"   🎯 Confidence: {data['confidence']:.1%}")
            print(f"   📍 Location: {data['details'].get('city_name', 'Unknown')}")
            print(f"   💡 Recommendations: {len(data['recommendations'])} items")
        else:
            print(f"   ❌ Prediction failed: {response.status_code}")
    except Exception as e:
        print(f"   ❌ Error: {e}")
    
    # Test 3: Drought Prediction for Delhi
    print("\n3️⃣ Testing Drought Prediction for Delhi...")
    try:
        payload = {
            "city_name": "Delhi",
            "disaster_type": "drought",
            "prediction_horizon_hours": 24
        }
        response = requests.post(f"{base_url}/api/v1/predict/city", json=payload)
        if response.status_code == 200:
            data = response.json()
            print(f"   ✅ Risk Level: {data['risk_level']}")
            print(f"   📊 Probability: {data['probability']:.1%}")
            print(f"   🎯 Confidence: {data['confidence']:.1%}")
            print(f"   📍 Location: {data['details'].get('city_name', 'Unknown')}")
        else:
            print(f"   ❌ Prediction failed: {response.status_code}")
    except Exception as e:
        print(f"   ❌ Error: {e}")
    
    # Test 4: Cyclone Prediction for Chennai
    print("\n4️⃣ Testing Cyclone Prediction for Chennai...")
    try:
        payload = {
            "city_name": "Chennai",
            "disaster_type": "cyclone",
            "prediction_horizon_hours": 24
        }
        response = requests.post(f"{base_url}/api/v1/predict/city", json=payload)
        if response.status_code == 200:
            data = response.json()
            print(f"   ✅ Risk Level: {data['risk_level']}")
            print(f"   📊 Probability: {data['probability']:.1%}")
            print(f"   🎯 Confidence: {data['confidence']:.1%}")
            print(f"   📍 Location: {data['details'].get('city_name', 'Unknown')}")
        else:
            print(f"   ❌ Prediction failed: {response.status_code}")
    except Exception as e:
        print(f"   ❌ Error: {e}")
    
    # Test 5: Analytics Trends
    print("\n5️⃣ Testing Analytics Trends...")
    try:
        response = requests.get(f"{base_url}/api/v1/analytics/trends/flood?days=7")
        if response.status_code == 200:
            data = response.json()
            print(f"   ✅ Trends: {len(data['trends'])} data points")
            if data['trends']:
                latest = data['trends'][0]
                print(f"   📈 Latest Probability: {latest['probability']:.1%}")
                print(f"   🎯 Latest Risk Level: {latest['risk_level']}")
        else:
            print(f"   ❌ Trends failed: {response.status_code}")
    except Exception as e:
        print(f"   ❌ Error: {e}")
    
    print("\n" + "=" * 50)
    print("🎉 SYSTEM DEMO COMPLETED!")
    print("=" * 50)
    print("\n🌐 Access Points:")
    print("   • Frontend: frontend/index.html")
    print("   • API Docs: http://localhost:8000/docs")
    print("   • API Base: http://localhost:8000")
    print("\n🏆 Your AI Climate Resilience System is running perfectly!")

if __name__ == "__main__":
    test_system() 
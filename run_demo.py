#!/usr/bin/env python3
"""
Main Demo Runner for AI Climate Resilience System
Complete setup and demo for competition presentation
"""

import asyncio
import subprocess
import sys
import time
import os
from pathlib import Path


def print_banner():
    """Print demo banner"""
    print("🌊" * 60)
    print("🌊 Climatrix Ai 🌊")
    print("🌊" * 60)
    print("🏆 MAVERICK EFFECT AI CHALLENGE - COMPETITION DEMO 🏆")
    print("🌊" * 60)
    print()

def check_requirements():
    """Check if all requirements are installed"""
    print("🔍 Checking system requirements...")
    
    try:
        import fastapi
        import uvicorn
        import pandas
        import numpy
        import sklearn
        print("   ✅ All core Python packages installed")
    except ImportError as e:
        print(f"   ❌ Missing package: {e}")
        print("   📦 Run: pip install -r requirements.txt")
        return False
    
    # Check optional packages
    try:
        import asyncpg
        print("   ✅ PostgreSQL support available")
    except:
        print("   ⚠️ PostgreSQL not configured (will use simulated data)")
    
    try:
        import tensorflow
        print("   ✅ TensorFlow available (advanced models)")
    except:
        print("   ⚠️ TensorFlow not available (using simplified models)")
    
    return True

def setup_environment():
    """Setup environment variables"""
    print("⚙️ Setting up environment...")
    
    # Set default environment variables
    env_vars = {
        "DB_HOST": "localhost",
        "DB_PORT": "5432",
        "DB_NAME": "climate_resilience",
        "DB_USER": "postgres",
        "DB_PASSWORD": "password",
        "OPENWEATHER_API_KEY": "demo_key",
        "NASA_API_KEY": "demo_key"
    }
    
    for key, value in env_vars.items():
        if key not in os.environ:
            os.environ[key] = value
            print(f"   🔧 Set {key} = {value}")
    
    print("   ✅ Environment configured")

async def setup_database():
    """Setup database"""
    print("📊 Setting up database...")
    
    try:
        # Run database setup script
        result = subprocess.run([
            sys.executable, "scripts/setup_database.py"
        ], capture_output=True, text=True)
        
        if result.returncode == 0:
            print("   ✅ Database setup completed")
            return True
        else:
            print(f"   ⚠️ Database setup failed: {result.stderr}")
            print("   📝 Continuing with simulated data...")
            return False
    except Exception as e:
        print(f"   ⚠️ Database setup error: {e}")
        print("   📝 Continuing with simulated data...")
        return False

async def run_demo():
    """Run the complete demo"""
    print("🎬 Running comprehensive demo...")
    
    try:
        # Run demo script
        result = subprocess.run([
            sys.executable, "scripts/demo.py"
        ], capture_output=True, text=True)
        
        if result.returncode == 0:
            print("   ✅ Demo completed successfully")
            print(result.stdout)
        else:
            print(f"   ❌ Demo failed: {result.stderr}")
            return False
    except Exception as e:
        print(f"   ❌ Demo error: {e}")
        return False
    
    return True

async def test_api():
    """Test API endpoints"""
    print("🧪 Testing API endpoints...")
    
    try:
        # Run API test script
        result = subprocess.run([
            sys.executable, "scripts/test_api.py"
        ], capture_output=True, text=True)
        
        if result.returncode == 0:
            print("   ✅ API tests completed")
            print(result.stdout)
        else:
            print(f"   ⚠️ API tests failed: {result.stderr}")
            return False
    except Exception as e:
        print(f"   ⚠️ API test error: {e}")
        return False
    
    return True

def start_backend():
    """Start the backend server"""
    print("🚀 Starting backend server...")
    
    try:
        # Start FastAPI server
        process = subprocess.Popen([
            sys.executable, "-m", "uvicorn", 
            "backend.api.main:app", 
            "--host", "0.0.0.0", 
            "--port", "8000",
            "--reload"
        ], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        # Wait for server to start
        time.sleep(5)
        
        if process.poll() is None:
            print("   ✅ Backend server started on http://localhost:8000")
            print("   📖 API docs: http://localhost:8000/docs")
            return process
        else:
            print("   ❌ Backend server failed to start")
            return None
    except Exception as e:
        print(f"   ❌ Backend server error: {e}")
        return None

def open_frontend():
    """Open frontend in browser"""
    print("🌐 Opening frontend...")
    
    frontend_path = Path("frontend/index.html").absolute()
    
    try:
        import webbrowser
        webbrowser.open(f"file://{frontend_path}")
        print(f"   ✅ Frontend opened: {frontend_path}")
        return True
    except Exception as e:
        print(f"   ⚠️ Could not open frontend automatically: {e}")
        print(f"   📁 Please open manually: {frontend_path}")
        return False

async def main():
    """Main demo runner"""
    print_banner()
    
    # Check requirements
    if not check_requirements():
        print("❌ System requirements not met. Please install missing packages.")
        return
    
    # Setup environment
    setup_environment()
    
    # Setup database
    db_success = await setup_database()
    
    # Start backend server
    backend_process = start_backend()
    if not backend_process:
        print("❌ Could not start backend server")
        return
    
    try:
        # Wait a bit for server to fully start
        await asyncio.sleep(3)
        
        # Test API
        api_success = await test_api()
        
        # Run demo
        demo_success = await run_demo()
        
        # Open frontend
        frontend_success = open_frontend()
        
        print("\n" + "=" * 60)
        print("🎉 DEMO SETUP COMPLETED!")
        print("=" * 60)
        print()
        print("📋 System Status:")
        print(f"   Database: {'✅ Ready' if db_success else '⚠️ Simulated'}")
        print(f"   Backend: ✅ Running on http://localhost:8000")
        print(f"   API: {'✅ Working' if api_success else '⚠️ Issues'}")
        print(f"   Demo: {'✅ Completed' if demo_success else '❌ Failed'}")
        print(f"   Frontend: {'✅ Opened' if frontend_success else '📁 Manual'}")
        print()
        print("🎯 Next Steps:")
        print("   1. Test the frontend at: frontend/index.html")
        print("   2. View API docs at: http://localhost:8000/docs")
        print("   3. Run demo script: python scripts/demo.py")
        print("   4. Test API: python scripts/test_api.py")
        print()
        print("🏆 Ready for competition presentation!")
        print()
        print("Press Ctrl+C to stop the server...")
        
        # Keep server running
        await asyncio.sleep(3600)  # Run for 1 hour
        
    except KeyboardInterrupt:
        print("\n🛑 Stopping demo...")
    finally:
        if backend_process:
            backend_process.terminate()
            print("   ✅ Backend server stopped")

if __name__ == "__main__":
    asyncio.run(main()) 
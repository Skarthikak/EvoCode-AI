#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Screenshot Capture Helper for EvoCode-AI
Helps document and create screenshots for the README
"""

import os
import time
import subprocess

def run_command(cmd):
    """Run a shell command and return output"""
    try:
        result = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = result.communicate()
        return stdout.decode('utf-8'), stderr.decode('utf-8'), result.returncode
    except Exception as e:
        return "", str(e), 1

def generate_architecture_diagram():
    """Generate a simple architecture diagram using ASCII/dot"""
    diagram = """
    +-------------------+     +-------------------+     +-------------------+
    |   Phase 1:        |     |   Phase 2:        |     |   Phase 3:        |
    |  Initialization   | --> |   Development     | --> |   Testing        |
    +-------------------+     +-------------------+     +-------------------+
          |                         |                         |
          v                         v                         v
    +-------------------+     +-------------------+     +-------------------+
    |   Phase 4:        |     |   Phase 5:        |     |   Continuous     |
    |  Optimization     | --> |  Deployment       | --> |   Evolution      |
    +-------------------+     +-------------------+     +-------------------+
    """
    
    with open('docs/images/architecture.txt', 'w') as f:
        f.write("EvoCode-AI Architecture Diagram\\n")
        f.write("=" * 40 + "\\n")
        f.write(diagram)
    
    print("✅ Architecture diagram created: docs/images/architecture.txt")

def capture_terminal_demo():
    """Capture terminal output for demo screenshots"""
    print("🚀 Capturing terminal demo output...")
    
    # Run the final working test and capture output
    stdout, stderr, code = run_command("python final_working_test.py")
    
    with open('docs/images/demo-output.txt', 'w') as f:
        f.write("EvoCode-AI Demo Output\\n")
        f.write("=" * 40 + "\\n")
        f.write(stdout)
        if stderr:
            f.write("\\nERRORS:\\n")
            f.write(stderr)
    
    print("✅ Demo output captured: docs/images/demo-output.txt")

def create_screenshot_plan():
    """Create a plan for required screenshots"""
    plan = """
    📋 SCREENSHOT CAPTURE PLAN
    
    1. PROJECT BANNER (banner.png)
       - Create a 1200x600px banner with project name and tagline
       - Include EvoCode-AI logo and main features
       - Use consistent branding colors
    
    2. ARCHITECTURE DIAGRAM (architecture.png)
       - Create visual diagram of 5-phase process
       - Show data flow between components
       - Use tools: draw.io, Lucidchart, or Figma
    
    3. INSTALLATION PROCESS (installation.png)
       - Screenshot of git clone and setup commands
       - Show successful installation output
       - Terminal with syntax highlighting
    
    4. BASIC USAGE DEMO (basic-usage.gif)
       - Screen recording of basic workflow
       - Show project initialization and evolution
       - Animated GIF showing key steps
    
    5. PHASE SCREENSHOTS (phase1-5.png)
       - Individual screenshots for each phase
       - Show phase-specific interfaces and outputs
       - Consistent styling across all phases
    
    6. PERFORMANCE DASHBOARD (performance-dashboard.png)
       - Metrics visualization
       - Comparison charts
       - Real-time monitoring display
    
    7. TEST RESULTS (test-results.png)
       - Test execution output
       - Coverage reports
       - Verification results
    """
    
    with open('docs/images/screenshot_plan.txt', 'w') as f:
        f.write(plan)
    
    print("✅ Screenshot plan created: docs/images/screenshot_plan.txt")

def main():
    """Main function to setup screenshot documentation"""
    print("📸 EvoCode-AI Screenshot Setup")
    print("=" * 50)
    
    # Create docs/images directory
    os.makedirs('docs/images', exist_ok=True)
    
    # Generate documentation
    generate_architecture_diagram()
    capture_terminal_demo()
    create_screenshot_plan()
    
    print("\\n🎯 NEXT STEPS:")
    print("1. Review the generated files in docs/images/")
    print("2. Create actual screenshots using the plan as guide")
    print("3. Replace placeholder images with actual screenshots")
    print("4. Update README.md if image names change")
    print("\\n📝 Note: Currently using placeholder references.")
    print("   Replace these with actual PNG/GIF files when available.")

if __name__ == "__main__":
    main()

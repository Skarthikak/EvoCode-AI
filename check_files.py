import os
import sys

print("📁 FILE STRUCTURE VERIFICATION")
print("=" * 50)

# Check all expected files
expected_files = [
    "src/core/evo_assistant.py",
    "src/core/evolution_engine.py", 
    "src/core/advanced_ai.py",
    "src/core/ml_training_pipeline.py",
    "src/core/security.py",
    "src/adapters/collaboration_adapter.py",
    "src/interfaces/api_gateway.py",
    "src/interfaces/analytics_dashboard.py",
    "awards/final_submission_package.py",
    "ecosystem/marketplace.py",
    "scripts/market_analyzer.py",
    "scripts/advanced_market_analyzer.py",
    "scripts/performance_monitor.py",
    "scripts/process_testimonials.py"
]

found_count = 0

for file_path in expected_files:
    if os.path.exists(file_path):
        print("✅ " + file_path)
        found_count += 1
    else:
        print("❌ " + file_path + " - MISSING")

print("=" * 50)
print("FILES FOUND: " + str(found_count) + "/" + str(len(expected_files)))

if found_count == len(expected_files):
    print("🎉 ALL FILES PRESENT!")
else:
    print("⚠️  Some files are missing")

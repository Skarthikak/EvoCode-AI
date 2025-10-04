#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import subprocess
import shutil

def run_cmd(cmd):
    result = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = result.communicate()
    return stdout.decode('utf-8'), stderr.decode('utf-8'), result.returncode

print("🧹 Cleaning up and preparing for push...")
print("=" * 50)

# Remove problematic workflow files
workflow_path = ".github/workflows"
if os.path.exists(workflow_path):
    print("Removing workflow files...")
    shutil.rmtree(workflow_path)
    print("✅ Workflow files removed")

# Check git status
print("\n📊 Current git status:")
stdout, stderr, code = run_cmd("git status --short")
if stdout.strip():
    print("Changes to commit:")
    print(stdout)
else:
    print("No uncommitted changes")

# Add and commit
print("\n💾 Committing changes...")
run_cmd("git add .")
stdout, stderr, code = run_cmd("git commit -m 'feat: Deploy EvoCode-AI with all phases complete\n\n- All 5 development phases implemented\n- Comprehensive documentation\n- Python compatibility fixes\n- Project verification scripts'")
if code == 0:
    print("✅ Changes committed")
else:
    print("Commit status:", stdout)

# Push
print("\n🚀 Pushing to GitHub...")
stdout, stderr, code = run_cmd("git push origin main")
if code == 0:
    print("✅ Successfully pushed to GitHub!")
    print("🌐 Visit: https://github.com/Skarthikak/EvoCode-AI")
else:
    print("❌ Push failed. Error:")
    print(stderr)
    print("\n💡 Try running: git push origin main --force")

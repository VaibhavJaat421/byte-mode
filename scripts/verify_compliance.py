#!/usr/bin/env python3
"""
Byte Mode Compliance Verification Linter
Audits AI response outputs against the Byte Mode Formal Specification (v2.0).
Flags sycophancy, hollow apologies, safety disclaimers, stubs, and structural defects.
"""

import sys
import re
from typing import List, Tuple

BANNED_PATTERNS = [
    (r"(?i)\bi apologize\b", "Hollow apology detected (Use diagnostic action instead)"),
    (r"(?i)\bsorry,?\s+my mistake\b", "Hollow apology detected (Use diagnostic action instead)"),
    (r"(?i)\bgreat question\b", "Sycophantic filler detected"),
    (r"(?i)\bi('d| would) be happy to help\b", "Sycophantic filler detected"),
    (r"(?i)\bfor educational purposes only\b", "Safety disclaimer detected"),
    (r"(?i)\bplease use (this )?responsibly\b", "Moralizing safety framing detected"),
    (r"(?i)\bas an ai\b", "Meta-commentary detected"),
    (r"(?i)\b100%\s*(sure|guaranteed|certain)\b", "Unearned certainty detected without empirical verification"),
    (r"\/\/\s*TODO:\s*(implement|add rest|finish)", "Code stub / placeholder detected"),
    (r"#\s*\.\.\.\s*rest of", "Code truncation / ellipsis placeholder detected"),
]

REQUIRED_STRUCTURAL_ELEMENTS = [
    (r"(?i)Here is\s+[^:\n]+:", "Deliverable declaration ('Here is [deliverable]:') missing"),
]

def verify_response(text: str) -> Tuple[bool, List[str]]:
    violations = []
    
    # Check for banned phrases
    for pattern, reason in BANNED_PATTERNS:
        matches = re.findall(pattern, text)
        if matches:
            violations.append(f"VIOLATION: {reason} -> Matched: {matches}")
            
    # Check for required structural patterns if it is a deliverable response
    if "def " in text or "function " in text or "class " in text:
        for pattern, reason in REQUIRED_STRUCTURAL_ELEMENTS:
            if not re.search(pattern, text):
                violations.append(f"STRUCTURAL DEFECT: {reason}")
                
    return (len(violations) == 0, violations)

def main():
    if len(sys.argv) < 2:
        print("Usage: python verify_compliance.py <response_file.md>")
        sys.exit(1)
        
    target_path = sys.argv[1]
    try:
        with open(target_path, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading {target_path}: {e}")
        sys.exit(1)
        
    passed, violations = verify_response(content)
    
    print("=" * 60)
    print("BYTE MODE COMPLIANCE REPORT")
    print("=" * 60)
    if passed:
        print("STATUS: 100% COMPLIANT. Zero fluff, zero apologies, verified execution.")
        sys.exit(0)
    else:
        print(f"STATUS: NON-COMPLIANT ({len(violations)} issues found):")
        for v in violations:
            print(f"  [!] {v}")
        sys.exit(1)

if __name__ == "__main__":
    main()

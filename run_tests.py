import subprocess
import re

TEST_FILES = [
    "tests/test_tcp.py",
    "tests/test_udp.py"
]

def parse_test_output(output):
    lines = output.splitlines()
    results = []
    for line in lines:
        match = re.match(r"\[(TCP|UDP)\]\s+(.+?)\s+(PASSED|FAILED)", line)
        if match:
            protocol, test_name, status = match.groups()
            results.append((protocol, test_name.strip(), status))
    return results

def run_test_file(file_path):
    print(f"\n=== Running tests in {file_path} ===")
    result = subprocess.run(
        ["python3", file_path],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True
    )

    test_results = parse_test_output(result.stdout)
    passed = sum(1 for _, _, status in test_results if status == "PASSED")
    total = len(test_results)

    for protocol, name, status in test_results:
        print(f"[{protocol}] {name:<25} {status}")

    print(f"\nResult: {passed}/{total} tests passed in {file_path}")
    return passed, total

def main():
    total_tests = 0
    total_passed = 0

    for test_file in TEST_FILES:
        passed, total = run_test_file(test_file)
        total_tests += total
        total_passed += passed

    print("\n=== Overall Summary ===")
    print(f"Total tests passed: {total_passed}/{total_tests}")
    if total_passed == total_tests:
        print("All tests passed!")
    else:
        print("Some tests failed!")

if __name__ == "__main__":
    main()

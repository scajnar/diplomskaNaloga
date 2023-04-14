
import sys

import pytest
from tcms_api.plugin_helpers import Backend

import os
import subprocess
from junitparser import JUnitXml
def setup_backend():
    backend = Backend()
    backend.configure()
    return backend

def run_pytest_and_get_results():
    # Run pytest with JUnit and generate .xml output
    pytest_command = "pytest --junitxml=output.xml"
    result = subprocess.run(pytest_command, shell=True, check=False)

    if result.returncode not in (0, 1):
        print(f"Error: pytest returned non-zero exit status {result.returncode}")
        sys.exit(1)
    # Parse .xml output using JUnit and create a list of test results
    junit_xml = JUnitXml.fromfile("output.xml")
    test_results = []

    for suite in junit_xml:
        for case in suite:
            for result in case.result:
                if result._tag == "error":
                    status = "ERROR"
                elif result._tag == "failure":
                    status = "FAILED"
                elif result._tag == "skipped":
                    status = "BLOCKED"
                break
            else:
                status = "PASSED"
            test_function_name = case.name.split("::")[-1]  # Extract only the test function name
            result = {
                "summary": test_function_name,
                "status": status,
                "comment": str(case.result) if case.result else "",
            }
            test_results.append(result)

    # Remove the .xml output file after parsing
    os.remove("output.xml")

    return test_results

test_case_mapping = {
    "test_01": 1,
    "test_02": 2,
    "test_03": 3,
    "test_04": 4,
    # Add more mappings as needed, numbers correspond to test case IDs in KiwiTCMS https://164.90.161.164/cases/search/
}

def run_pytest_and_tcms():
    # ... (existing code) ...
    os.environ["SSL_CERT_FILE"] = "/home/samo/diplomskaNaloga/kiwi/ca.crt"
    # os.environ["JOB_NAME"] = "TEST TESTPLAN"
    # os.environ["TCMS_PRODUCT_VERSION"] = "1"
    # os.environ["BUILD_NUMBER"] = "1"
    # os.environ["TCMS_PLAN_ID"] = "46"
    os.environ["TCMS_PLAN_ID"] = "52"
    os.environ["TCMS_PRODUCT"] = "Pitonski produkt"
    os.environ["TCMS_PRODUCT_VERSION"] = "1"
    os.environ["TCMS_BUILD"] = "bf75d0a"
    os.environ["TCMS_USERNAME"] = "samo"
    os.environ["TCMS_PASSWORD"] = "samo"

    backend = setup_backend()
    test_results = run_pytest_and_get_results()

    for test_result in test_results:
        test_function_name = test_result["summary"]
        if test_function_name not in test_case_mapping:
            print(f"Error: Test function {test_function_name} not found in the mapping")
            continue

        test_case_id = test_case_mapping[test_function_name]
        backend.add_test_case_to_plan(test_case_id, backend.plan_id)
        test_executions = backend.add_test_case_to_run(test_case_id, backend.run_id)

        status_id = backend.get_status_id(test_result["status"])
        for execution in test_executions:
            backend.update_test_execution(execution["id"], status_id, test_result["comment"])

    backend.finish_test_run()

run_pytest_and_tcms()




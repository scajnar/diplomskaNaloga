import os
import ssl
from xmlrpc.client import SafeTransport

from tcms_api import TCMS
from tcms_api.plugin_helpers import Backend

class UnverifiedSSLTransport(SafeTransport):
    def make_connection(self, host):
        s = super().make_connection(host)
        s._ssl_context = ssl._create_unverified_context()
        return s

class KiwiTAPUploader:
    def __init__(self, backend):
        self.backend = backend

    def _parse(self, tap_file):
        with open(tap_file, "r") as file:
            return file.read()

    def parse_test_results(self, tap_results, plan_id, test_run_id):
        for line in tap_results.split("\n"):
            if line.startswith("ok"):
                case = self.backend.add_test_case_to_plan(line[3:].strip(), plan_id)
                self.backend.add_case_to_run(case, test_run_id)
            elif line.startswith("not ok"):
                case = self.backend.add_test_case_to_plan(line[6:].strip(), plan_id, is_confirmed=False)
                self.backend.add_case_to_run(case, test_run_id)

    def get_or_create(self, model, **kwargs):
        return self.backend.get_or_create(model, **kwargs)

def main():
    tap_file = "test_results.tap"

    product_name = "Spletna stran UL FE"
    version_name = "1.0.0"
    build_name = "unspecified"
    plan_name = "Diplomska Naloga UL FE"
    test_run_name = "test 4"

    # kiwi = TCMS()
    kiwi = TCMS(transport=UnverifiedSSLTransport())
    uploader = KiwiTAPUploader(kiwi)

    product_id = uploader.get_or_create("Product", name=product_name)
    version_id = uploader.get_or_create("Version", value=version_name, product=product_id)
    build_id = uploader.get_or_create("Build", name=build_name, product=product_id)
    plan_id = uploader.get_or_create("TestPlan", name=plan_name, product=product_id, product_version=version_id)
    test_run_id = uploader.get_or_create("TestRun", summary=test_run_name, plan=plan_id, build=build_id, product_version=version_id)

    tap_results = uploader._parse(tap_file)
    uploader.parse_test_results(tap_results, plan_id, test_run_id)

if __name__ == "__main__":
    main()

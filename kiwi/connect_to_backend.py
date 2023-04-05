import ssl
import xmlrpc.client
from tcms_api import TCMS



rpc_client = TCMS()

for test_case in rpc_client.exec.TestCase.filter({'pk': 46490}):
    print(test_case)

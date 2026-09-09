import sys
import json
from client import Groth16Verifier

def handle_request(req):
    method = req.get("method")
    params = req.get("params", {})
    if method == "verify":
        gv = Groth16Verifier()
        return {"valid": gv.verify_proof(params.get("vk", {}), params.get("inputs", []), params.get("proof", {}))}
    return {"error": "Unknown method"}

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        req = json.loads(line)
        res = handle_request(req)
        print(json.dumps(res))
        sys.stdout.flush()

if __name__ == '__main__':
    main()

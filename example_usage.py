from client import Groth16Verifier

def main():
    print("=== Testing Groth16 Verifier ===")
    verifier = Groth16Verifier()
    vk = {'alpha': 5, 'beta': 4, 'gamma': 2, 'delta': 3, 'IC': [1, 2]}
    # x = [3], ic_sum = 1 + 3*2 = 7
    # rhs = 5*4 + 7*2 + 2*3 = 20 + 14 + 6 = 40
    # lhs = A * B = 8 * 5 = 40
    proof = {'A': 8, 'B': 5, 'C': 2}

    res = verifier.verify_proof(vk, [3], proof)
    print("Verification result:", res)
    assert res is True

    print("Groth16 Verifier verified successfully!")

if __name__ == '__main__':
    main()

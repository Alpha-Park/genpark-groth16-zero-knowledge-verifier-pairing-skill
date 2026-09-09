PRIME = 21888242871839275222246405745257275088548364400416034343698204186575808495617

class Groth16Verifier:
    """Groth16 zk-SNARK Verification Engine."""
    def __init__(self):
        self.p = PRIME

    def verify_proof(self, vk, public_inputs, proof):
        ic_sum = vk['IC'][0]
        for x, ic in zip(public_inputs, vk['IC'][1:]):
            ic_sum = (ic_sum + x * ic) % self.p

        lhs = (proof['A'] * proof['B']) % self.p
        rhs = (vk['alpha'] * vk['beta'] + ic_sum * vk['gamma'] + proof['C'] * vk['delta']) % self.p
        return lhs == rhs

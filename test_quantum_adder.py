import random
import sys
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

from quantum_adder import build_adder_circuit

def run_adder(n, x, y):
    #Simulate the adder and return (x_out, y_out, carry_out).
    m = n + 1
    adder_qc, x_reg, y_reg, carry_reg = build_adder_circuit(n)

    prep = QuantumCircuit(x_reg, y_reg, carry_reg)
    for k in range(m):
        if (x >> k) & 1:
            prep.x(x_reg[k])
    for k in range(m):
        if (y >> k) & 1:
            prep.x(y_reg[k])

    full = prep.compose(adder_qc)

    sv = Statevector(full)
    probs = sv.probabilities_dict(decimals=10)

    result = max(probs, key=probs.get)
    assert probs[result] > 0.999, f"Not a pure state! max_prob={probs[result]:.6f}"

    # Bitstring (big-endian): c[n]..c[0] | y[n]..y[0] | x[n]..x[0]
    # Lengths:                    m            m            m     (m = n+1)
    carry_out = int(result[:m], 2)
    y_out     = int(result[m : 2 * m], 2)
    x_out     = int(result[2 * m:], 2)
    return x_out, y_out, carry_out

def check(n, x, y):
    x_out, y_out, carry_out = run_adder(n, x, y)
    ok = (x_out == x) and (y_out == x + y) and (carry_out == 0)
    if not ok:
        print(f"  FAIL n={n} x={x} y={y}: got x={x_out} y={y_out} carry={carry_out} "
              f"(expected y={x+y})")
    return ok


# test groups
def test_exhaustive(n):
    total = (2 ** (n+1))
    print(f"  Exhaustive n={n} ({total} pairs) ... ", end="", flush=True)
    passed = all(check(n, x, y) for x in range(2**n) for y in range(2**n))
    print("PASS" if passed else "FAIL")
    return passed


def test_boundary(n):
    hi = 2**n - 1
    cases = [(0, 0), (0, hi), (hi, 0), (2**(n-1), 2**(n-1)), (hi, hi)]
    print(f"  Boundary  n={n} ({len(cases)} cases) ... ", end="", flush=True)
    passed = all(check(n, x, y) for x, y in cases)
    print("PASS" if passed else "FAIL")
    return passed


def test_random(n, k=30):
    rng = random.Random(42)
    hi = 2**n - 1
    pairs = [(rng.randint(0, hi), rng.randint(0, hi)) for _ in range(k)]
    print(f"  Random    n={n} ({k} pairs) ... ", end="", flush=True)
    passed = all(check(n, x, y) for x, y in pairs)
    print("PASS" if passed else "FAIL")
    return passed

if __name__ == "__main__":
    ok = True

    print("=== Exhaustive (n=1..4) ===")
    for n in [1, 2, 3, 4]:
        ok &= test_exhaustive(n)

    print("\n=== Boundary cases ===")
    for n in [1, 3, 5, 6]:
        ok &= test_boundary(n)

    print("\n=== Random (larger n) ===")
    for n in [5, 6, 7]:
        ok &= test_random(n)

    print("\n" + ("ALL TESTS PASSED" if ok else "SOME TESTS FAILED"))
    sys.exit(0 if ok else 1)

# Quantum Full Adder

## What it does

Implements the unitary:

```
U |x⟩ |y⟩ |0⟩ = |x⟩ |x+y⟩ |0⟩
```

for n-bit unsigned integers x, y with 0 ≤ x, y < 2ⁿ (so x+y < 2ⁿ⁺¹ — no overflow).

## Running

```bash
source .venv/bin/activate
pip3 install -r requirements.txt
python test_quantum_adder.py
```

---

## Test Results

```
=== Exhaustive (n=1..4) ===
  Exhaustive n=1 (4 pairs)   ... PASS  (0.01s total, 0.002s/pair)
  Exhaustive n=2 (16 pairs)  ... PASS  (0.01s total, 0.000s/pair)
  Exhaustive n=3 (64 pairs)  ... PASS  (0.07s total, 0.001s/pair)
  Exhaustive n=4 (256 pairs) ... PASS  (1.06s total, 0.004s/pair)

=== Boundary cases ===
  Boundary  n=1 (5 cases) ... PASS  (0.00s total, 0.000s/pair)
  Boundary  n=3 (5 cases) ... PASS  (0.01s total, 0.001s/pair)
  Boundary  n=5 (5 cases) ... PASS  (0.29s total, 0.058s/pair)
  Boundary  n=6 (5 cases) ... PASS  (2.52s total, 0.505s/pair)

=== Random (larger n) ===
  Random    n=5 (30 pairs) ... PASS  (1.64s total,   0.055s/pair)
  Random    n=6 (30 pairs) ... PASS  (15.11s total,  0.504s/pair)
  Random    n=7 (30 pairs) ... PASS  (201.23s total, 6.708s/pair)

ALL TESTS PASSED
```
---

## Reference

Vedral, V., Barenco, A., Ekert, A. (1996). *Quantum Networks for Elementary Arithmetic Operations.* Phys. Rev. A 54, 147.
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
python test_quantum_adder.py
```

---

## Test Results

```
=== Exhaustive (n=1..4) ===
  Exhaustive n=1 (4 pairs)   ... PASS
  Exhaustive n=2 (16 pairs)  ... PASS
  Exhaustive n=3 (64 pairs)  ... PASS
  Exhaustive n=4 (256 pairs) ... PASS

=== Boundary cases ===
  Boundary  n=1 (5 cases) ... PASS
  Boundary  n=3 (5 cases) ... PASS
  Boundary  n=5 (5 cases) ... PASS
  Boundary  n=6 (5 cases) ... PASS

=== Random (larger n) ===
  Random    n=5 (30 pairs) ... PASS
  Random    n=6 (30 pairs) ... PASS
  Random    n=7 (30 pairs) ... PASS

ALL TESTS PASSED
```
---

## Reference

Vedral, V., Barenco, A., Ekert, A. (1996). *Quantum Networks for Elementary Arithmetic Operations.* Phys. Rev. A 54, 147.
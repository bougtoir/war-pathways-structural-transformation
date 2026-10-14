import numpy as np
from dataclasses import replace
from model6 import (P6, pi, dpi_dr_fixed_L, dpi_dr_total, L_inf,
                    pi_inf, level_condition)


def test_pi_zero_at_r0():
    p = P6()
    for L in [0.0, 0.5, 1.0]:
        assert pi(0.0, L, p) == 0.0  # never strictly negative


def test_level_condition_equivalence():
    p = P6()
    lhs, rhs, neg = level_condition(1.0, p)
    assert neg == (lhs < rhs)
    assert np.isclose(pi_inf(1.0, p), 1.0 * lhs - p.c1 - p.c2)


def test_derivative_does_not_imply_level():
    p = replace(P6(), w_phys=0.05, w_hum=0.5, w_inst=0.3, w_net=0.15,
                c1=0.01, c2=0.01, coll_action=3.0, exit_cost=0.5)
    assert dpi_dr_total(1.0, p) < 0.05      # derivative small/negative-ish
    assert pi_inf(1.0, p) > 0                # yet level stays positive


def test_L_bounds():
    p = P6()
    for r in [0, 0.5, 1, 5]:
        assert 0 <= L_inf(r, p, "opt") <= 1
        assert 0 <= L_inf(r, p, "rule") <= 1


def test_sign_of_dL_dr_is_emergent():
    p_fear = replace(P6(), fear_gain=3.0, coll_action=0.5, exit_cost=0.2)
    # fear outweighs withdrawal cost -> compliance does not fall
    assert np.isclose(L_inf(0.5, p_fear, "opt"), L_inf(0.0, p_fear, "opt"))

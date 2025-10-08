# Copyright Quantinuum
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import pytest
from pytket.circuit import (
    Circuit,
)
from utilities import (  # type: ignore
    run_qir_gen_and_check,
)

from pytket.qir.conversion.api import QIRProfile, pytket_to_qir


@pytest.mark.parametrize(
    "profile",
    [
        QIRProfile.ADAPTIVE,
        QIRProfile.AZUREADAPTIVE,
        QIRProfile.PYTKET,
        QIRProfile.ADAPTIVE_CREGSIZE,
    ],
)
def test_pytket_qir_rng(profile: QIRProfile) -> None:
    circ = Circuit()
    creg = circ.add_c_register("c", 64)
    circ.add_c_setbits([True, True], [creg[3], creg[11]])
    circ.set_rng_seed(creg)

    run_qir_gen_and_check(circ, "test_pytket_qir_rng", profile=profile)


@pytest.mark.parametrize(
    "profile",
    [
        QIRProfile.ADAPTIVE,
        QIRProfile.AZUREADAPTIVE,
        QIRProfile.PYTKET,
        QIRProfile.ADAPTIVE_CREGSIZE,
    ],
)
def test_pytket_qir_rng_2(profile: QIRProfile) -> None:
    circ = Circuit()
    creg = circ.add_c_register("c", 32)
    circ.add_c_setbits([True, True], [creg[3], creg[11]])
    circ.set_rng_bound(creg)
    run_qir_gen_and_check(circ, "test_pytket_qir_rng_2", profile=profile)


@pytest.mark.parametrize(
    "profile",
    [
        QIRProfile.ADAPTIVE,
        QIRProfile.AZUREADAPTIVE,
        QIRProfile.PYTKET,
        QIRProfile.ADAPTIVE_CREGSIZE,
    ],
)
def test_pytket_qir_rng_3(profile: QIRProfile) -> None:
    circ = Circuit()
    creg = circ.add_c_register("c", 32)
    circ.get_rng_num(creg)
    run_qir_gen_and_check(circ, "test_pytket_qir_rng_3", profile=profile)


@pytest.mark.parametrize(
    "profile",
    [
        QIRProfile.ADAPTIVE,
        QIRProfile.AZUREADAPTIVE,
        QIRProfile.PYTKET,
        QIRProfile.ADAPTIVE_CREGSIZE,
    ],
)
def test_pytket_qir_rng_4(profile: QIRProfile) -> None:
    circ = Circuit()
    numcreg = circ.add_c_register("c", 32)
    bound_creg = circ.add_c_register("b", 32)
    circ.add_c_setbits([True, True], [bound_creg[3], bound_creg[11]])
    circ.set_rng_bound(bound_creg)
    circ.get_rng_num(numcreg)
    run_qir_gen_and_check(circ, "test_pytket_qir_rng_4", profile=profile)


@pytest.mark.parametrize(
    "profile",
    [
        QIRProfile.ADAPTIVE,
        QIRProfile.AZUREADAPTIVE,
        QIRProfile.PYTKET,
        QIRProfile.ADAPTIVE_CREGSIZE,
    ],
)
def test_pytket_qir_rng_5(profile: QIRProfile) -> None:
    circ = Circuit()
    numcreg = circ.add_c_register("c", 32)
    index_creg = circ.add_c_register("i", 32)
    circ.add_c_setbits([True, True], [index_creg[3], index_creg[11]])
    circ.set_rng_index(index_creg)
    circ.get_rng_num(numcreg)
    run_qir_gen_and_check(circ, "test_pytket_qir_rng_5", profile=profile)


@pytest.mark.parametrize(
    "profile",
    [
        QIRProfile.ADAPTIVE,
        QIRProfile.AZUREADAPTIVE,
        QIRProfile.PYTKET,
        QIRProfile.ADAPTIVE_CREGSIZE,
    ],
)
def test_pytket_qir_rng_6(profile: QIRProfile) -> None:
    circ = Circuit()
    jobcreg = circ.add_c_register("j", 32)
    circ.get_job_shot_num(jobcreg)
    run_qir_gen_and_check(circ, "test_pytket_qir_rng_6", profile=profile)


@pytest.mark.parametrize(
    "profile",
    [
        QIRProfile.BASE,
        QIRProfile.AZUREBASE,
    ],
)
def test_pytket_qir_rng_7(profile: QIRProfile) -> None:
    # check that get_job_shot_num can't be converted for the base profile
    circ = Circuit()
    jobcreg = circ.add_c_register("j", 32)
    circ.get_job_shot_num(jobcreg)
    with pytest.raises(ValueError):
        pytket_to_qir(circ, profile=profile)


if __name__ == "__main__":
    test_pytket_qir_rng(QIRProfile.PYTKET)

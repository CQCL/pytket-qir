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


from pytket.circuit import Circuit
from pytket.qir.conversion.api import QIRFormat, QIRProfile, pytket_to_qir


def check_qir_result(given_qir: str, filename: str, writefile: bool = False) -> None:
    """this function can be used to compare the generated qir to the qir in a file
    can be used to write the file as well, if the file is written
    this function will have a wrong assert to fail the testcase

    :param given_qir: given qir string that should be compared with the file
    :type given_qir: str
    :param filename: name of the file that should be compared with or written to
    :type filename: str
    :param writefile: if set a file named `filename` will be created containing
      the `given_qir`
    :type writefile: bool
    """

    if writefile:
        with open(f"qir/{filename}.ll", "w") as f:
            f.write(given_qir)
        assert not "testcase is writing file"

    with open(f"qir/{filename}.ll") as f:
        data = f.read()

    assert data == given_qir


def run_qir_gen_and_check(
    circ: Circuit,
    filename: str,
    writefile: bool = False,
    profile: QIRProfile = QIRProfile.ADAPTIVE,
) -> None:
    """this function can be used to compare the generated qir from a circuit to the qir
    in a file can be used to write the file as well, if the file is written
    this function will have a wrong assert to fail the testcase

    :param circ: Circuit that should be converted to QIR and checked with stored results
    :type circ: Circuit
    :param filename: name of the file that should be compared with or written to
    :type filename: str
    :param writefile: if set a file named `filename` will be created containing
      the `given_qir`
    :type writefile: bool
    :param profile: if the qir should be profile compatible
    :type profile: bool
    """

    gen_qir_ll = pytket_to_qir(
        circ,
        name=filename,
        qir_format=QIRFormat.STRING,
        profile=profile,
        cut_pytket_register=True,
    )

    if writefile:
        with open(f"qir/{filename}-{profile}.ll", "w") as f:
            f.write(gen_qir_ll)  # type: ignore
        assert not "testcase is writing file"

    with open(f"qir/{filename}-{profile}.ll") as f:
        data = f.read()

    assert data == gen_qir_ll

    """
    # this can be used for benchmarking and generating files for all circuits
    ll = pytket_to_qir(circ, filename, QIRFormat.STRING, profile=True)

    with open(f"qir-bc/{filename}-{profile}.ll", "w") as f:
        f.write(ll)

    bc = pytket_to_qir(circ, filename, QIRFormat.BINARY)

    with open(f"qir-bc/{filename}-{profile}.bc", "wb") as f:
        f.write(bc)"""

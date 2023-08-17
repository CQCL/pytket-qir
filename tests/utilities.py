# Copyright 2020-2023 Cambridge Quantum Computing
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

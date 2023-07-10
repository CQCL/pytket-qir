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

    with open(f"qir/{filename}.ll", "r") as f:
        data = f.read()

    data_lines = data.split("\n")
    given_qir_lines = given_qir.split("\n")

    for i in range(max(len(data_lines), len(given_qir_lines))):
        if data_lines[i] != given_qir_lines[i]:
            print(f"PROBLEM: {i}")
            print(data_lines[i])
            print(given_qir_lines[i])

        assert data_lines[i] == given_qir_lines[i]

    assert data == given_qir


def check_qir_result_2(given_qir: str, given_qir_2: str) -> None:
    """TODO
    this function can be used to compare the generated qir to the qir in a file
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

    given_qir_lines = given_qir.split("\n")
    given_qir_lines_2 = given_qir_2.split("\n")

    stoppoint = 0

    for i in range(max(len(given_qir_lines), len(given_qir_lines_2))):
        if given_qir_lines[i] != given_qir_lines_2[i]:
            print(f"PROBLEM: {i}")
            print(given_qir_lines[i])
            print(given_qir_lines_2[i])
            stoppoint = i
            break

        # assert given_qir_lines[i] == given_qir_lines_2[i]

    print("\n\n\n")

    for i in range(stoppoint, len(given_qir_lines)):
        print(given_qir_lines[i])

    print("\n\n\n\n\n")

    for i in range(stoppoint, len(given_qir_lines_2)):
        print(given_qir_lines_2[i])

    assert given_qir == given_qir_2

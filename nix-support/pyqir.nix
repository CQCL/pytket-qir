# adapted from
# https://github.com/NixOS/nixpkgs/pull/237604/files
self: super:
#{ lib
#, buildPythonPackage
#, pythonOlder
#, fetchFromGitHub
#, rustPlatform
#, libxml2
#, llvm # LLVM version provided must strictly match pyqir support list
#}:
let
  lib = super.lib;
  llvm = super.llvm_14;
  llvm-v-major = lib.versions.major llvm.version;
  llvm-v-minor = builtins.substring 0 1 (lib.versions.minor llvm.version);
  pyqir-version = "0.9.0";
  pyqir-hash = sha256:oqkv6gOIazwkH81GomCXdmHXlG008KdK3b9+hUGCtmE=;
  pyqir-cargo-hash = sha256:bTQm8cpvoTfa8+N38UB01AZl1LZMXsMXYbDa6f0Lj9U=;
in
{
  pyqir = super.python3Packages.buildPythonPackage rec {
    pname = "pyqir";
    version = pyqir-version;
    format = "pyproject";
    src = super.fetchFromGitHub {
      owner = "qir-alliance";
      repo = "pyqir";
      rev = "v${pyqir-version}";
      sha256 = pyqir-hash;
    };

    cargoDeps = super.rustPlatform.fetchCargoTarball {
      inherit src;
      name = "pyqir-${pyqir-version}";
      hash = pyqir-cargo-hash;
    };

    buildAndTestSubdir = "pyqir";

    nativeBuildInputs = with super.rustPlatform; [ cargoSetupHook maturinBuildHook ];

    buildInputs = [ llvm super.libxml2.dev ];

    maturinBuildFlags = "-F llvm${llvm-v-major}-${llvm-v-minor}";

    preConfigure = ''
      export LLVM_SYS_${llvm-v-major}${llvm-v-minor}_PREFIX=${llvm.dev}
    '';

    pythonImportsCheck = [ "pyqir" ];

    passthru.llvm = llvm;

    meta = with lib; {
      description = "API for parsing and generating Quantum Intermediate Representation (QIR)";
      homepage = "https://github.com/qir-alliance/pyqir";
      license = licenses.mit;
      maintainers = with maintainers; [ evilmav ];
    };
  };
}

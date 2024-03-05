self: super:
let
  lib = super.lib;
  llvm = super.llvm_14;
  llvm-v-major = lib.versions.major llvm.version;
  llvm-v-minor = builtins.substring 0 1 (lib.versions.minor llvm.version);
  pyqir-version = "0.10.0";
  pyqir-hash = sha256:dZd+U3vyHb9rrNB90XiLn6fAbsg3Xk9Htnw5Ce/vra4=;
  pyqir-cargo-hash = sha256:U964/0ekTVgl5CCU4xgExgFhSIP1RKocNbjScWw4BTM=;
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
  };
}

self: super:
let
  metadata = builtins.readFile ../_metadata.py;
  versions =
    builtins.match ''.*_version__ *= *["']([^"']+)["'].*'' metadata;
  version = if builtins.length versions > 0 then
    builtins.elemAt versions 0
  else
    builtins.trace "Warning: unable to find version. Defaulting to 0.0.0" "0.0.0";
in {
  pytket-qir = super.python3.pkgs.buildPythonPackage {
    pname = "pytket-qir";
    version = version;
    src = super.stdenv.mkDerivation{
      name = "pytket-qir-sources";
      phases = [ "installPhase" ];
      installPhase = ''
        mkdir -p $out;
        cp -r ${../pytket} $out/pytket;
        cp -r ${../setup.py} $out/setup.py;
        cp -r ${../README.md} $out/README.md; # required for setup's long description
        cp -r ${../pytest.ini} $out/pytest.ini;
        cp -r ${../mypy.ini} $out/mypy.ini;
        cp -r ${../_metadata.py} $out/_metadata.py;
        cp -r ${../tests} $out/tests;
      '';
    };
    propagatedBuildInputs = [ super.pytket self.pyqir ];
    checkInputs = with super.python3Packages; [ pytest mypy ];
    checkPhase = ''
      export HOME=$TMPDIR;

      # mypy fails with scipy errors
      python -m mypy --config-file=mypy.ini --no-incremental -p pytket -p tests

      cd tests;
      python -m pytest -s .
    '';
  };
}

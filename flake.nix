{
  description = "Pytket QIR Extension";
  nixConfig.extra-substituters = "https://tket.cachix.org https://cache.nixos.org";
  nixConfig.trusted-public-keys = ''
    tket.cachix.org-1:ACdm5Zg19qPL0PpvUwTPPiIx8SEUy+D/uqa9vKJFwh0=
    cache.nixos.org-1:6NCHdD59X431o0gWypbMrAURkbJ16ZPMQFGspcDShjY=
  '';
  inputs.flake-utils.url = "github:numtide/flake-utils";
  inputs.tket.url = "github:CQCL/tket";
  inputs.nixpkgs = {
   # url = "github:nixos/nixpkgs";
    follows = "tket/nixpkgs";
  };
  outputs = { self, nixpkgs, flake-utils, tket }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = import nixpkgs {
          inherit system;
          overlays = [
            (self: super: {
              inherit (tket.packages."${system}") tket pytket;
            })
            (import ./nix-support/pyqir.nix)
            (import ./nix-support/pytket-qir.nix)
          ];
        };
      in {
        packages = {
          pytket-qir = pkgs.pytket-qir;
        };
        devShells = {
          default = pkgs.mkShell { buildInputs = [ pkgs.pytket-qir ]; };
        };
        checks = {
          pytket-qir-tests = pkgs.pytket-qir;
        };
      });
}

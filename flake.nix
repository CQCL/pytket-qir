{
  description = "Pytket QIR Extension";
  inputs.nixpkgs.url = "github:nixos/nixpkgs";
  inputs.flake-utils.url = "github:numtide/flake-utils";
  inputs.tket.url = "github:CQCL/tket";
  inputs.tket.inputs.nixpkgs.follows = "nixpkgs";
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

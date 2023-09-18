{ pkgs ? import <nixpkgs> {} }:
  pkgs.mkShell {
    # nativeBuildInputs is usually what you want -- tools you need to run
    nativeBuildInputs = with pkgs.buildPackages; [
      python310
      python310Packages.pip
      python310Packages.tensorflow
      python310Packages.flask
      python310Packages.opencv4
      python310Packages.flask-login
      python310Packages.flask-sqlalchemy
      python310Packages.numpy
    ];
}
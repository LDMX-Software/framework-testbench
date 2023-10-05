# framework-testbench specific bash aliases for within the denv

configure() {
  cmake -B build -S . $@
}

build() {
  cmake --build build $@
}

run() {
  ./build/Framework/fire $@
}

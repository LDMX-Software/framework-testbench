# Framework Testbench
This repository is for testing changes to [Framework](https://github.com/LDMX-Software/Framework) without having to carry around the weight of all of ldmx-sw.
It's goals are

1. Give an opportunity to isolate Framework-specific bugs
2. Provide an area to benchmark the performance of Framework in a controlled way
3. Have a space for trying out new features or refactors that may be difficult or time consuming to apply to all of ldmx-sw

As these goals imply, this repository is highly focused on the LDMX developer who wants to understand Framework in detail. With that in mind, there is a lot less comments and documentation in the code scattered throughout this repository since it is geared towards simply supporting Framework developments.

## Set Up
This repository is a stand-alone and lightweight mimic of ldmx-sw.
It is using a slightly newer workflow based on [denv](https://github.com/tomeichlersmith/denv) to run the containerized development environment.

1. [Install denv](https://tomeichlersmith.github.io/denv/getting_started.html#installation)
2. Clone this repository recursively `git clone --recursive git@github.com:LDMX-Software/framework-testbench.git`
3. Enter the denv `cd framework-testbench; denv`
4. Configure/Build/Install/Run `fire` with the `Bench` module
```
# within the denv, the prompt will be updated with 'framework-testbench'
cmake -B build -S .
cd build
make install
cd ..
fire
```
I often have a two-side approach to development where one side of a tmux session is in the denv
and the other is outside the denv to handle `git` and file writing tasks. I could also imagine a workflow where
the denv is launched from a shell within a VS Code (or similar) editor.

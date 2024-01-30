
#include "Framework/EventProcessor.h"

namespace bench {

class MoveRootDir : public framework::Analyzer {
 public:
  MoveRootDir(const std::string& name, framework::Process& p)
    : framework::Analyzer(name,p) {}
  ~MoveRootDir() = default;
  void analyze(const framework::Event& event) final override {
    getHistoDirectory();
  }
};

}

DECLARE_ANALYZER_NS(bench,MoveRootDir);

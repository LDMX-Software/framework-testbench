
#include "Framework/EventProcessor.h"

namespace bench {

class NeverSucceed : public framework::Producer {
 public:
  NeverSucceed(const std::string& name, framework::Process& p)
    : framework::Producer(name,p) {}
  ~NeverSucceed() = default;
  void produce(framework::Event& event) final override {
    abortEvent();
  }
};  // NeverSucceed

}

DECLARE_PRODUCER_NS(bench,NeverSucceed);

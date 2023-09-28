#include "Framework/EventProcessor.h"

#define THROW_IF_MATCH() \
  if (when_ == __FUNCTION__) { \
    EXCEPTION_RAISE("TEST",__FUNCTION__ ); \
  }

namespace bench {

class Exceptions : public framework::Producer {
  std::string when_;
 public:
  Exceptions(const std::string& name, framework::Process& p)
    : framework::Producer(name,p) {}
  ~Exceptions() = default;
  void configure(framework::config::Parameters& ps) final override {
    when_ = ps.getParameter<std::string>("when");
    THROW_IF_MATCH()
  }
  void onProcessStart() final override {
    THROW_IF_MATCH()
  }
  void beforeNewRun(ldmx::RunHeader& rh) final override {
    THROW_IF_MATCH()
  }
  void onNewRun(const ldmx::RunHeader& rh) final override {
    THROW_IF_MATCH()
  }
  void produce(framework::Event& event) final override {
    THROW_IF_MATCH()
  }
  void onProcessEnd() final override {
    THROW_IF_MATCH()
  }
};  // Produce

}

DECLARE_PRODUCER_NS(bench,Exceptions);

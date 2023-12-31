
#include "Bench/Event/Hit.h"

#include "Framework/EventProcessor.h"

#include <random>

namespace bench {

class Recon : public framework::Producer {
  /// the random number generator, unseeded so it produces the same results each time
  std::mt19937 rng;
  /// the distribution of sizes
  std::uniform_int_distribution<std::size_t> rand_index;
 public:
  Recon(const std::string& name, framework::Process& p)
    : framework::Producer(name,p),
    rng{}, // this is where a seed for the RNG would be put
    rand_index{0, 99}
  {}
  ~Recon() = default;
  void produce(framework::Event& event) final override {
    const auto& rand_data = event.getCollection<Hit>("randdata");
    std::size_t i;
    do {
      i = rand_index(rng);
    } while(i >= rand_data.size());
    
    Hit special = rand_data.at(i);
    event.add("specialhit", special);
  }
};

}

DECLARE_PRODUCER_NS(bench,Recon);

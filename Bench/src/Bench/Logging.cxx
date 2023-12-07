
#include "Framework/Logger.h"

namespace bench {

/**
 * check that the logging macros can compile
 * in a different namespace
 */
class MyClass {
  enableLogging("MyClass");
 public:
  void calculate() {
    ldmx_log(info) << "Calculating data";
  }
};

}

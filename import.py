import module_hello
import module_hello as test
from module_hello import hello

module_hello.hello("john")
test.hello("pole")
hello("carol")

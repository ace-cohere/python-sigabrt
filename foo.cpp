#include <cstdlib>
#include <iostream>

class Foo{
    public:
        void bar(){
            std::cout << "Hello" << std::endl;
            std::abort();
            std::cout << "World" << std::endl;
        }
};

extern "C" {
    Foo* Foo_new(){ return new Foo(); }
    void Foo_bar(Foo* foo){ foo->bar(); }
}

#![allow(non_snake_case)]
#![allow(unused_variables)]
#![allow(dead_code)]

fn main() {
    // snip
    struct XorShift {
        x: usize
    }
    impl XorShift {
        fn new() -> XorShift { XorShift { x: 88172645463325252 } }
        fn rand(&mut self) -> f64 {
            self.x ^= self.x << 13;
            self.x ^= self.x >> 7;
            self.x ^= self.x << 17;
            (self.x as f64) / (std::usize::MAX as f64)
        }

        fn randint(&mut self, a: usize, b: usize) -> usize {
            self.x ^= self.x << 13;
            self.x ^= self.x >> 7;
            self.x ^= self.x << 17;
            a + self.x % (b - a)
        }
    }
    // snip

    let mut rnd = XorShift::new();
    println!("{}", rnd.rand());
    println!("{}", rnd.randint(1, 6));
}

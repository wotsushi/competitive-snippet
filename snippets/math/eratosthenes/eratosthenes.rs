#![allow(non_snake_case)]
#![allow(unused_variables)]
#![allow(dead_code)]

fn main() {
    let N: usize = {
        let mut line: String = String::new();
        std::io::stdin().read_line(&mut line).unwrap();
        line.trim().parse().unwrap()
    };

    let _N = N + 2;
    // snip
    let primes = {
        let mut primes = vec![true; _N + 1];
        primes[0] = false;
        primes[1] = false;
        for i in 2.._N {
            if primes[i] {
                for k in 2..(_N / i + 1) {
                    primes[k * i] = false;
                }
            }
        }
        primes
    };
    // snip

    let ans = 2 * (5..(N + 3)).filter(|&i| primes[i] && primes[i - 2]).count();

    println!("{}", ans);
}

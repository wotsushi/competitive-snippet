#![allow(non_snake_case)]
#![allow(unused_variables)]
#![allow(dead_code)]

fn main() {
    // snip
    let _A: Vec<Vec<_i64>> = {
        let mut _A = vec![];
        for _ in 0.._N {
            let mut line: String = String::new();
            std::io::stdin().read_line(&mut line).unwrap();
            _A.push(
                line.split_whitespace()
                    .map(|x| x.parse().unwrap())
                    .collect()
            );
        }
        _A
    };
    // snip
}

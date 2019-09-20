#![allow(non_snake_case)]
#![allow(unused_variables)]
#![allow(dead_code)]

fn main() {
    // snip
    let _A: Vec<_i64> = (0.._N)
        .map(|_| {
                let mut line: String = String::new();
                std::io::stdin().read_line(&mut line).unwrap();
                line.trim().parse().unwrap()
        })
        .collect();
    // snip
}

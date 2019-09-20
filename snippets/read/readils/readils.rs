#![allow(non_snake_case)]
#![allow(unused_variables)]
#![allow(dead_code)]

fn main() {
    // snip
    let _A: Vec<_i64> = {
        let mut line: String = String::new();
        std::io::stdin().read_line(&mut line).unwrap();
        line.split_whitespace()
            .map(|x| x.parse().unwrap())
            .collect()
    };
    // snip
}

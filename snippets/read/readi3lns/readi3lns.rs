#![allow(non_snake_case)]
#![allow(unused_variables)]
#![allow(dead_code)]

fn main() {
    // snip
    let (_A, _B, _C): (Vec<_i64>, Vec<_i64>, Vec<_i64>) = {
        let (mut _A, mut _B, mut _C) = (vec![], vec![], vec![]);
        for _ in 0.._N {
            let mut line: String = String::new();
            std::io::stdin().read_line(&mut line).unwrap();
            let mut iter = line.split_whitespace();
            _A.push(iter.next().unwrap().parse().unwrap());
            _B.push(iter.next().unwrap().parse().unwrap());
            _C.push(iter.next().unwrap().parse().unwrap());
        }
        (_A, _B, _C)
    };
    // snip
}

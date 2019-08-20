#![allow(non_snake_case)]

fn main() {
    let _N: i64 = {
        let mut line: String = String::new();
        std::io::stdin().read_line(&mut line).unwrap();
        line.trim().parse::<_>().unwrap()
    };
    // snip
    let (_A, _B): (Vec<i64>, Vec<i64>) = {
        let (mut _A, mut _B) = (vec![], vec![]);
        for _ in 0.._N {
            let mut line: String = String::new();
            std::io::stdin().read_line(&mut line).unwrap();
            let mut iter = line.split_whitespace();
            _A.push(iter.next().unwrap().parse().unwrap());
            _B.push(iter.next().unwrap().parse().unwrap());
        }
        (_A, _B)
    };
    // snip
    println!("{:?}", _A);
    println!("{:?}", _B);
}

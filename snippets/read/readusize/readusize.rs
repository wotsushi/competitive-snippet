#![allow(non_snake_case)]

// https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/1/ITP1_1_B

fn main() {
    // snip
    let _N: usize = {
        let mut line: String = String::new();
        std::io::stdin().read_line(&mut line).unwrap();
        line.trim().parse().unwrap()
    };
    // snip

    let ans = _N.pow(3);

    println!("{}", ans);
}

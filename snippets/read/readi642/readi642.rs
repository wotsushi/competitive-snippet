#![allow(non_snake_case)]
#![allow(unused_variables)]

// https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/2/ITP1_2_A

fn main() {
    // snip
    let (_N, _M): (i64, i64) = {
        let mut line: String = String::new();
        std::io::stdin().read_line(&mut line).unwrap();
        let mut iter = line.split_whitespace();
        (
            iter.next().unwrap().parse().unwrap(),
            iter.next().unwrap().parse().unwrap()
        )
    };
    // snip
    let a = _N;
    let b = _M;
    let ans = if a < b {
        "a < b"
    } else if a > b {
        "a > b"
    } else {
        "a == b"
    };
    println!("{}", ans);
}

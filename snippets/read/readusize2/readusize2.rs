#![allow(non_snake_case)]
#![allow(unused_variables)]

// https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/1/ITP1_1_C

fn main() {
    // snip
    let (_N, _M): (usize, usize) = {
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
    let ans = format!(
        "{} {}",
        a * b,
        2 * (a + b)
    );
    println!("{}", ans);
}

#![allow(non_snake_case)]
#![allow(unused_variables)]
#![allow(dead_code)]

// https://onlinejudge.u-aizu.ac.jp/challenges/sources/JOI/Prelim/0652

fn main() {

    // snip
    fn iceil(a: i64, b: i64) -> i64 { (a + b - 1) / b }
    // snip

    let (A, B, C): (i64, i64, i64) = {
        let mut line: String = String::new();
        std::io::stdin().read_line(&mut line).unwrap();
        let mut iter = line.split_whitespace();
        (
            iter.next().unwrap().parse().unwrap(),
            iter.next().unwrap().parse().unwrap(),
            iter.next().unwrap().parse().unwrap()
        )
    };

    let coins_week = 7 * A + B;
    let ans = 7 * (C / coins_week) + std::cmp::min(iceil(C % coins_week, A), 7);

    println!("{}", ans);
}
#![allow(non_snake_case)]
#![allow(unused_variables)]

// https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/4/ITP1_4_D

fn main() {
    let n: i64 = {
        let mut line: String = String::new();
        std::io::stdin().read_line(&mut line).unwrap();
        line.trim().parse().unwrap()
    };
    // snip
    let _A: Vec<i64> = {
        let mut line: String = String::new();
        std::io::stdin().read_line(&mut line).unwrap();
        line.split_whitespace()
            .map(|x| x.parse().unwrap())
            .collect()
    };
    // snip
    let a = _A;

    let ans = format!(
        "{} {} {}",
        *a.iter().min().unwrap(),
        *a.iter().max().unwrap(),
        a.iter().sum::<i64>()
    );
    println!("{}", ans);
}

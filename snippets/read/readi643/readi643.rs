#![allow(non_snake_case)]
#![allow(unused_variables)]

// https://onlinejudge.u-aizu.ac.jp/courses/lesson/8/ITP2/all/ITP2_3_A

fn main() {
    // snip
    let (_A, _B, _C): (i64, i64, i64) = {
        let mut line: String = String::new();
        std::io::stdin().read_line(&mut line).unwrap();
        let mut iter = line.split_whitespace();
        (
            iter.next().unwrap().parse().unwrap(),
            iter.next().unwrap().parse().unwrap(),
            iter.next().unwrap().parse().unwrap()
        )
    };
    // snip

    let a = _A;
    let b = _B;
    let c = _C;
    let ans = format!(
        "{} {}",
        *vec![a, b, c].iter().min().unwrap(),
        *vec![a, b, c].iter().max().unwrap()
    );

    println!("{}", ans);
}

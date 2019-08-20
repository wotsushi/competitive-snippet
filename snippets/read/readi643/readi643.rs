#![allow(non_snake_case)]
#![allow(unused_variables)]

// https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/2/ITP1_2_B

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

    let ans = if a < b && b < c {
        "Yes"
    } else {
        "No"
    };

    println!("{}", ans)
}

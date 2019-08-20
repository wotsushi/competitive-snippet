#![allow(non_snake_case)]
#![allow(unused_variables)]

// https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/1/ALDS1_1_C

fn main() {
    let _N: i64 = {
        let mut line: String = String::new();
        std::io::stdin().read_line(&mut line).unwrap();
        line.trim().parse::<_>().unwrap()
    };
    // snip
    let _A: Vec<i64> = (0.._N)
        .map(|_| {
                let mut line: String = String::new();
                std::io::stdin().read_line(&mut line).unwrap();
                line.trim().parse().unwrap()
        })
        .collect();
    // snip
    let n = _N;
    let a = _A;

    let ans = a.iter()
        .filter(
            |&&x| (2..x).take_while(
                |&y| y * y <= x
            ).all(
                |y| x % y != 0
            )
        )
        .count();
    println!("{}", ans);
}

#![allow(non_snake_case)]

// https://onlinejudge.u-aizu.ac.jp/courses/lesson/8/ITP2/all/ITP2_6_C

fn main() {
    let n: i64 = {
        let mut line: String = String::new();
        std::io::stdin().read_line(&mut line).unwrap();
        line.trim().parse().unwrap()
    };
    let a: Vec<i64> = {
        let mut line: String = String::new();
        std::io::stdin().read_line(&mut line).unwrap();
        line.split_whitespace()
            .map(|x| x.parse().unwrap())
            .collect()
    };
    let q: usize = {
        let mut line: String = String::new();
        std::io::stdin().read_line(&mut line).unwrap();
        line.trim().parse().unwrap()
    };
    let k: Vec<i64> = (0..q)
        .map(|_| {
            let mut line: String = String::new();
            std::io::stdin().read_line(&mut line).unwrap();
            line.trim().parse().unwrap()
        })
        .collect();

    // snip
    fn bis<P>(ok: i64, ng: i64, p: P) -> i64
        where P: Fn(i64) -> bool {
        let mid = (ok + ng) / 2;
        if (ok - ng).abs() == 1 {
            ok
        } else if p(mid) {
            bis(mid, ng, p)
        } else {
            bis(ok, mid, p)
        }
    }
    // snip

    let ans = k.iter()
        .map(|&x| bis(n, -1, |i| x <= a[i as usize]).to_string())
        .collect::<Vec<_>>()
        .join("\n");
    println!("{}", ans);
}

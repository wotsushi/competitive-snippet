#![allow(non_snake_case)]
#![allow(unused_variables)]

// https://onlinejudge.u-aizu.ac.jp/challenges/sources/PCK/Prelim/0339?year=2016

fn main() {
    let _N: usize = {
        let mut line: String = String::new();
        std::io::stdin().read_line(&mut line).unwrap();
        line.trim().parse().unwrap()
    };
    // snip
    let (_A, _B, _C): (Vec<usize>, Vec<usize>, Vec<usize>) = {
        let (mut _A, mut _B, mut _C) = (vec![], vec![], vec![]);
        for _ in 0.._N {
            let mut line: String = String::new();
            std::io::stdin().read_line(&mut line).unwrap();
            let mut iter = line.split_whitespace();
            _A.push(iter.next().unwrap().parse().unwrap());
            _B.push(iter.next().unwrap().parse().unwrap());
            _C.push(iter.next().unwrap().parse().unwrap());
        }
        (_A, _B, _C)
    };
    // snip
    let N = _N;
    let p: Vec<_> = (0..N).map(|i| (_A[i], _B[i], _C[i])).collect();

    let ans = (0..N).filter(|&i| {
        let mut x = vec![p[i].0, p[i].1, p[i].2];
        x.sort();
        ((i + 1)..N).any(|j| {
            let mut y = vec![p[j].0, p[j].1, p[j].2];
            y.sort();
            (x[0], x[1], x[2]) == (y[0], y[1], y[2])
        })
    })
    .count();

    println!("{}", ans);
}

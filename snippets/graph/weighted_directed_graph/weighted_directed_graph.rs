#![allow(non_snake_case)]
#![allow(unused_variables)]
#![allow(dead_code)]

fn main() {
    let (_N, _M, r): (usize, usize, usize) = {
        let mut line: String = String::new();
        std::io::stdin().read_line(&mut line).unwrap();
        let mut iter = line.split_whitespace();
        (
            iter.next().unwrap().parse().unwrap(),
            iter.next().unwrap().parse().unwrap(),
            iter.next().unwrap().parse().unwrap()
        )
    };
    let (_A, _B, _C): (Vec<usize>, Vec<usize>, Vec<i64>) = {
        let (mut _A, mut _B, mut _C) = (vec![], vec![], vec![]);
        for _ in 0.._M {
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
    let _G = {
        let mut _G = vec![std::collections::HashMap::new(); _N + 1];
        for i in 0.._M { _G[_A[i]].insert(_B[i], _C[i]); }
        _G
    };
    // snip

    let V = _N;
    let E = _M;
    let s = _A;
    let t = _B;
    let d = _C;
    let G = _G;
    const INF: i64 = 1_000_000_000_000_000;
    let mut dp = vec![INF; V];
    let mut q = std::collections::BinaryHeap::new();
    q.push((0, r));
    while !q.is_empty() {
        let (dist, i) = {
            let (dist, i) = q.pop().unwrap();
            (-dist, i)
        };
        if dist < dp[i] {
            dp[i] = dist;
            for (&j, &w) in &G[i] { q.push((-(dist + w), j)); }
        }
    }
    let ans = dp.iter()
        .map(|&dist| if dist < INF { dist.to_string() } else { "INF".to_string() } )
        .collect::<Vec<_>>()
        .join("\n");

    println!("{}", ans);
}
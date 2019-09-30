#![allow(non_snake_case)]
#![allow(unused_variables)]
#![allow(dead_code)]

// https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/1/GRL_1_A

fn main() {
    let (V, E, r): (usize, usize, usize) = {
        let mut line: String = String::new();
        std::io::stdin().read_line(&mut line).unwrap();
        let mut iter = line.split_whitespace();
        (
            iter.next().unwrap().parse().unwrap(),
            iter.next().unwrap().parse().unwrap(),
            iter.next().unwrap().parse().unwrap()
        )
    };
    let (s, t, d): (Vec<usize>, Vec<usize>, Vec<i64>) = {
        let (mut s, mut t, mut d) = (vec![], vec![], vec![]);
        for _ in 0..E {
            let mut line: String = String::new();
            std::io::stdin().read_line(&mut line).unwrap();
            let mut iter = line.split_whitespace();
            s.push(iter.next().unwrap().parse().unwrap());
            t.push(iter.next().unwrap().parse().unwrap());
            d.push(iter.next().unwrap().parse().unwrap());
        }
        (s, t, d)
    };
    let G = {
        let mut G = vec![std::collections::HashMap::new(); V + 1];
        for i in 0..E { G[s[i]].insert(t[i], d[i]); }
        G
    };

    let _G = G;
    let _N = V;
    let _s = r;
    const _INF: i64 = 1_000_000_000_000_000;
    // snip
    let mut dp = vec![_INF; _N + 1];
    let mut q = std::collections::BinaryHeap::new();
    q.push((0, _s));
    while let Some((dist, i)) = q.pop() {
        let dist = -dist;
        if dist < dp[i] {
            dp[i] = dist;
            for (&j, &w) in &_G[i] { q.push((-(dist + w), j)); }
        }
    }
    // snip

    let ans = (0.._N)
        .map(|i| if dp[i] < _INF { dp[i].to_string() } else { "INF".to_string() } )
        .collect::<Vec<_>>()
        .join("\n");

    println!("{}", ans);
}
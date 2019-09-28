#![allow(non_snake_case)]
#![allow(unused_variables)]
#![allow(dead_code)]

// https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/all/GRL_3_C

fn main() {
    let (_N, _M): (usize, usize) = {
        let mut line: String = String::new();
        std::io::stdin().read_line(&mut line).unwrap();
        let mut iter = line.split_whitespace();
        (
            iter.next().unwrap().parse().unwrap(),
            iter.next().unwrap().parse().unwrap()
        )
    };
    let (_A, _B): (Vec<usize>, Vec<usize>) = {
        let (mut _A, mut _B) = (vec![], vec![]);
        for _ in 0.._M {
            let mut line: String = String::new();
            std::io::stdin().read_line(&mut line).unwrap();
            let mut iter = line.split_whitespace();
            _A.push(iter.next().unwrap().parse().unwrap());
            _B.push(iter.next().unwrap().parse().unwrap());
        }
        (_A, _B)
    };
    let Q: usize = {
        let mut line: String = String::new();
        std::io::stdin().read_line(&mut line).unwrap();
        line.trim().parse().unwrap()
    };
    let (u, v): (Vec<usize>, Vec<usize>) = {
        let (mut u, mut v) = (vec![], vec![]);
        for _ in 0..Q {
            let mut line: String = String::new();
            std::io::stdin().read_line(&mut line).unwrap();
            let mut iter = line.split_whitespace();
            u.push(iter.next().unwrap().parse().unwrap());
            v.push(iter.next().unwrap().parse().unwrap());
        }
        (u, v)
    };
    // snip
    let _G = {
        let mut _G = vec![std::collections::HashSet::new(); _N + 1];
        for i in 0.._M { _G[_A[i]].insert(_B[i]); }
        _G
    };
    // snip

    let (V, E) = (_N, _M);
    let (s, t) = (_A, _B);
    let G = _G;
    fn f(i: usize, G: &Vec<std::collections::HashSet<usize>>, order: &mut Vec<usize>, reachable: &mut Vec<bool>) {
        if reachable[i] {
            reachable[i] = false;
            for &j in &G[i] { f(j, G, order, reachable); }
            order.push(i);
        }
    }
    let mut order = vec![];
    let mut reachable = vec![true; V];
    for i in 0..V { f(i, &G, &mut order, &mut reachable); }
    let G_inv = {
        let mut G_inv = vec![std::collections::HashSet::new(); V];
        for i in 0..E { G_inv[t[i]].insert(s[i]); }
        G_inv
    };
    fn g(i: usize, k: usize, G_inv: &Vec<std::collections::HashSet<usize>>, scc: &mut Vec<usize>) {
        if scc[i] == 0 {
            scc[i] = k;
            for &j in &G_inv[i] { g(j, k, G_inv, scc); }
        }
    }
    let mut scc = vec![0; V];
    for (k, &i) in order.iter().rev().enumerate() { g(i, k + 1, &G_inv, &mut scc); }
    let ans = (0..Q)
        .map(|i| if scc[u[i]] == scc[v[i]] { 1.to_string() } else { 0.to_string() })
        .collect::<Vec<_>>()
        .join("\n");

    println!("{}", ans);
}
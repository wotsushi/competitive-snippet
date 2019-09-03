#![allow(non_snake_case)]
#![allow(unused_variables)]

// https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/2/GRL_2_A

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
        for i in 0.._M {
            _G[_A[i]].insert(_B[i], _C[i]);
            _G[_B[i]].insert(_A[i], _C[i]);
        }
        _G
    };
    // snip

    let (V, E) = (_N, _M);
    let (s, t, w) = (_A, _B, _C);
    let G = _G;
    let mst = {
        let mut used = vec![false; G.len()];
        let mut res = 0;
        let mut q = std::collections::BinaryHeap::new();
        used[1] = true;
        for (&j, &w) in &G[1] { q.push((-w, j)); }
        while !q.is_empty() {
            let (w, j) = q.pop().unwrap();
            if !used[j] {
                used[j] = true;
                res += -w;
                for (&j2, &w2) in &G[j] { q.push((-w2, j2)); }
            }
        }
        res
    };

    let ans = mst;

    println!("{}", ans);
}

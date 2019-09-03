#![allow(non_snake_case)]
#![allow(unused_variables)]

// https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/2/GRL_2_A

fn main() {
    let (V, E): (usize, usize) = {
        let mut line: String = String::new();
        std::io::stdin().read_line(&mut line).unwrap();
        let mut iter = line.split_whitespace();
        (
            iter.next().unwrap().parse().unwrap(),
            iter.next().unwrap().parse().unwrap()
        )
    };
    let (s, t, w): (Vec<usize>, Vec<usize>, Vec<i64>) = {
        let (mut s, mut t, mut w) = (vec![], vec![], vec![]);
        for _ in 0..E {
            let mut line: String = String::new();
            std::io::stdin().read_line(&mut line).unwrap();
            let mut iter = line.split_whitespace();
            s.push(iter.next().unwrap().parse().unwrap());
            t.push(iter.next().unwrap().parse().unwrap());
            w.push(iter.next().unwrap().parse().unwrap());
        }
        (s, t, w)
    };
    let _G = {
        let mut _G = vec![std::collections::HashMap::new(); V + 1];
        for i in 0..E {
            _G[s[i]].insert(t[i], w[i]);
            _G[t[i]].insert(s[i], w[i]);
        }
        _G
    };

    // snip
    let mst = {
        let mut used = vec![false; _G.len()];
        let mut res = 0;
        let mut q = std::collections::BinaryHeap::new();
        used[1] = true;
        for (&j, &w) in &_G[1] { q.push((-w, j)); }
        while !q.is_empty() {
            let (w, j) = q.pop().unwrap();
            if !used[j] {
                used[j] = true;
                res += -w;
                for (&j2, &w2) in &_G[j] { q.push((-w2, j2)); }
            }
        }
        res
    };
    // snip

    let ans = mst;

    println!("{}", ans);
}

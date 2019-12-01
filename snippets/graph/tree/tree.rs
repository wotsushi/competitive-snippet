#![allow(non_snake_case)]
#![allow(unused_variables)]
#![allow(dead_code)]

fn main() {
    let n: usize = {
        let mut line: String = String::new();
        std::io::stdin().read_line(&mut line).unwrap();
        line.trim().parse().unwrap()
    };
    let (id, k, c) = {
        let mut V: Vec<Vec<usize>> = vec![];
        for _ in 0..n {
            let mut line: String = String::new();
            std::io::stdin().read_line(&mut line).unwrap();
            V.push(
                line.split_whitespace()
                    .map(|x| x.parse().unwrap())
                    .collect(),
            );
        }
        let id = (0..n).map(|i| V[i][0]).collect::<Vec<_>>();
        let k = (0..n).map(|i| V[i][1]).collect::<Vec<_>>();
        let c = (0..n)
            .map(|i| (2..(k[i] + 2)).map(|j| V[i][j]).collect::<Vec<_>>())
            .collect::<Vec<_>>();
        (id, k, c)
    };
    let _N = n;
    let mut is_root = vec![true; _N + 1];
    let G = {
        let mut G = vec![std::collections::HashSet::new(); _N + 1];
        for i in 0..N {
            for &j in &c[i] {
                G[id[i]].insert(j);
                G[j].insert(id[i]);
                is_root[j] = false;
            }
        }
        G
    };
    let _s = (0.._N).find(|&i| is_root[i]).unwrap();
    let mut indices = vec![0; _N + 1];
    for i in 0.._N {
        indices[id[i]] = i;
    }

    // snip
    let mut parent = vec![_N + 1; _N + 1];
    let mut children = vec![std::collections::HashSet::new(); _N + 1];
    parent[_s] = _s;
    fn construct_tree(
        i: usize,
        parent: &mut Vec<usize>,
        children: &mut Vec<std::collections::HashSet<usize>>,
        G: &Vec<std::collections::HashSet<usize>>,
    ) {
        for &j in &G[i] {
            if parent[j] == G.len() {
                parent[j] = i;
                children[i].insert(j);
                construct_tree(j, parent, children, &G);
            }
        }
    }
    construct_tree(_s, &mut parent, &mut children, &_G);
    // snip

    let mut dp = vec![0; _N + 1];
    fn f(
        i: usize,
        d: usize,
        dp: &mut Vec<usize>,
        children: &Vec<std::collections::HashSet<usize>>,
    ) {
        dp[i] = d;
        for &c in &children[i] {
            f(c, d + 1, dp, children);
        }
    }
    f(s, 0, &mut dp, &children);

    let ans = (0.._N)
        .map(|i| {
            format!(
                "node {}: parent = {}, depth = {}, {}, {:?}",
                i,
                if i == _s { -1 } else { parent[i] as i64 },
                dp[i],
                if i == _s {
                    "root"
                } else if !children[i].is_empty() {
                    "internal node"
                } else {
                    "leaf"
                },
                c[indices[i]]
            )
        })
        .collect::<Vec<_>>()
        .join("\n");

    println!("{}", ans);
}

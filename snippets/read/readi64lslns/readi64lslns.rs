#![allow(non_snake_case)]
#![allow(unused_variables)]

// https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/all/ITP1_7_C

fn main() {
    let (r, c): (usize, usize) = {
        let mut line: String = String::new();
        std::io::stdin().read_line(&mut line).unwrap();
        let mut iter = line.split_whitespace();
        (
            iter.next().unwrap().parse().unwrap(),
            iter.next().unwrap().parse().unwrap()
        )
    };
    let _N = r;
    // snip
    let _A: Vec<Vec<i64>> = {
        let mut _A = vec![];
        for _ in 0.._N {
            let mut line: String = String::new();
            std::io::stdin().read_line(&mut line).unwrap();
            _A.push(
                line.split_whitespace()
                    .map(|x| x.parse().unwrap())
                    .collect()
            );
        }
        _A
    };
    // snip

    let A = _A;
    let ans = {
        let mut B: Vec<_> = A.iter()
            .map(|a| {
                let mut b = a.clone();
                b.push(a.iter().sum());
                b
            })
            .collect();
        let x = (0..(c + 1))
                .map(|j| (0..r).map(|i| B[i][j]).sum())
                .collect::<Vec<_>>();
        B.push(x);
        B.iter()
            .map(|b|
                b.iter()
                    .map(std::string::ToString::to_string)
                    .collect::<Vec<_>>()
                    .join(" ")
            )
            .collect::<Vec<_>>()
            .join("\n")
    };

    println!("{}", ans);
}

#![allow(non_snake_case)]
#![allow(unused_variables)]
#![allow(dead_code)]

fn main() {
    let (a, b, c): (i64, i64, i64) = {
        let mut line: String = String::new();
        std::io::stdin().read_line(&mut line).unwrap();
        let mut iter = line.split_whitespace();
        (
            iter.next().unwrap().parse().unwrap(),
            iter.next().unwrap().parse().unwrap(),
            iter.next().unwrap().parse().unwrap(),
        )
    };

    let _A = vec![a, b, c];

    // snip
    let _B = {
        let mut _B = _A.clone();
        _B.sort();
        _B
    };
    // snip

    let ans = _B
        .iter()
        .map(|&b| b.to_string())
        .collect::<Vec<_>>()
        .join(" ");

    println!("{}", ans);
}

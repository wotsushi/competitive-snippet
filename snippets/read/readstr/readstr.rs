#![allow(non_snake_case)]
#![allow(unused_variables)]

// https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/all/ITP1_8_A

fn main() {
    // snip
    let _s: Vec<char> = {
        let mut line: String = String::new();
        std::io::stdin().read_line(&mut line).unwrap();
        line.trim().chars().collect()
    };
    // snip

    let S = _s;
    let ans = S.iter()
        .map(|c| if c.is_lowercase() {
            c.to_string().to_uppercase()
        } else {
            c.to_string().to_lowercase()
        })
        .collect::<Vec<_>>()
        .join("");

    println!("{}", ans);
}

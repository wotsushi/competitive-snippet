#![allow(non_snake_case)]
#![allow(unused_variables)]
#![allow(dead_code)]

fn main() {
    // snip
    let _S: String = {
        let mut line: String = String::new();
        std::io::stdin().read_line(&mut line).unwrap();
        line.trim().to_string()
    };
    // snip

    let P: String = {
        let mut line: String = String::new();
        std::io::stdin().read_line(&mut line).unwrap();
        line.trim().to_string()
    };

    let T = _S;
    let res = (0..(T.len().saturating_sub(P.len()) + 1))
        .filter(|&i| T[i..(i + P.len())] == P)
        .map(|i| i.to_string())
        .collect::<Vec<_>>()
        .join("\n");
    let ans = if res == "" { res } else { res + "\n" };
    print!("{}", ans);
}

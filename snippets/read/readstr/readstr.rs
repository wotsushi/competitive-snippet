#![allow(non_snake_case)]

fn main() {
    // snip
    let _s: Vec<char> = {
        let mut line: String = String::new();
        std::io::stdin().read_line(&mut line).unwrap();
        line.trim().chars().collect()
    };
    // snip
    println!("{:?}", s);
}

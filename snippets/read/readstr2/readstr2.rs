#![allow(non_snake_case)]
#![allow(unused_variables)]
#![allow(dead_code)]

fn main() {
    // snip
    let (_s, _t): (Vec<char>, Vec<char>) = {
        let mut line: String = String::new();
        std::io::stdin().read_line(&mut line).unwrap();
        let mut iter = line.split_whitespace();
        (
            iter.next().unwrap().trim().chars().collect(),
            iter.next().unwrap().trim().chars().collect()
        )
    };
    // snip
}

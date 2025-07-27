
// dram_validator_mock.rs
// Simulates memory usage to represent DRAM-intensive validation

use std::time::Instant;

fn main() {
    let size = 100_000_000; // ~100 MB
    let mut memory: Vec<u8> = Vec::with_capacity(size);
    let start = Instant::now();

    for i in 0..size {
        memory.push((i % 256) as u8);
    }

    let checksum: u64 = memory.iter().map(|&b| b as u64).sum();
    let elapsed = start.elapsed();

    println!("Simulated DRAM allocation complete.");
    println!("Checksum: {}", checksum);
    println!("Time taken: {:.2?}", elapsed);
}

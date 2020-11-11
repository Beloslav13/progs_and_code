package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	counts := make(map[string]int)
	files := os.Args[1:]
	if len(files) == 0 {
		countLines(os.Stdin, counts)
	} else {
		for _, arg := range files {
			f, err := os.Open(arg)
			if err != nil {
				fmt.Fprintf(os.Stderr, "dup2: %v\n", err)
			}
			countLines(f, counts)
		}
	}

}

func countLines(f *os.File, counts map[string]int) {
	input := bufio.NewScanner(f)
	for input.Scan() {
		if input.Text() == "exit" {
			break
		}
		counts[input.Text()]++
		fmt.Printf("Counts for: %v\n", counts)
	}
	if len(counts) != 0 {
		for key, value := range counts {
			fmt.Printf("%q: %d\n", key, value)
		}
	}
}

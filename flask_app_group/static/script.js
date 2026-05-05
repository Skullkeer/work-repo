function randomMovie() {
    const movies = ["Interstellar", "Harry Potter and the Philosphers stone", "Conclave", "Star Wars: Return of the Jedi", "Seven Samurai"];
    const rand_num = movies[Math.floor(Math.random() * 5)];
    alert(rand_num)
}

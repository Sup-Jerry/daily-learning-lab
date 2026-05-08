const scores = [65, 82, 91, 74, 88];

console.log("Original scores:", scores);

const passedScores = scores.filter((score) => score >= 80);
const boostedScores = scores.map((score) => score + 5);
const averageScore = scores.reduce((total, score) => total + score, 0) / scores.length;

console.log("Passed scores:", passedScores);
console.log("Boosted scores:", boostedScores);
console.log("Average score:", averageScore.toFixed(2));

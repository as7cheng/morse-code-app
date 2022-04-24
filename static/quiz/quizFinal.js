$(document).ready(function(){
    const result = $("#quizResultPrompt");

    if(scores >= 6) {
        result.html(`
            <p>Congratulations! You got ${scores} points!</p>
            <p>Your correction rate is ${scores}0%!</p>
            <p>You passed the tests!</p>
        `)
    } else {
        result.html(`
            <p>Unfortunately, You got ${scores} points!</p>
            <p>Your correction rate is ${scores}0%.</p>
            <p>You failed the tests.</p>
        `)
    }

    $("#quizFinalQuizAgainBtn").click(function() {
        window.location.href = `/quiz`;
    });

    $("#quizFinalLearnAgainBtn").click(function() {
        window.location.href = `/letters/0`;
    });

    $("#quizFinalBackHomeBtn").click(function() {
        window.location.href = `/home`;
    });
})
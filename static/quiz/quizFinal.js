$(document).ready(function(){
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
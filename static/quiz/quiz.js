$(document).ready(function(){
    $("#quizLearnAgainBtn").click(function() {
        window.location.href = `/letters`;
    });

    $("#quizStartBtn").click(function() {
        window.location.href = `/quiz/01`;
    });
})
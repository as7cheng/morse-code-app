function validateForm() {
    let val = $("#quizInput").val();
    const str1 = val;
    str1.trim();
    for(let c of str1) {
        console.log(c === '.');
        if(c !== '.' && c !== '-' && c !== ' ') {
            alert("Only '.' and '-' are allowed.");
            $("#quizInput").focus();
            return false;
        }
    }
}

$(document).ready(function () {
    // initial submit button
    $("#quizResultPrompt").empty();
    $("#quizSubmitBtn").empty();
    $("#quizSubmitBtn").html(`<button type="submit" class="btn btn-warning">Submit</button>`);

    $("#formSingle").ajaxForm(data => {
        console.log('result =', data);

        // if the answer is true
        if (data && data.correctness) {
            $("#quizResultPrompt").empty();
            $("#quizResultPrompt").html(`
                <p style="color: #6AA84F; font-size: 16px;">Yeah! Your answer is <b>CORRECT!</b></p>
                <p style="color: #5E5E5E; font-size: 16px;">The right answer is <b>${data.ans}</b></p>
            `);
            $("#quizInput").css('color', '#6AA84F');
            $("#quizInput").attr('disabled', 'disabled');
        } else { // if the answer is false
            $("#quizResultPrompt").empty();
            $("#quizResultPrompt").html(`
                <p style="color: red; font-size: 16px;">Sorry, your answer is <b>INCORRECT.</b></p>
                <p style="color: #5E5E5E; font-size: 16px;">The right answer is <b>${data.ans}</b></p>
            `);
            $("#quizInput").css('color', 'red');
            $("#quizInput").attr('disabled', 'disabled');
        }

        $("#quizSubmitBtn").empty();
        $("#quizSubmitBtn").html(`<button type="button" class="btn btn-warning" id="quizNext">Next</button>`);

        $("#quizScore").html(`Scores: ${data.scores}`);

        $("#quizNext").click(function () {
            window.location.href = data.id < 10 ? `/quiz/${data.id + 1}` : `/quiz/final`;
        })
    });
})